#!/usr/bin/env python3


from argparse import ArgumentTypeError

from args import read_args
from integrity import check_integrity
from validation import validate_args


def main() -> None:
    """
    Main entry point.

    This function parses command-line arguments, validates them, and executes
    the check_integrity function to verify the integrity of files.
    """
    try:
        args = read_args()
        validate_args(args)
        check_integrity(
            source_file=args.source_file,
            algorithm=args.algorithm,
            copy_file=args.copy_file,
            provided_hash=args.provided_hash,
            num_threads=args.num_threads,
        )
    except (ArgumentTypeError, ValueError) as e:
        print(str(e))


if __name__ == "__main__":
    main()
