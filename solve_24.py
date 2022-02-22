import sys
import itertools


OPERATIONS = ["+", "-", "*", "/"]


def solve(n):
    for e in itertools.permutations(n):
        for o in itertools.combinations_with_replacement(OPERATIONS, 3):
            equation = f"((({e[0]} {o[0]} {e[1]}) {o[1]} {e[2]}) {o[2]} {e[3]})"
            if eval(equation) == 24:
                print(equation, "= 24")


if __name__ == "__main__":
    n = sys.argv[1:5]
    if len(n) < 4:
        raise Exception("Not enough arguments, needs 4")
    # Supposed to be integer
    n = [int(e) for e in n]

    solve(n)
