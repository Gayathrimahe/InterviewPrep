items = (10, 'one', 4, 'eleven', 5, 8, 'zero')
a, b, c, d, e, f, g = items
print(d)
new_items = (12, 'ones', 41, 'elves', 15, 80, 'zeros')
a, *b, g = new_items
print(b)
