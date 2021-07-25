### So you know python ?

#### Variable and Attribute scoping
Python used a order to find the variable. This order also known as `LEGB`.

- L - Local
- E - Encapsuled function
- G - Global
- B - Builtins

so python will search a variable first in local scope and if it does not found it will search in enacapsuled function . 

for example

```python
name = "amit"

def main() -> None:
    name = "raghav"
    print(name)
```
output will be -

```bash
raghav
```

