from copy import deepcopy

def main():
    "script to print out default results (no arguments)"
    from pprint import pprint

    print("\nnaive piece descriptions:")
    naive = refine()
    pprint(naive)

    print("\nsymmetries:")
    equivalence_classes = symmetries(flatten(naive))
    pprint(equivalence_classes)

    print("\ncanonical piece descriptions:")
    canonical_pieces = representative(equivalence_classes)
    pprint(canonical_pieces)

    return canonical_pieces

def representative(equivalence_classes):
    "grabs the first (i.e. canonical) example from each equivalence_class"
    return [x[0] for x in equivalence_classes]

def symmetries(pieces):
    "organizes piece descriptions into equivalence_classes based on rotation"
    equivalence_classes = [pieces[:1]]
    for piece in pieces[1:]:
        matched = False
        for equivalence_class in equivalence_classes:
            matched = same_piece(piece, equivalence_class[0])
            if matched:
                equivalence_class.append(piece)
                break
        if matched:
            continue
        equivalence_classes.append([piece])
    return equivalence_classes

def same_piece(piece, canon):
    "checks whether two piece descriptions are equivalent (by rotation)"
    piece_copy = deepcopy(piece)
    for _ in range(3):
        piece_copy = rotate(piece_copy)
        if piece_copy == canon:
            return True
    return False

def rotate(piece):
    "rotates a piece description"
    return tuple(sorted(rotate_path(path) for path in piece))

def rotate_path(path):
    "rotates a path on a piece"
    return tuple(sorted((x + 2) % 8 for x in path))

def flatten(nested4levels):
    "flattens the nested list of recursive refinements"
    return [z for w in nested4levels for x in w for y in x for z in y]

def refine(piece=()):
    "recurses into all possible piece descriptions"
    if len(piece) == 4:
        return piece
    avail = available(piece)
    return [refine(piece + ((avail[0], x),)) for x in avail[1:]]

def next_start(piece):
    "finds start position for next path connection"
    return min(available(piece))

def available(piece):
    "finds all available positions to be connected by a path"
    used_positions = [x for row in piece for x in row]
    return [x for x in range(8) if x not in used_positions]

if __name__ == '__main__':
    main()
