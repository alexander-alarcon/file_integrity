import hashlib
from pathlib import Path

from args import Algorithm


def calculate_hash(file: Path, algorithm: Algorithm) -> str:
    """
    Calculate the hash value of a file using the specified algorithm.

    Args:
        file (Path): The path to the file whose hash is to be calculated.
        algorithm (Algorithm): The hashing algorithm to use for the calculation.

    Returns:
        str: The hexadecimal representation of the calculated hash value.
    """
    hash_algo = hashlib.new(algorithm)
    with open(file, "rb") as target:
        while chunk := target.read(4096):
            hash_algo.update(chunk)

    return hash_algo.hexdigest()
