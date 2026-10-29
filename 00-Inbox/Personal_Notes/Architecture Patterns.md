
> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=20&selection=3,28,5,7&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.20]]
> > it’s only just starting to take on the kinds of problems that the C# and Java world has been working on for years. 
> 
> - C# and JAVA already have worked on tougher software robustness related problems

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=20&selection=12,40,13,60&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.20]]
> > Zen of Python: “There should be one—and preferably only one—obvious way to do it.”
> 
> #bbxn 

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=21&selection=2,0,3,11&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.21]]
> > In order of notoriety, we know of three tools for managing complexity:
> 
> - TDD
> - DDD
> - EDA

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=35&selection=15,0,26,1&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.35]]
> > The term encapsulation covers two closely related ideas: simplifying behavior and hiding data. In this discussion, we’re using the first sense. We encapsulate behavior by identifying a task that needs to be done in our code and giving that task to a well-defined object or function. We call that object or function an abstraction.
> 
> - encapsulation: simplifying behaviour, if you only want wikipedia articles, instead of using requests library directly use a function which only takes query and uses requests library to give an answer.
> - Abstraction: the function that has been created to simplify behaviour is abstraction. basically hiding the low level details and giving high level tools with fixed input and output

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=37&selection=0,0,1,67&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.37]]
> > Encapsulating behavior by using abstractions is a powerful tool for making code more expressive, more testable, and easier to maintain.
> 
> - reason behind using abstraction and encapsulation

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=37&selection=5,1,22,75&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.37]]
> > n the literature of the object-oriented (OO) world, one of the classic characterizations of this approach is called responsibility-driven design; it uses the words roles and responsibilities rather than tasks. The main point is to think about code in terms of behavior, rather than in terms of data or algorithms
> 
> - thinking of object in terms of roles and responsibilities.

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=37&selection=27,33,28,32&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.37]]
> > n. In Python you can (and we sometimes do) use ABCs, but you can also happily rely on duck typing
> 
> - duck typing: if something walks and talks like a duck(basically behaves like a duck) then python considers it a duck.


##### Duck Typing

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

- notice how make_it_quack takes in variable thing and it can be any object that can be passed, Duck or person, it will work as long as the quack function can be called.


---

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=38&selection=5,61,8,11&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.38]]
> > n a layered architecture, we divide our code into discrete categories or roles, and we introduce rules about which categories of code can call each other.

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=40&selection=23,0,42,7&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.40]]
> > Depends on doesn’t mean imports or calls, necessarily, but rather a more general idea that one module knows about or needs another module.


> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=44&selection=3,0,3,47&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.44]]
> > To do that, we present four key design patterns
> 
> - to do what?
> 	- build persistance ignorant code (DB independent) and create stable APIs around the domain which can be refactored aggressively.
> - 4 patterns:
> 	- repository pattern - persistence independent
> 	- service layer - define use case boundaries
> 	- unit of work - atomic operations
> 	- aggregate - enforce integrity of data

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=49&selection=4,0,16,9&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.49]]
> > In the introduction, we used the term business logic layer to describe the central layer of a three-layered architecture. For the rest of the book, we’re going to use the term domain model instead. 
> 
> Business logic layer = domain model

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=49&selection=31,8,33,24&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.49]]
> > . Most programmers spend their days trying to improve or automate business processes; the domain is the set of activities that those processes support.

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=50&selection=0,0,1,17&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.50]]
> > The domain model is the mental map that business owners have of their businesses.

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=51&selection=13,0,14,12&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.51]]
> > In a nutshell, DDD says that the most important thing about software is that it provides a useful model of a problem
> 
> #kim 

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=63&selection=15,32,16,70&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.63]]
> > sticking rigidly to our principles of encapsulation and careful layering will help us to avoid a ball of mud
> 
> focus on encapsulation and Careful Layering
> 

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=65&selection=21,0,26,9&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.65]]
> > Whenever we have a business concept that has data but no identity, we often choose to represent it using the Value Object pattern. 
> 
> this has been done in our project with TokenUsage Class.



