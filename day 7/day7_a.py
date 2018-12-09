from collections import defaultdict
from itertools import chain
from string import ascii_uppercase

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

a_items = []
b_items = []
branches = defaultdict(list)
roots = []
old_string = ''
new_string = ''

for line in data:
    word = line.split(' ')
    a, b = word[1], word[7]
    a_items.append(a)
    b_items.append(b)
for i in a_items:
    if i not in b_items:
        branches[i] = []
        if i not in old_string:
            old_string += i
branchchange = True
while True:
    for i in branches.keys():
        for j in range(len(a_items)):
            if i == a_items[j] and b_items[j] not in branches[i]:
                branches[i].append(b_items[j])
    for i in list(chain(*branches.values())):
        if i not in branches:
            branches[i] = []
            break
    else:
        break
print(branches)
print(old_string)
while True:
    for node_value in ascii_uppercase:
        if node_value in old_string and node_value not in new_string:
            new_string += node_value
            a = node_value
            break
    else:
        break
    old_string = old_string.replace(a, '') + ''.join(b for b in (''.join(n for n in branches[a] if n not in branches[(m for m in old_string)])) if b not in old_string and b not in new_string)
    print(old_string, new_string)