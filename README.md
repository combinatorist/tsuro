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
+------+------+------+
|      |      |      |
|      /      \      |
+---\ /        \-----+
|    x               |
|   / \              |
+--/   \-------------+
|       /----\       |
|      |      |      |
+------+------+------+
```

## Usage
Simply run:

    python tsuro.py

or:

    python test.py

Both print out results.
