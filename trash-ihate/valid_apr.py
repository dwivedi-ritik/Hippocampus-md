text = "{[()}"

stack = []

temp = {")": "(", "]": "[", "}": "{"}
for el in text:
    if len(stack) != 0 and temp.get(el) == stack[-1]:
        stack.pop(-1)
    else:
        stack.append(el)
    print(stack)


if len(stack) > 0:
    print(False)
else:
    print(True)
