import rure

from ..enums import Symbols
from ..output import error
from .type import process_type


def process(index: int, line: str, memory: dict) -> dict:
    """
    Processing declaration.

    # Constant Constants
    Can't be changed under any circumstances.
    ```java
    const const name = "Luke"!
    ```

    # Constant Variables
    Can be edited, but not re-assigned.
    ```java
    const var name = "Luke"!
    ```

    # Variable Constants
    Can be re-assigned, not edited.
    ```java
    var const name = "Luke"!
    ```

    # Variable Variables
    Can be re-assigned and edited
    ```java
    var var name = "Luke"!
    ```
    """
    if line.strip().startswith("const const "):
        if res := rure.findall("""const\s+const\s+(\w+) = (.*?)(!+)""", line):
            # const const
            context = res[0]
            plain_value = context[1]

            result = process_type(index, plain_value, memory)
            if result["type"] == Symbols.RETURN:
                return result

            value = result["value"]

            if context[0] in memory["vars"]:
                if (attr := memory["vars"][context[0]]["attribute"]) in [
                    "const const",
                    "const var",
                ]:
                    error(
                        index,
                        line,
                        f"Variable '{context[0]}' with attribute '{attr}' cannot be re-assigned.",
                    )
                    return {"type": Symbols.RETURN}
            memory["vars"][context[0]] = {
                "attribute": "const const",
                "description": "Cannot be changed in any way.",
                "type": result["type"],
                "value": value,
            }
            return {
                "type": Symbols.RESULT,
                "attribute": "const const",
                "result": {"name": context[0], "value": value},
            }
        else:
            error(index, line, "Syntax Error: invalid syntax for constant constants.")
            return {"type": Symbols.RETURN}

    elif line.strip().startswith("const var "):
        if res := rure.findall("""const\s+var\s+(\w+) = (.*?)(!+)""", line):
            # const var
            context = res[0]
            plain_value = context[1]

            result = process_type(index, plain_value, memory)
            if result["type"] == Symbols.RETURN:
                return result

            value = result["value"]

            if context[0] in memory["vars"]:
                if (attr := memory["vars"][context[0]]["attribute"]) in [
                    "const const",
                    "const var",
                ]:
                    error(
                        index,
                        line,
                        f"Variable '{context[0]}' with attribute '{attr}' cannot be re-assigned.",
                    )
                    return {"type": Symbols.RETURN}
            memory["vars"][context[0]] = {
                "attribute": "const var",
                "description": "Can be edited, but not re-assigned.",
                "type": result["type"],
                "value": value,
            }
            return {
                "type": Symbols.RESULT,
                "attribute": "const var",
                "result": {"name": context[0], "value": value},
            }
        else:
            error(index, line, "Syntax Error: invalid syntax for constant variables.")
            return {"type": Symbols.RETURN}

    elif line.strip().startswith("var const "):
        if res := rure.findall(r"""var\s+const\s+(\w+) = (.*?)(!+)""", line):
            # var const
            context = res[0]
            plain_value = context[1]

            result = process_type(index, plain_value, memory)
            if result["type"] == Symbols.RETURN:
                return result

            value = result["value"]

            if context[0] in memory["vars"]:
                if (attr := memory["vars"][context[0]]["attribute"]) in [
                    "const const",
                    "const var",
                ]:
                    error(
                        index,
                        line,
                        f"Variable '{context[0]}' with attribute '{attr}' cannot be re-assigned.",
                    )
                    return {"type": Symbols.RETURN}
            memory["vars"][context[0]] = {
                "attribute": "var const",
                "description": "Can be re-assigned, but not edited.",
                "type": result["type"],
                "value": value,
            }
            return {
                "type": Symbols.RESULT,
                "attribute": "var const",
                "result": {"name": context[0], "value": value},
            }
        else:
            error(index, line, "Syntax Error: invalid syntax for variable constants.")
            return {"type": Symbols.RETURN}
    else:
        return {"type": Symbols.BLANK}
