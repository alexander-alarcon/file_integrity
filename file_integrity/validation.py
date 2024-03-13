from argparse import ArgumentTypeError
from pathlib import Path

from file_integrity.args import Args


def file_exists(file: Path, error_message: str) -> None:
    if not file.exists():
        raise ArgumentTypeError(error_message)


def validate_args(args: Args) -> None:
    file_exists(args.source_file, "Error: The specified source file does not exist.")
    if args.copy_file:
        file_exists(args.copy_file, "Error: The specified copy file does not exist.")
