import os
from typing import Optional

DEFAULT_NUM_THREADS = 4
MAX_NUM_THREADS = 32
ADDITIONAL_THREADS = 4


def calculate_threads(num_threads: Optional[int]) -> int:
    """
    Calculate the number of threads to use for concurrent processing.

    This function calculates the number of threads to use for concurrent processing
    based on the number of available CPU cores and a provided num_threads argument.

    Args:
        num_threads (int, optional): The desired number of threads to use.
            If None, the function will determine the number of threads based on
            the available CPU cores. Defaults to None.

    Returns:
        int: The calculated number of threads to use. If num_threads is provided,
            it returns the provided value if it is valid. Otherwise, it returns
            a default value of DEFAULT_NUM_THREADS threads if num_threads is None, or the maximum
            possible number of threads based on available CPU cores if num_threads
            exceeds the maximum.

    Raises:
        ValueError: If num_threads is less than or equal to 0.

    Notes:
        If the CPU count information is not available, the function uses a default
        value of DEFAULT_THREADS threads.
    """
    available_cores: Optional[int] = os.cpu_count()

    if available_cores is None:
        print(f"CPU count not available. Using default value: {DEFAULT_NUM_THREADS}")
        return DEFAULT_NUM_THREADS

    max_threads = min(MAX_NUM_THREADS, available_cores + ADDITIONAL_THREADS)

    if num_threads is None or num_threads <= 0:
        return min(DEFAULT_NUM_THREADS, max_threads)
    else:
        return min(max_threads, num_threads)
