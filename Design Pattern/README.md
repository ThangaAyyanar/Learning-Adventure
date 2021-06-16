# Design Pattern
The challenge is to learn design patterns from [https://refactoring.guru](https://refactoring.guru)

I really loved how it is explained, so i bought the ebook.

Design patterns are a toolkit of tried and tested solutions to common
problems in software design.

Parent book : Design patterns: Elements of Reusable Object-Oriented Software
Other Name  : "The GoF(Gang of Four) book"
Authors     : Erich Gamma, John Vlissides, Ralph Johnson, Richard Helm

## Solid Principles
- Introduced in Agile software Development, Principles, Patterns and Practices.
- Single Responsibility Principle
  - Class must take one responsibility.
- Open/closed Principle
  - Clases should be open for extension but closed for modification.
  - If the class is tested, stable then try to create a sub class and
    implement the behavior in it. It will doesn't break old changes.
- Liskov Substitution Principle
  - When extending the class remember that you should be able to pass
    object of subclass instead of base class
- Interface Segregation Principle
  - Clients shouldn't be forced to depend on methods they don't use.
- Dependency Inversion Principle
  - High level classes shouldn't depend on low level classes. Both should
    depend on abstractions. Abstractions shouldn't depend on details.
    Details should depend on abstractions.
## Creational patterns
- Objection creation mechanisms
- Few patterns
  - [x] Factory Method
      - Handles object creation and encapsulates it in a subclass.
      - This decouples the client code in the superclass from the object
      creation code in the subclass.
      - Seperate object construction code from the code that actually uses the object.
      - Applications
        - Database connections
        - File sytesm
  - [x] Abstract factory
      - Which will create a abstract class. which doesn't know the implementation of the methods
      - 
  - [x] Builder
      - Construct complex objects step by step
      - Able to create different types and representations of an object using the same construction code
      - We can use a helper called Director in which Constructor accepts the builder, expose the method to create most need complex objects.
  - [x] Prototype
    - Object are reference type.so creating a clone is difficult ( Create a new object and pass the exact same parameter but cannot able to populate the value for private values)
    - So we crete a interface with clone method, class will implements this interface.
    - Clone method pass the current object to the constructor (Constructor(Obj) overloaded constructor) where all the variables are copied from one object to another
    - We can create a helper class called register which will hold the recent/most needed objects, which does the clone for you. (Optional)
  - [x] Singleton
    - Only able to create a single object.
    - Used to access a single database from different class.

## Structural Pattern
- Assemble objects and classes into larger structures
- Few patterns
  - [x] Adapter
    - Incompatible interfaces to collaborate with each other.
    - It is also called as **wrapper**
    - Adapter usually wraps just one object.
    - Client access the adapter using Client Interface which is implemented by adaptor class.
  - [x] Bridge
    - Split large class or a set of closely related classes into two
      seperate hierarchies (abstraction and implementation) which can be
      developed independent of each other
      - Create a interace which will be implemented by different class
      - Bridge's abstract class uses the Interface as property to access the object of the class.
  - [x] Composite
    - Compose objects into tree structures and then work with these structures as if they were individual objects
    - tree like object structure.
  - [x] Decorator
    - Adapter changes the interface of an existing object, Decorator enhances an objects.
    - Assign extra behavior to objects at runtime without breaking the code.
    - Use the pattern when it's awkward or not possible to extend an object's behavior using inheritance
    - Supports recursive composition.
  - [x] Facade
    - Defines new interface for existing objects.
    - Facade works with an entire subsystem ofj objects.
    - Simply a wrapper for SDK or framework
  - [x] Flyweight
    - Also known as **cache**
    - The object that only stores the intrinsic state(Immutatable/Constant data) is Flyweight
    - Object has Unique data are sperated into Extrinsic state.
    - When your program must support a huge number of objects which barely fit into available RAM.
  - [x] Proxy
    - Adaptor provide different interface to wrapped object, 
    - Decorator provide enhanced interface(additional functionality to existing methods)
    - Proxy provies same interface
    - Difference between decorator and proxy, proxy has control over life
      cycle of its service object.Decorators is always controlled by
      client
    - Applications:
      - lazy initialization - Virtual proxy
      - logging             - logging proxy
      - access control      - Protection proxy
      - caching             - Caching proxy
      - object is located in network - Remote proxy
      - Smart reference - Clearing objects when not needed(similar to reference count)

## Behavioral Pattern
- Responsibility assignment and communication between objectes
  - [x] Chain of Responsibility
    - Passes request sequentially along a dynamic chain of potential receivers until one of them handles it.
    - Every handler(basic unit in Chain of Responsibility) checks and decide to execute or pass to other.
  - [x] Command
    - Client Implementation
      - Create recievers.
      - Create commands and associate them with recievers if needed.
      - Create senders and associate them with specific commands.
    - Unidirectional connections between senders and receivers.
    - Turns request into stand alone object that contain all the information about the request.
    - When you want to parametrize objects with operations.
  - [x] Iterator
    - Provide a abstraction to walk through the complex datastructure
    - It is used in loops
    - Client Implementation
      - Create a iterator interface that has getNext, hasNext, currentPos....
      - Collection Interface which creates the iterator.
      - Client access the collection interface to access the iterator.
  - [x] Mediator
    - Eliminate direct connection between senders and receivers, forcing
      them to communicate indirectly via a mediator object
    - Example:
      Airplanes communicate with Air Trafic Controlller(Mediator) then they procide for landing
  - [x] Memento
    - Also known as **Snapshot**
    - save and restore the previous state of an object with revealing the details of its implementation.
  - [x] Observer
    - Let recievers dynamically subscribe to and unsubscribe from receiving requests.
    - When changes to the state of one object may require changing the
      other objects, and the actual set of objects is unknown beforehand
      or changes dynamically.
    - Some object must observe others, but only for a limited time or in specific cases.
  - [x] State
    - Object alter its behavior when its internal state changes.
    - Each state is written in seperate class implementing interface state
    - Main class act as context, which start the initial state
    - Concreate state class perform operation based on the context object
  - [x] Strategy
    - People confuse it with Bridge
    - State and Strategy may look similar but State pattern aware of each
      other whereas Strategies almost never know about each other.
    - Main class act as context, Client decides which algorithm to use.
    - Each algorithm is implemented in Startegies, each startegy
      implements common startegy interface known to context
  - [x] Template Method
    - Defines Skeleton of an algorithm in the superclass but lets
      subclasses override specific steps of the algorithm without changing
      its structure.
    - Template method in super class defines in which order the function should be executed.
    - Subclass override mehtods other than template method to their liking.
  - [x] Visitor
    - Lets us seperate algorithms from the objects on which they operate.
    - When you need to perform an operation on all elements of a complex
      object structure
    - Clean up the businness logic of auxiliary behaviors.
