from itertools import product

print("TRUTH TABLE")

headers = ["P", "Q", "R", "Q->P", "P->~Q", "QvR", "KB", "R->P", "Q->R"]

rows = []

for P, Q, R in product([False, True], repeat=3):

    a = (not Q) or P
    b = (not P) or (not Q)
    c = Q or R

    KB = a and b and c

    d = (not R) or P
    e = (not Q) or R

    row = [P, Q, R, a, b, c, KB, d, e]
    rows.append(["T" if x else "F" for x in row])

widths = [max(len(headers[i]), 3) for i in range(len(headers))]

border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

print(border)
print("|" + "|".join(" " + headers[i].center(widths[i]) + " " for i in range(len(headers))) + "|")
print(border)

for row in rows:
    print("|" + "|".join(" " + row[i].center(widths[i]) + " " for i in range(len(row))) + "|")

print(border)

# Check entailment
kb_models = []

for P, Q, R in product([False, True], repeat=3):

    KB = ((not Q) or P) and ((not P) or (not Q)) and (Q or R)

    if KB:
        kb_models.append((P, Q, R))

r_result = all(R for P, Q, R in kb_models)
rp_result = all((not R) or P for P, Q, R in kb_models)
qr_result = all((not Q) or R for P, Q, R in kb_models)


print(" KB entail R", "YES" if r_result else "NO")
print(" Does KB entail R -> P", "YES" if rp_result else "NO")
print(" Does KB entail Q -> R", "YES" if qr_result else "NO")
