# Stretch Challenge: Logic Gate Simulator

def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def nand_gate(a, b):
    return not (a and b)

def nor_gate(a, b):
    return not (a or b)

def xor_gate(a, b):
    return a != b

def xnor_gate(a, b):
    return a == b


print("Logic Gate Simulator")
print("Choose a gate: AND, OR, NAND, NOR, XOR, XNOR")

gate = input("Enter gate: ").upper()

a = input("Enter input A as 0 or 1: ")
b = input("Enter input B as 0 or 1: ")

a = a == "1"
b = b == "1"

if gate == "AND":
    result = and_gate(a, b)
elif gate == "OR":
    result = or_gate(a, b)
elif gate == "NAND":
    result = nand_gate(a, b)
elif gate == "NOR":
    result = nor_gate(a, b)
elif gate == "XOR":
    result = xor_gate(a, b)
elif gate == "XNOR":
    result = xnor_gate(a, b)
else:
    result = "Invalid gate"

print("Output:", result)
