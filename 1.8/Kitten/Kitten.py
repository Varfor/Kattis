tree = {}
ut = []
cat = int(input())
branch = [int(x) for x in input().split()]
def climb(cat, tree):
    if cat in tree:
        ut.append(tree[cat])
        cat = tree[cat]
        climb(cat, tree)
    else:
        return cat
while branch[0] != -1:
    for x in branch[1:]:
        tree[x] = branch[0]
    branch = [int(x) for x in input().split()]
climb(cat, tree)
print(cat, ' '.join([str(x) for x in ut]))
