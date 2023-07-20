from ..enums import Symbols
from ..output import error
from .not_operator import process as NotOper
from .string import process as String


def process_type(*args) -> dict:
    string = String(*args)
    if string["type"] == Symbols.RESULT:
        return {"type": "string", "value": string["result"]}

    notoper = NotOper(*args)
    if notoper["type"] == Symbols.RESULT:
        return {
            "type": "boolean",
            "value": notoper["result"],
            "actual": notoper["actual"],
        }

    if s := args[2]["vars"].get(args[1]):
        return {"type": "variable", "attribute": s["attribute"], "value": s["value"]}

    error(args[0], args[1], f"Unknown variable / syntax: {args[1]}")
    return {"type": Symbols.RETURN}
