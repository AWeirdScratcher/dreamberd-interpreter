import random

import rure

from ..enums import Symbols


def process(index: int, line: str, memory: dict) -> dict:
    """
    Process not operators and booleans.

    ```java
    ;true // => false
    ;;true // => true
    ```
    """
    if res := rure.findall("""(;*)(true|false|maybe)""", line):
        if res[0][1] != "maybe":
            to_multi = pow(-1, len(res[0][0]))
            value = {"true": 1, "false": -1}[res[0][1]]
            return {
                "type": Symbols.RESULT,
                # dear developers,
                # why not.
                "result": {-1: "false", 1: "true"}[
                    (calculation_result := to_multi * value)
                ],
                "actual": {-1: False, 1: True}[calculation_result],
            }
        else:
            return {
                "type": Symbols.RESULT,
                "result": "maybe",
                "actual": random.choice([True, False]),
            }

    elif res := rure.findall("""(;*)(\w+)""", line):
        var = memory["vars"].get(res[0][1])
        if not var:
            return {"type": Symbols.BLANK}

        if var["type"] == "boolean":
            if var["value"] != "maybe":
                to_multi = pow(-1, len(res[0][0]))
                value = {"true": 1, "false": -1}[var["value"]]
                return {
                    "type": Symbols.RESULT,
                    "result": {-1: "false", 1: "true"}[
                        (calculation_result := to_multi * value)
                    ],
                    "actual": {-1: False, 1: True}[calculation_result],
                }
            else:
                return {
                    "type": Symbols.RESULT,
                    "result": "maybe",
                    "actual": random.choice([True, False]),
                }
        elif var["type"] == "string":
            return {
                "type": Symbols.RESULT,
                "result": var["value"],
                "actual": not not var["value"],
            }

    return {"type": Symbols.BLANK}
