from copy import deepcopy

def main():
    "script to print out default results (no arguments)"
    from pprint import pprint
    naive = refine()

    print("\nnaive piece descriptions:")
    pprint(naive)

    print("\nsymmetries:")
    equivalence_classes = symmetries(flatten(naive))
    pprint(equivalence_classes)

    print("\ncannonical piece descriptions:")
    pprint(representative(equivalence_classes))

def representative(equivalence_classes):
    "grabs the first (i.e. cannonical) example from each equivalence_class"
    return [x[0] for x in equivalence_classes]

def symmetries(pieces):
    "organizes piece descriptions into equivalence_classes based on rotation"
    equivalence_classes = [pieces[:1]]
    for piece in pieces[1:]:
        matched = False
        for ec in equivalence_classes:
            matched = same_piece(piece, ec[0])
            if matched:
              ec.append(piece)
              break
        if matched:
          continue
        equivalence_classes.append([piece])
    return equivalence_classes

def same_piece(piece, cannon):
    "checks whether two piece descriptions are equivalent (by rotation)"
    piece_copy = deepcopy(piece)
    for rotation in range(3):
        piece_copy = rotate(piece_copy)
        if piece_copy == cannon:
            return True
    return False

def rotate(piece):
    "rotates a piece description"
    return tuple(sorted(tuple(sorted((x + 2) % 8 for x in edge)) for edge in piece))

def flatten(nested4levels):
    "flattens the nested list of recursive refinements"
    return [z for w in nested4levels for x in w for y in x for z in y]

def refine(piece = ()):
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
