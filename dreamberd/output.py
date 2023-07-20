import random

import termcolor
from rich import print as pprint
from rich.console import Console
from rich.syntax import Syntax

console = Console()


def error(index: int, line: str, error: str):  # arg: error not used
    """
    Prints out an error.
    """
    print(termcolor.colored(f"⨯ {error}", "red", attrs=["bold"]))
    syntax = Syntax("\n" + f"  {index + 1} | " + line + "\n", "java", theme="one-dark")
    print()
    console.print(syntax)
    print(" " * 5, termcolor.colored("^" * len(line), "red"))
    print(
        termcolor.colored(
            random.choice(
                [
                    "How dare you make a mistake in the perfect programming language?",
                    "It's either our problem or yours...",
                    "This may be our fault, oops.",
                ]
            ),
            "red",
        )
    )
    print(termcolor.colored(f"(parts from line {index + 1})", "red"))


def print_state(*states, **options) -> None:
    pprint(*states, **options)


def syntax_out(output: str) -> None:
    syntax = Syntax(output, "java", theme="one-dark", background_color=None)
    console.print(syntax)


def aemi(index) -> None:
    print(
        termcolor.colored(
            f"AEMI: Fixed exclamation mark on line {index + 1}", attrs=["dark"]
        )
    )


def abi(index) -> None:
    print(
        termcolor.colored(
            f"ABI: Inserted a bracket on line {index + 1}", attrs=["dark"]
        )
    )


def aqmi(index) -> None:
    print(
        termcolor.colored(
            f"AQMI: awd so dalao I mean write docs there  {index + 1}", attrs=["dark"]
        )
    )
