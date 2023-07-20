import locale

import rure
import termcolor

from .enums import Symbols
from .libraries.declare import process as Declare
from .libraries.if_statements import process as IfStatements
from .libraries.not_operator import process as NotOper
from .libraries.string import process as String, actual_string as actual_currency_string
from .libraries.type import process_type
from .output import abi, aemi, error, print_state

function = r"[function]{2,8}\s(\w*)\s*\((?:\w+(?:,\s)?)*\)\s=>\s*{([\s\S]*?)}"


class UnknownVar(object):
    """Unknown variable."""


def interprete(code: str) -> None:
    """
    Interprete a `.db` source file / code.
    """
    FILE = "main.db"
    # storage is only used when there are multiple files
    # just as lazy as i am
    STORAGE = {"main.db": {"vars": {}}}

    memory = {"vars": {}}
    states = []
    indent = 0

    def make_state():
        """Show debug information."""
        print_state("[yellow]=> [/yellow]", end="")
        print_state(
            {
                "line": index + 1,
                "vars": memory["vars"],
                "locale": {
                    "interpolation": actual_currency_string,
                    "locale": locale.setlocale(locale.LC_ALL, ""),
                },
            }
        )

    iterator = enumerate(code.splitlines())
    if code.splitlines()[-1].startswith("reverse"):
        code = code.splitlines()[:-1]
        iterator = reversed(list(enumerate(code)))

    for index, line in iterator:
        if line.startswith("//"):
            continue
        elif line.startswith("/*"):
            states.append("COMMENT2")
            continue

        if "COMMENT2" in states:
            if line.endswith("*/"):
                states.remove("COMMENT2")
            continue

        if "if_find" in states or "if_find&exec" in states:  # no exec
            actual_state = "if_find" if "if_find" in states else "if_find&exec"

            if line.strip().startswith("}"):
                indent -= 3
                states.remove(actual_state)
                continue

            if "exec" not in actual_state:
                continue  # true / false both continue for NO_EXEC

        if not line.strip():
            continue

        # count indents
        if spaces := rure.findall("^(\s*)\S", line):
            if len(spaces[0]) != indent:
                s_count = len(spaces[0])
                error(
                    index,
                    "▒" * s_count + line[s_count:],
                    f"Invalid indent, we take it seriously. At this point, the indent should be {indent}.",
                )
                return

        line = rure.findall("^(.*?)\s*(?://.*)?$", line)[0]

        if line == "?":
            make_state()
            continue

        if line.startswith("====="):
            if file := rure.findall(r"""[=]{5,}\s+(.+?\.db)\s+[=]{5,}""", line):
                if file[0] == "main.db" == FILE:
                    print(
                        termcolor.colored(
                            "Tip: Developers like to save time (= money). You don't need to name the file 'main.db' as this is the default one.\n...or if you're lazy like me, just don't.",
                            attrs=["dark"],
                        )
                    )
                else:
                    # NEXT FILE
                    FILE = file[0]
                    STORAGE[file[0]] = memory
                    memory = STORAGE[FILE]

                continue
            else:
                error(
                    index,
                    line,
                    "Invalid file structure. Must be like:\n  ===== file_name_here.db =====",
                )
                return

        if line.strip().startswith("export "):
            if not line.endswith("!"):
                aemi(index)
                line += "!"
            if res := rure.findall(r"""export\s+(\w+?)\s+to\s+"+(.*\.db)"+""", line):
                data, file = res[0]
                var = memory["vars"].get(data)
                if not var:
                    error(index, line, f"Error: Undefined variable: {var}")
                    return
                if not STORAGE.get(file):
                    STORAGE[file] = {"vars": {}}
                STORAGE[file]["vars"][data] = var

                continue
        if line.strip().startswith("print("):
            if not line.endswith(("!", "?")):
                if rure.findall(r"""["']+.*""", line) and not line.endswith(')'):
                    abi(index)
                    line += ")!"
                elif line.endswith(")"):
                    aemi(index)
                    line += "!"

            if res := rure.findall(r"""print\((.*)\)(!*)(\??)""", line):
                context = res[0]
                if context[0]:
                    string = String(index, context[0], memory)
                    if string["type"] == Symbols.RETURN:
                        return
                    if string["type"] == Symbols.BLANK:
                        not_oper = NotOper(index, context[0], memory)
                        if not_oper["type"] == Symbols.BLANK:
                            message = (
                                memory["vars"]
                                .get(context[0], {})
                                .get("value", UnknownVar)
                            )
                            if message is UnknownVar:
                                error(
                                    index,
                                    line,
                                    f"Unknown Variable / Syntax: {context[0]}",
                                )
                                return
                        else:
                            message = not_oper["result"]
                    else:
                        message = string["result"]
                else:
                    message = ""

                if context[2] and context[1]:
                    error(
                        index,
                        line,
                        "You should NOT be bold and unsure at the same time. However, you can be bold that you're unsure.",
                    )
                    return
                if context[2] == "?":  # unsure
                    print(termcolor.colored(f"(?) {message}", "yellow"))
                    make_state()
                    continue
                elif context[1].startswith("!"):  # !
                    if len(context[1]) >= 3 and len(context[1]) <= 10:
                        print(termcolor.colored(message, attrs=["bold"]))
                        continue

                    elif len(context[1]) > 10:
                        error(
                            index,
                            line,
                            "CPU Failure: You're being too BOLD about this.",
                        )
                        return
                    else:
                        print(message)
                        continue

            else:
                # syntax error for print()!
                error(index, line, "Syntax Error: Should be print(...)!")
                return

        statement = IfStatements(index, line, memory)

        if statement["type"] == Symbols.RETURN:
            return

        if statement["type"] == Symbols.IF__FIND_CURLY_BRACKETS:
            states.append("if_find" + ("&exec" if statement["execute"] else ""))
            indent += 3
            continue

        if not line.endswith(("!", "?")):
            aemi(index)
            line += "!"

        res = Declare(index, line, memory)
        if res["type"] == Symbols.RETURN:
            return
        elif res["type"] == Symbols.RESULT:  # declared
            continue

        error(
            index,
            line,
            f"Invalid syntax: {f'{line[:20]}...' if len(line) >= 20 else line}",
        )
        return
