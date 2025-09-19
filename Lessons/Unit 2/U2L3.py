a = "Hello"
b = "Hello"
print("location of a =", id(a))
print("location of b =", id(b))
print(a is b)
a = a.replace("e","z")
print(a)
print(b)
print(a is b)
print("location of a =", id(a))
print("location of b =", id(b))

# I predict this code will print the unicode for a and b, then print true.
# It will then replace the "e" in a with z, compare a and b, then print the unicode.

A = ["zebra", "kangaroo", "cat", "human", "aardvark"]
n = len(A)
for i in range(n):
    for j in range(i + 1, n):
        if A[i] > A[j]:
          A[i], A[j] = A[j], A[i]

print(A)
