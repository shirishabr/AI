
# FIRST ORDER LOGIC - FORWARD CHAINING

def unify(pattern, fact, subst=None):
    if subst is None:
        subst = {}

    if pattern == fact:
        return subst

    # Check variable
    if isinstance(pattern, str) and pattern.startswith("?"):
        if pattern in subst:
            return subst if subst[pattern] == fact else None
        subst[pattern] = fact
        return subst

    # Check compound expressions
    if isinstance(pattern, tuple) and isinstance(fact, tuple):
        if pattern[0] != fact[0] or len(pattern) != len(fact):
            return None

        for p, f in zip(pattern[1:], fact[1:]):
            subst = unify(p, f, subst)
            if subst is None:
                return None

        return subst

    return None


def substitute(expr, subst):
    if isinstance(expr, str) and expr.startswith("?"):
        return subst.get(expr, expr)

    if isinstance(expr, tuple):
        return (expr[0],) + tuple(
            substitute(arg, subst) for arg in expr[1:]
        )

    return expr


def forward_chaining(facts, rules, query):
    kb = list(facts)

    while True:
        new_facts = []

        for premises, conclusion in rules:

            # Match rule premises with existing facts
            def match_all(index, subst):
                if index == len(premises):
                    return [subst]

                results = []

                for fact in kb:
                    current = unify(
                        substitute(premises[index], subst),
                        fact,
                        dict(subst)
                    )

                    if current is not None:
                        results.extend(
                            match_all(index + 1, current)
                        )

                return results

            substitutions = match_all(0, {})

            for subst in substitutions:
                result = substitute(conclusion, subst)

                if result not in kb and result not in new_facts:
                    new_facts.append(result)

                    # Check query
                    answer = unify(result, query)

                    if answer is not None:
                        return True, answer

        if not new_facts:
            return False, None

        kb.extend(new_facts)


# Convert input into predicate format
def parse(text):
    name, args = text.strip().split("(", 1)
    args = args.rstrip(")")
    return (name.strip(),) + tuple(
        x.strip() for x in args.split(",")
    )


# MAIN PROGRAM
print("FIRST ORDER LOGIC - FORWARD CHAINING")

facts = []
rules = []

n = int(input("\nEnter number of facts: "))

print("Enter facts: ")
for i in range(n):
    facts.append(parse(input()))

r = int(input("\nEnter number of rules: "))

print("Enter rules in format: premise1 & premise2 -> conclusion")

for i in range(r):
    rule = input()
    left, right = rule.split("->")

    premises = [parse(x) for x in left.split("&")]
    conclusion = parse(right)

    rules.append((premises, conclusion))

query = parse(input("\nEnter query to prove: "))

result, substitution = forward_chaining(
    facts, rules, query
)

if result:
    print("\nQuery Proved!")
    print("Substitution:", substitution)
else:
    print("\nQuery Cannot Be Proved!")
