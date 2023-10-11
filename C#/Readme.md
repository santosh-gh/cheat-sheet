# What are features of C#?

    Strong type checking.

    Automatic memory management.

    Object-oriented programming.

    Interoperability with other languages.

    Component-based architecture.

    Delegate type for events and callbacks.

# What is a delegate in C#?

    A delegate in C# is a type that represents a method with a specific signature. 

    It acts as a reference to a method and can be passed as a parameter to another method.

    Delegates are used to implement events and callbacks in C# and provide a way to pass methods as arguments to other methods, allowing for more dynamic and flexible code. 

# What is Garbage Collection in C#?

    Garbage Collection is the process by which the .NET runtime automatically frees up this memory when it is no longer in use.

    The Garbage Collector periodically scans the heap to determine which objects are no longer being used by the application and can be safely removed. 

# What are the types of classes in C#?

    There are several types of classes in C#. Let us look at some of them:

    Regular Class: These are the most common type of classes in C#. They can contain fields, properties, methods, events, and other members. You can use regular classes to define objects that represent real-world entities or abstract concepts.
    
    Partial class: These are classes that are split into multiple files. Each file contains a portion of the class definition, and the compiler combines them into a single class.
    
    Abstract Class: These are classes that cannot be instantiated directly. Instead, they are designed to be inherited by other classes.
    
    Sealed Class: These are classes that cannot be inherited by other classes. Sealed classes are often used to prevent unintended modification of a class, or to improve performance by allowing the compiler to optimize the code.
    
    Nested Class: These are classes that are defined within another class. Nested classes can be either static or non-static, and can be used to encapsulate functionality that is only relevant to the containing class.
    
    Static Class: These are classes that contain only static members, such as fields, methods, and properties.

    What is the difference between an Array and ArrayList in C#?

# Array Vs ArrayList

    The type of element in an array must be specified at the time of creation of the array i.e., they are statically typed.	
    ArrayLists are dynamically typed which means that we can store elements of any type.

    Arrays have a fixed size and cannot be changed once the array is created.	    
    ArrayLists can resize themselves and are more flexible than arrays.

    Arrays are generally faster because if fixed size.	
    ArrayLists are slower as they require more memory and performance overhead.

    Arrays are created using [] within which the size is specified.	
    ArrayLists can be created using ArrayList class and the initial size can be specified.

# struct Vs class

    Structs are value types, meaning that when you assign a struct to a variable, you create a copy of the struct in memory.	
    Classes are reference types, meaning that when you assign a class to a variable, you create a reference to an object stored elsewhere in memory.

    Structs are stored on the stack.	
    Classes are stored on the heap.

    Structs cannot have destructors.	
    Classes can have destructors.

    Struct does not support the protected modifier.	
    The class supports protected modifiers.

# What is a lambda expression in C#?

    A lambda expression in C# is a shorthand syntax for creating anonymous functions. 
    It allows you to define a method in place without declaring a separate delegate or named method.
    A lambda expression can be assigned to a delegate type or passed as a parameter to a method that expects a delegate. 

# abstract class Vs an interface

    An abstract class in C# can contain both abstract and concrete methods and properties, and its derived classes can override its abstract methods to provide their own implementation.	
    An interface in C# only defines a set of methods and properties that a class must implement without providing any implementation.

    It contains different types of access modifiers.	
    It contains only public access modifiers.

    The performance is fast.	
    The performance is slow.

    Abstract class can be implemented using the “:” keyword.	
    Interface can be implemented using “:” and “,” keywords.

    The “abstract” keyword is used to declare the abstract class.	
    The “interface” keyword is used to declare the interface.

# dispose() Vs finalize()

    The Dispose method in C# is an explicit method that the user can call to release resources held by an object. 
    
    The Finalize method is an implicit method that the garbage collector automatically calls to release resources when an object is no longer needed. 
    
    The Dispose method is preferred over the Finalize method as it allows for more immediate and efficient resource management.

# How would you force Garbage Collection?
    In C#, you can use the GC.Collect() method to manually force Garbage Collection. The GC.Collect() method triggers the Garbage Collection process immediately rather than waiting for the .NET runtime to perform it automatically.

# Non-Generic Collection Types.

    Each non-generic collection can be used to store different types as they are not strongly typed.

    ArrayList: Similar to an array, does not have a specific size, and can store any number of elements

    HashTable: Stores key-value pairs for each item, does not have a specific size, can store any number of elements, key objects must be immutable

    SortedList: Combination of ArrayList and HashTable, data stored as key-value pairs, items sorted by keys, items accessed by key or index, does not have a specific size, can store any number of elements

    Stack: Simple Last-In-First-Out (LIFO) structure, does not have a specific size, can store any number of elements, elements are pushed onto the stack and popped off from the stack

    Queue: First-In-First-Out (FIFO) structure, does not have a specific size, can store any number of elements, elements are enqueued into the queue and dequeued from the queue

# Why Are Async and Await used in C#?
    If we have a program that requires methods to be run independently of the primary process, we need to use asynchronous programming. This allows us to run processes and, when needed, make them wait without blocking the rest of the program.

    To do this, we use the Async keyword to create an asynchronous method and Await to run it without blocking our program.
