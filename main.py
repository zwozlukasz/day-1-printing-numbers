# How to printing numbers:
value_1 = 3442
value_2 = 24

# 1
print(f"Show values: value_1 = {value_1:6}, value_2 = {value_2:6}")

# 2
print("Show values: value_1 = %6d, value_2 = %6d" % (value_1, value_2))

# 3
print("Show values: value_1 = {0:6}, value_2 = {1:6}".format(value_1, value_2))

# float values
value_1 = 453.524434434
value_2 = 2.423424242
value_3 = 6.32

# 1
print(
    f"Resutls: value_1: {value_1:.3}, value_2: {value_2:.5}, value_3: {value_3:.3}"
)

# 2
print("results: %.3f, %.3f, %.3f" % (value_1, value_2, value_3))

# 3
print("results: value_1: {:.3} value_2: {:.3} value_3: {:.3}".format(
    value_1, value_2, value_3))

# format
print()

border = 43
imie_1 = "Tom"
nazwisko_1 = "Kowalski"
wyplata_1 = 233.343
imie_2 = "Mark"
nazwisko_2 = "Nowak"
wyplata_2 = 533.436
print("=" * border)
print("|{:16}|{:16}|{:7}|".format("imie", "nazwisko", "wyplata"))
print("=" * border)
print(f"|{imie_1:16}|{nazwisko_1:16}|{wyplata_1:4.8}|")
print("-" * border)
print(f"|{imie_2:16}|{nazwisko_2:16}|{wyplata_2:4.8}|")
print("=" * border)

print("Dzialanie znacznika r: %r, %8s, %4d, %.4f" %
      ("ciag znak", "okresla dlugosc ciagu znakow", 123456.77, 12345.4324))

print("Dzialanie znacznika x - wynik 16: %02x, %02x" % (17, 123))
print("Dzialanie znacznika o - wynik 8: %02o, %02o" % (17, 123))

"""Wnioski:
napis oznaczamy: %s (s – string)
liczbę całkowitą oznaczamy: %d (d – digit)
liczbę zmiennoprzecinkową: %f (f – float)
dowolną wartość: %r (r – raw)"""
