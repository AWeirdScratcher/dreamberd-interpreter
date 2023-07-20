import rure

from ..enums import Symbols
from .type import process_type


def process(index, line, memory) -> dict:
    """
    Process if statements and send a symbol back to the HQ.
    """
    if res := rure.findall(r"""if\s+\((.*?)\)\s*\{""", line, rure.MULTILINE):
        type_ = process_type(index, res[0], memory)
        value = None

        if type_["type"] == Symbols.RETURN:
            return {"type": Symbols.RETURN}

        if type_["type"] == "boolean":
            value = type_["actual"]
        else:
            value = not not type_["value"]  # bool

        return {"type": Symbols.IF__FIND_CURLY_BRACKETS, "execute": value}

    return {"type": Symbols.BLANK}
