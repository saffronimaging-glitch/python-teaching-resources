# Debug the Logic Gates

# Debug 1
# This should print True only when both inputs are True.

a = True
b = False

and_gate = a or b

print("AND gate:", and_gate)


# Debug 2
# This should be a NAND gate.

a = True
b = True

nand_gate = a and b

print("NAND gate:", nand_gate)


# Debug 3
# This should be True only when the inputs are different.

a = True
b = False

xor_gate = a == b

print("XOR gate:", xor_gate)


# Debug 4
# This should activate only if the student is over 18 AND has ID.

age = 20
has_id = True

if age > 18 or has_id:
    print("Entry allowed")
else:
    print("Entry denied")
