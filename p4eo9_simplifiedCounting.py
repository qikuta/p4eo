# Simplified counting with .get()

counts = dict()
names = ['cwen', 'zhen', 'tich', 'han', 'mack']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
