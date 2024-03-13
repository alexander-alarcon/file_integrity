from concurrent.futures import as_completed, ProcessPoolExecutor
from pathlib import Path
from typing import Optional

from args import Algorithm
from hash import calculate_hash


def check_integrity(
    source_file: Path,
    algorithm: Algorithm,
    copy_file: Optional[Path],
    provided_hash: Optional[str],
    num_threads: Optional[int],
):
    """
    Check the integrity of files by calculating their hash values.

    This function calculates the hash values of the source file and, if provided,
    the copy file, using the specified algorithm. It then compares the calculated
    hash values with the provided hash or with each other to determine if the files
    are identical or if their integrity has been compromised.

    Args:
        source_file (Path): The path to the original file whose integrity is to be verified.
        algorithm (Algorithm): The hashing algorithm to use for the calculation.
        copy_file (Path, optional): The path to the file to compare against the source file
            (for hash comparison). Defaults to None.
        provided_hash (str, optional): The hash value of the file to compare against
            (for direct hash comparison). Defaults to None.
        num_threads (int, optional): The number of threads to use for concurrent processing.
            Defaults to None.

    Raises:
        ValueError: If neither a copy file nor a provided hash is specified.

    """
    if not copy_file and not provided_hash:
        raise ValueError(
            "Error: Either a copy file or a provided hash must be specified."
        )

    hash_results = {}
    with ProcessPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        source_future = executor.submit(
            calculate_hash, file=source_file, algorithm=algorithm
        )
        futures.append(source_future)

        if copy_file:
            copy_future = executor.submit(
                calculate_hash, file=copy_file, algorithm=algorithm
            )
            futures.append(copy_future)

        for future in as_completed(futures):
            result = future.result()
            if future == source_future:
                hash_results["source_file"] = result
            else:
                hash_results["copy_file"] = result

    if provided_hash and provided_hash == hash_results["source_file"]:
        print("Source file hash matches provided hash.")

    elif copy_file and hash_results["copy_file"] == hash_results["source_file"]:
        print("Source file hash matches copy file hash.")

    else:
        print("Source file hash does not match provided hash or copy file hash.")
