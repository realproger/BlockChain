# Simple Blockchain Implementation

This is a simple implementation of a blockchain using Python. The code defines a `Block` class that creates a basic blockchain structure and generates a hash for each block using the SHA-256 algorithm.

## Overview

The Python script consists of the following components:

### Block Class

The `Block` class represents a block in the blockchain. Each block contains:
- `prev_hash`: The hash of the previous block
- `transaction`: Details about the transaction
- `amount`: The amount related to the transaction
- `hash`: The hash of the current block
- `time`: Timestamp of the block creation

### Methods

#### `__init__`
- Initializes the Block class with provided parameters and generates the block hash.

#### `get_data`
- Returns the data associated with the block.

#### `make_hash`
- Creates a hash for the block using SHA-256.

#### `add_data`
- Adds new data (transaction, amount) to the blockchain.

#### `print_blocks`
- Prints the information of all the blocks in the blockchain.

## Usage

To use this code:
1. Initialize a block using `Block(prev_hash, transaction, amount)`.
2. Add more data to the blockchain using `add_data(transaction, amount)`.
3. View the details of the blockchain using `print_blocks(block)`.

### Example

```python
test_block = Block('000746bd11a3a38ad2ac56a51cec7be5ce5930da347d8b31b5ef505568182a49', 'Ivan', 100)
test_block.add_data("Boris", 1042)
print_blocks(test_block)
