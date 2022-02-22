import sys
import itertools


OPERATIONS = ["+", "-", "*", "/"]


def check_equation(equation):
    if eval(equation) == 24:
        print(equation, "= 24")


def solve(n):
    for e in itertools.permutations(n):
        for o in itertools.product(OPERATIONS, OPERATIONS, OPERATIONS):
            e0, e1, e2, e3 = e
            o0, o1, o2 = o
            check_equation(f"(({e0} {o0} {e1}) {o1} {e2}) {o2} {e3}")
            check_equation(f"({e0} {o0} ({e1} {o1} {e2})) {o2} {e3}")
            check_equation(f"({e0} {o0} {e1}) {o1} ({e2} {o2} {e3})")
            check_equation(f"{e0} {o0} (({e1} {o1} {e2}) {o2} {e3})")
            check_equation(f"{e0} {o0} ({e1} {o1} ({e2} {o2} {e3}))")


if __name__ == "__main__":
    n = sys.argv[1:5]
    if len(n) < 4:
        raise Exception("Not enough arguments, needs 4")
    # Supposed to be integer
    n = [int(e) for e in n]

    solve(n)
