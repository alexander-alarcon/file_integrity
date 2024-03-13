from argparse import ArgumentParser, Namespace
from enum import StrEnum
from pathlib import Path
from typing import NamedTuple, Optional

from file_integrity.threads import calculate_threads


class Algorithm(StrEnum):
    MD5 = "md5"
    SHA256 = "sha256"


class Args(NamedTuple):
    source_file: Path
    copy_file: Optional[Path]
    algorithm: Algorithm = Algorithm.MD5
    provided_hash: Optional[str] = None
    num_threads: int = calculate_threads(None)


def read_args() -> Args:
    parser = ArgumentParser(description="Utility to check integrity of files")
    parser.add_argument(
        "source_file",
        help="Path to the original file whose integrity is to be verified.",
        type=Path,
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        help="Hashing algorithm to use for verification. Default is md5",
        choices=[algo.value for algo in Algorithm],
        default=Algorithm.MD5.value,
    )
    parser.add_argument("-t", "--threads", help="Number of threads to use.", type=int)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-p",
        "--provided-hash",
        help="Hash value of the file to compare against (for direct hash comparison).",
    )
    group.add_argument(
        "-c",
        "--copy-file",
        help="Path to the file to compare against the source file (for hash comparison).",
        type=Path,
    )

    args: Namespace = parser.parse_args()

    return Args(
        source_file=args.source_file,
        copy_file=args.copy_file,
        algorithm=args.algorithm,
        provided_hash=args.provided_hash,
        num_threads=calculate_threads(args.threads),
    )
