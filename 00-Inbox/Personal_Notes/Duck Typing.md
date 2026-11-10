---
tags:
  - computer-science
  - python
---

##### Duck Typing

^e7ca82

```
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm imitating a duck!")

def make_it_quack(thing):
    thing.quack()

make_it_quack(Duck())    # Quack!
make_it_quack(Person())  
```

^ec485a

- notice how make_it_quack takes in variable thing and it can be any object that can be passed, Duck or person, it will work as long as the quack function can be called.

### Languages that support duck typing

|Language|Duck typing|
|---|---|
|Python|Yes|
|JavaScript|Yes|
|Ruby|Yes|
|PHP|Yes|
|Perl|Yes|
|Go|Yes, through implicit interfaces|
|TypeScript|Structural typing (similar concept)|

### Languages that generally don't use duck typing

|Language|Approach|
|---|---|
|Java|Nominal typing (interfaces and inheritance)|
|C#|Nominal typing (interfaces and inheritance)|
|C++|Primarily static, nominal typing; templates support structural requirements|
|Rust|Trait-based typing|
|Swift|Protocol-based typing|