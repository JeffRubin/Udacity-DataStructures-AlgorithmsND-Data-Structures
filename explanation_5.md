# Problem 5: Blockchain

## Overview
Implemented a linked list for the blockchain.  Kept track of the head and tail for the linked list so could add new
blocks to the list quickly at the tail instead of having to iterate from the head of the list to the end and then add a
new block.

## Time Complexity: O(1) (block creation)
- O(1) to create a new block and add it to the blockchain at the tail.
- O(n) where n is the number of blocks in the chain to verify the chain since have to check every block.  This is
very interesting since it seems to ensure the integrity of the chain since if data is modified or a block is deleted
all subsequent blocks in the chain have to be updated.  Real blockchains probably have many blocks so correcting
all subsequent would be very time consuming.

## Space Complexity: O(n)
- O(n) where n is the number of blocks in the chain
