# Truth Tables for Logic Gates

inputs = [
    [False, False],
    [False, True],
    [True, False],
    [True, True]
]

print("A\tB\tAND\tOR\tNAND\tNOR\tXOR\tXNOR")

for a, b in inputs:
    and_gate = a and b
    or_gate = a or b
    nand_gate = not (a and b)
    nor_gate = not (a or b)
    xor_gate = a != b
    xnor_gate = a == b

    print(a, b, and_gate, or_gate, nand_gate, nor_gate, xor_gate, xnor_gate, sep="\t")
