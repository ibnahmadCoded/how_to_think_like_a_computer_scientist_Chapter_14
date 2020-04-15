def main():
    import random

    board = list(range(8)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        random.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(board, tries))
            tries = 0
            num_found += 1

main()
