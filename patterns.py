# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# n=5 
# for i in range(n,0,-1):
#     for j in range(i+1):
#         print("*", end="")
#     print()

rows=4
for i in list(range(1, rows + 1)) + list(range(rows - 1, 0, -1)):
    print(" " * (rows - i) + "* " * i)
 