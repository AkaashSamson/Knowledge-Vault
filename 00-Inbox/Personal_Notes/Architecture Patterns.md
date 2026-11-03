
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
> - [[Duck Typing]]: if something walks and talks like a duck(basically behaves like a duck) then python considers it a duck.

![[Duck Typing#^ec485a]]



---

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=38&selection=5,61,8,11&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.38]]
> > n a layered architecture, we divide our code into discrete categories or roles, and we introduce rules about which categories of code can call each other.

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=39&selection=27,35,31,30&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.39]]
> > DIP’s formal definition: 1. High-level modules should not depend on low-level modules. Both should depend on abstractions. 2. Abstractions should not depend on details. Instead, details should depend on abstractions.


> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=40&selection=23,0,42,7&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.40]]
> > Depends on doesn’t mean imports or calls, necessarily, but rather a more general idea that one module knows about or needs another module.

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=41&selection=19,0,26,14&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.41]]
> > The second part is even more mysterious. “Abstractions should not depend on details” seems clear enough, but “Details should depend on abstractions” is hard to imagine. How can we have an abstraction that doesn’t depend on the details it’s abstracting? By the time we get to Chapter 4, we’ll have a concrete example that should make this all a bit clearer.
> 
> - Waiting for chapter 4
> 

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


> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=65&selection=63,1,85,10&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.65]]
> > rom dataclasses import dataclass from typing import NamedTuple from collections import namedtuple
> 
> - these are 3 different ways of creating and managing value objects in python.

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=67&selection=15,0,21,26&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.67]]
> > That’s the definition of a value object: any object that is identified only by its data and doesn’t have a long-lived identity. What about a batch, though? That is identified by a reference.
> 
> - where as entities can't be identified only by it's data. as the data can change, it needs an immutable attribute which becomes the identifier for that entity. basically an "id" field is required by an entity. 


> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=68&selection=33,0,38,22&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.68]]
> > Entities, unlike values, have identity equality. We can change their values, and they are still recognizably the same thing. Batches, in our example, are entities.

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=68&selection=77,0,81,13&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.68]]
> > Python’s __eq__ magic method 
> 
> - magic method as in special methods which include dunder methods. 

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=69&selection=17,0,32,20&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.69]]
> > For entities, the simplest option is to say that the hash is None, meaning that the object is not hashable and cannot, for example, be used in a set. If for some reason you decide you really do want to use set or dict operations with entities, the hash should be based on the attribute(s), such as .reference, that defines the entity’s unique identity over time. You should also try to somehow make that attribute read-only.
> 
> #kim 

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=70&selection=7,0,13,51&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.70]]
> > Evans discusses the idea of Domain Service operations that don’t have a natural home in an entity or value object. A thing that allocates an order line, given a set of batches, sounds a lot like a function, and we can take advantage of the fact that Python is a multiparadigm language and just make it a function.
> 
> - you don't always need to keep the domain models restricted to objects and classes, sometimes a service as in a service could work better. 
> - here we can use the multiparadigm nature of Python. 
> - as in the given example allocate() is a separate function. 

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=72&selection=50,36,51,29&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.72]]
> > exceptions can be used to express domain concepts too. 
> 
> #kim 

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=73&selection=0,0,0,21&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.73]]
> > DOMAIN MODELING RECAP

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=73&selection=41,0,44,41&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.73]]
> > This is the time to apply your best OO design principles Revisit the SOLID principles and all the other good heuristics like “has a versus is-a,” “prefer composition over inheritance,” and so on.
> 
> - explore these ideas.

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=76&selection=54,0,57,32&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.76]]
> > Domain services are not the same thing as the services from the service layer, although they are often closely related. 

### Chapter 2 

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=79&selection=56,0,57,52&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.79]]
> > We expect to be working in an agile manner, so our priority is to get to a minimum viable product as quickly as possible. 
> 
> - the first step of Agile dev is to get MVP as quickly as possible

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=79&selection=58,30,60,31&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.79]]
> > In a real project, you might dive straight in with some end-to-end tests and start plugging in a web framework, test-driving things outside-in.

> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=82&selection=13,1,18,1&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.82]]
> > nstead, as discussed in the introduction, we’ll think of our model as being on the “inside,” and dependencies flowing inward to it; this is what people sometimes call onion architecture 
> 
> - onion architecture's whole point is to have the domain in the core?

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=83&selection=6,1,8,38&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.83]]
> > s this ports and adapters? Or is it hexagonal architecture? Is that the same as onion architecture? What about the clean architecture? What’s a port, and what’s an adapter? Why do you people have so many words for the same thing?
> 
> so Real..

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=83&selection=10,0,12,64&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.83]]
> > Although some people like to nitpick over the differences, all these are pretty much names for the same thing, and they all boil down to the dependency inversion principle: high-level modules (the domain) should not depend on low-level ones (the infrastructure)
> 
> - so they are all basically focused on DIP


> [!PDF|important] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=84&selection=25,0,33,6&color=important|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.84]]
> > These days, it’s unlikely that your team members are hand-rolling their own SQL queries. Instead, you’re almost certainly using some kind of framework to generate SQL for you based on your model objects. These frameworks are called object-relational mappers (ORMs)
> 
> - ORM: mapping model objects with actual SQL DB

> [!PDF|note] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=85&selection=0,0,6,64&color=note|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.85]]
> > The most important thing an ORM gives us is persistence ignorance: the idea that our fancy domain model doesn’t need to know anything about how data is loaded or persisted. This helps keep our domain clean of direct dependencies on particular database technologies

> [!PDF|yellow] [[Architecture Patterns with Python - Bob Gregory, Harry Percival.pdf#page=85&selection=61,22,63,58&color=yellow|Architecture Patterns with Python - Bob Gregory, Harry Percival, p.85]]
> > Can we really say this model is ignorant of the database? How can it be separate from storage concerns when our model properties are directly coupled to database columns?
> 
> 

