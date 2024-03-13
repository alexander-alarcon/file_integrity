# File Integrity Checker CLI

A command-line utility to check the integrity of files using cryptographic hashing algorithms.

## Description

This CLI tool allows users to verify the integrity of files by comparing their cryptographic hashes.
It supports various hashing algorithms and can compare a file against either another file :quot::qor a provided hash value.

## Features

- Calculate the cryptographic hash of a file using MD5 or SHA-256 algorithms.
- Compare the hash of a file against another file or a provided hash value.
- Automatically determine the number of threads based on available CPU cores.

## Supported Hashing Algorithms

The following hashing algorithms are supported:

- **MD5**: Produces a 128-bit hash value, commonly used for checksums and file integrity verification.
- **SHA-256**: Produces a 256-bit hash value, considered more secure than MD5 and suitable for cryptographic applications.


## Usage

```bash
python file_integrity/main.py [source_file] [-a ALGORITHM] [-c COPY_FILE | -p PROVIDED_HASH] [-t THREADS]
```


- `source_file`: Path to the original file whose integrity is to be verified.
- `-a, --algorithm ALGORITHM`: Hashing algorithm to use for verification (default is MD5).
- `-c, --copy-file COPY_FILE`: Path to the file to compare against the source file (for hash comparison).
- `-p, --provided-hash PROVIDED_HASH`: Hash value of the file to compare against (for direct hash comparison).
- `-t, --threads THREADS`: Number of threads to use for concurrent processing.


