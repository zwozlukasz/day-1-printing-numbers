# How to printing numbers:
value_1 = 3442
value_2 = 24

# 1
print(f"Show values: value_1 = {value_1:6}, value_2 = {value_2:6}")

# 2
print("Show values: value_1 = %6d, value_2 = %6d"%(value_1, value_2))

# 3
print("Show values: value_1 = {0:6}, value_2 = {1:6}".format(value_1, value_2))

# float values
value_1 = 453.524434434
value_2 = 2.423424242
value_3 = 6.32

# 1
print(f"Resutls: value_1: {value_1:4.3}, value_2: {value_2:4.5}, value_3: {value_3:4.3}")

# 2
print("results: %.3f, %.3f, %.3f"%(value_1, value_2, value_3))

# 3
print("results: value_1: {:.3} value_2: {:.3} value_3: {:.3}".format(value_1, value_2, value_3))
