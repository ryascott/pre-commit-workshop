import argparse
from typing import Sequence

from .check import validate_uppercase_filename


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='validate_uppercase_filename')
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames to process.',
    )

    args = parser.parse_args(argv)

    results = [validate_uppercase_filename(filename) for filename in args.filenames]
    return int(any(results))
