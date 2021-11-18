# fuck its worked
res = []

print(inp.split("/"))

for c in inp.split("/"):
    if c != "." and c != "":
        if c == ".." and len(inp) != 0:
            res.pop(-1)
        else:
            res.append(c)
print("/".join(res))
