
# Swapping values of two variables without using a temporary variable

a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)
