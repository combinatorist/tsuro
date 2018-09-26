# tsuro
analysis of the 35 pieces in the game tsuro

## Motivation
The game pieces are based on an interesting combinatorial problem.
I hope to expand this with generalizations, formulas, and optimizations.

## Game Piece Description
- Each Tsuro piece is a square.
- Each edge of the square has two nodes on it.
- Each node has a path connecting it to exactly one other node on the piece.
- That other node may be on the same side or a different one.
- The game has exactly one of each possible piece (up to rotation).

```
         4      5
  +------+------+------+
  |      |      |      |
  |      /      \      |
3 +---\ /        \-----+ 6
  |    x               |
  |   / \              |
2 +--/   \-------------+ 7
  |       /----\       |
  |      |      |      |
  +------+------+------+
         1      0
```

## Notation / Data Structure
- I numbered the nodes around the square 0 - 7.
- To describe a piece, I list 4 pairs (paths) of connected nodes.
- For comparison, I sort the nodes in a pair and the pairs in the list.
- Of all the equivalent descriptions, the first by sorting is the canonical one.

Hence, the picture above is represented by the following piece description:

    ((0, 1), (2, 4), (3, 7), (5, 6))

Notice, the first node in each pair is just the next available node (starting with 0).
Furthermore, the last pair is just whatever's left over.
So, you could compress the data structure to: `(1, 4, 7)`.
But that would be less human readable and would require decompression anyway for rotations.

## Usage
Simply run:

    python tsuro.py

or:

    python test.py

Both print out results.
