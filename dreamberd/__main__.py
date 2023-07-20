import os
import sys

try:
    from dreamberd import interprete
except ModuleNotFoundError:
    sys.exit("Use -m keyword.")

from argparse import ArgumentParser

parser = ArgumentParser(
    prog="DreamBerd Interpreter (Python)",
    description="The perfect programming language.",
)
parser.add_argument("content", help="The file or code to run.")
args = parser.parse_args()

if os.path.exists(args.content):
    with open(args.content, "r", encoding="utf-8") as file:
        content: str = file.read()
else:
    content = args.content

interprete(content)
