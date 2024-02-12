#create sets:
s = set()

# add elements to the set nenhum elemento aparece mais de uma vez no set.
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(8)
s.add(7)
s.add(1)

print(s)

s.remove(1)

print(s)

print(f"The set has {len(s)} elements.")