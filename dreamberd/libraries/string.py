import locale

import rure

from ..enums import Symbols
from ..output import error
from .not_operator import process as NotOper

locale.setlocale(locale.LC_ALL, "")  # set current locale

currency_info = locale.localeconv()
currency_symbol = currency_info["currency_symbol"].replace("$", r"\$")
# important, $ is a symbol for regex. Whether it's NT$, or simply a $, must be replaced to r'\$'

currency_symbol_pos = currency_info["p_cs_precedes"]
# 0 if symbol follows value, 1 if symbol precedes value

regex = r"\{(.*?)\}"
if currency_symbol_pos:
    formatted_regex = f"{currency_symbol}{regex}"
    actual_string = (f"{currency_symbol}" + "{VARIABLE}").replace("\\", "")
else:
    formatted_regex = f"{regex}{currency_symbol}"
    actual_string = ("{VARIABLE} + " f"{currency_symbol}").replace("\\", "")


def process(index: int, line: str, memory: dict) -> dict:
    """
    Process strings.
    """
    if line.startswith('"'):
        if "'" in line:
            error(index, line, "For now, you cannot add any other quotation marks.")
            return {"type": Symbols.RETURN}
    elif line.startswith("'"):
        if '"' in line:
            error(index, line, "For now, you cannot add any other quotation marks.")
            return {"type": Symbols.RETURN}

    if matches := rure.findall(rf"""["']+.*?{formatted_regex}.*?["']+""", line):
        # the "${...}" string (or something like "NT${...}")
        var = matches[0]
        if var.strip(";") in ["true", "false", "maybe"]:
            res = NotOper(index, var, memory)
            line = line.replace(actual_string.replace("VARIABLE", var), res["result"])
        else:
            found_var = memory["vars"].get(var)
            if not found_var:
                error(index, line, "Unknown syntax / variable: " + var)
                return {"type": Symbols.RETURN}

            line = line.replace(
                actual_string.replace("VARIABLE", var), found_var["value"]
            )
    if matches := rure.findall(r"""["']+(.*?)["']+""", line):
        exact_string = "".join(matches)
        return {"type": Symbols.RESULT, "result": exact_string}
    else:
        return {"type": Symbols.BLANK}
