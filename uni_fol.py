
def is_variable(x):
    return x.islower() and len(x) == 1


def occurs(var, term, subst):
    term = apply_subst(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(var, arg, subst) for arg in term[1:])

    return False


def apply_subst(term, subst):
    while isinstance(term, str) and term in subst:
        term = subst[term]

    if isinstance(term, tuple):
        return (term[0],) + tuple(
            apply_subst(arg, subst) for arg in term[1:]
        )

    return term


def unify(x, y, subst):
    x = apply_subst(x, subst)
    y = apply_subst(y, subst)

    if x == y:
        return True

    if isinstance(x, str) and is_variable(x):
        if occurs(x, y, subst):
            return False
        subst[x] = y
        return True

    if isinstance(y, str) and is_variable(y):
        if occurs(y, x, subst):
            return False
        subst[y] = x
        return True

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0]:
            return False

        if len(x) != len(y):
            return False

        for a, b in zip(x[1:], y[1:]):
            if not unify(a, b, subst):
                return False

        return True

    return False


# Read expressions from user
def parse_expression(expression):
    expression = expression.replace(" ", "")
    name, args = expression.split("(", 1)
    args = args.rstrip(")")
    return (name,) + tuple(args.split(","))


print("FIRST ORDER LOGIC - UNIFICATION")

e1 = input("Enter first expression: ")
e2 = input("Enter second expression: ")

expr1 = parse_expression(e1)
expr2 = parse_expression(e2)

subst = {}

if unify(expr1, expr2, subst):
    print("\nUnification Successful!")
    print("Substitution:")
    if subst:
        for var, value in subst.items():
            print(var, "=", value)
    else:
        print("No substitution required")

    print("Unified Expression:", apply_subst(expr1, subst))
else:
    print("\nUnification Failed!")
