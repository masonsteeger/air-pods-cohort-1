# Gang of Four Patterns — Reference

*Design Patterns: Elements of Reusable Object-Oriented Software* (Gamma, Helm, Johnson, Vlissides, 1994) catalogs 23 patterns. We use a subset as the vocabulary of object-oriented design. This reference gives intent, structure, and when-to-use for each pattern we apply.

## Contents

- Creational: Factory Method, Builder, Singleton (sparingly)
- Structural: Adapter, Decorator, Facade, Composite
- Behavioral: Strategy, Observer, Command, State
- Relations Between Patterns

---

## Creational Patterns

### Factory Method

**Intent:** Define an interface for creating an object, but let subclasses (or implementors) decide which class to instantiate. Decouples client code from concrete product classes.

**Structure:** A *Creator* (abstract or base class) declares a factory method that returns a *Product* (interface/abstract type). *ConcreteCreators* override the factory method to return *ConcreteProducts*. The creator’s main responsibility is not creation—it usually contains logic that uses the product; the factory method isolates construction.

**When to use:**
- You don’t know upfront the exact types or dependencies of objects (e.g. pluggable implementations, environment-specific types).
- You want to give library/framework users a single extension point for creating components.
- You want to centralize or reuse creation logic (e.g. pooling, caching) in one place.

**Our guidance:** Name the factory method or class so the pattern is obvious (e.g. `OrderFactory`, `createButton()`). Prefer returning an interface/abstract type. If you have many related product families, consider Abstract Factory instead (see Relations below).

---

### Builder

**Intent:** Separate the construction of a complex object from its representation so that the same construction process can create different representations. Construct step-by-step with a fluent API instead of a large constructor or many overloads.

**Structure:** A *Director* (optional) invokes a *Builder* interface to build an object step-by-step. *ConcreteBuilders* implement the steps and provide a method to return the final product. The client uses the builder rather than calling a product constructor with many parameters.

**When to use:**
- Object has many optional parameters or configuration steps.
- You want to avoid telescoping constructors and keep construction readable.
- You need to enforce a valid construction sequence or reuse the same process for different representations.

**Our guidance:** Name the builder class after what it builds (e.g. `OrderBuilder`, `HttpRequestBuilder`). Avoid giant constructors; prefer builders for complex objects.

---

### Singleton (sparingly)

**Intent:** Ensure a class has only one instance and provide a global access point to it.

**Structure:** Class with a private constructor and a static (or otherwise single) instance, often exposed via `getInstance()` or similar. May use lazy initialization or a static holder for thread-safe lazy init.

**When to use:**
- Exactly one instance must coordinate actions across the system (e.g. shared connection manager, app-wide configuration). Use only when the single-instance requirement is real and not just convenience.

**Our guidance:** Use **sparingly**. Singleton introduces global state, complicates testing, and can hide dependencies. Prefer dependency injection of a single instance where possible. If you must use Singleton, document why one instance is required.

---

## Structural Patterns

### Adapter

**Intent:** Convert the interface of a class into another interface clients expect. Lets classes work together that couldn’t otherwise because of incompatible interfaces.

**Structure:** *Adapter* implements the *Target* interface expected by the client and holds a reference to the *Adaptee*. Adapter delegates client calls to the Adaptee, translating as needed. Can be class adapter (inherit Adaptee) or object adapter (compose Adaptee)—prefer object adapter for flexibility.

**When to use:**
- Integrating a third-party or legacy class whose interface doesn’t match what the rest of the system expects.
- Reusing a class in a new context without changing its source.

**Our guidance:** Name the adapter after what it adapts (e.g. `LegacyPaymentAdapter`, `ExternalApiAdapter`). Keep adaptation logic in the adapter; don’t pollute the domain with “if legacy then …” branches.

---

### Decorator

**Intent:** Attach additional responsibilities to an object dynamically. Provide a flexible alternative to subclassing for extending functionality.

**Structure:** *Component* is the common interface. *ConcreteComponent* is the base implementation. *Decorator* implements *Component* and holds a *Component* (wraps it). Concrete decorators add behavior before/after delegating to the wrapped component. Multiple decorators can wrap in sequence.

**When to use:**
- Add responsibilities to individual objects at runtime without affecting other objects.
- Subclassing would lead to an explosion of subclasses (e.g. many combinations of optional behaviors).

**Our guidance:** Prefer composition over inheritance; Decorator is a key way to do that. Name decorators by the responsibility they add (e.g. `LoggingDecorator`, `CachingDecorator`). Ensure the decorator implements the same interface as the component so clients treat them uniformly.

---

### Facade

**Intent:** Provide a unified, higher-level interface to a set of interfaces in a subsystem. Makes the subsystem easier to use.

**Structure:** *Facade* is a single class that delegates to multiple classes in the subsystem. Clients depend only on the facade, not on the subsystem’s internal types.

**When to use:**
- Simplify a complex subsystem (e.g. many classes, steps, or configuration) behind a simple API.
- Decouple client code from the internals of a library or module.

**Our guidance:** Name the facade after the capability or subsystem it represents (e.g. `OrderFulfillmentFacade`, `ReportingFacade`). Don’t turn the facade into a god object—it should remain a thin, coherent entry point.

---

### Composite

**Intent:** Compose objects into tree structures to represent part-whole hierarchies. Lets clients treat individual objects and compositions of objects uniformly.

**Structure:** *Component* (interface) defines the common contract; it may define child management (add/remove/getChildren) for composites. *Leaf* implements *Component* and has no children. *Composite* implements *Component* and holds a collection of *Component* children, delegating operations to children when appropriate.

**When to use:**
- You have a tree structure where some nodes are leaves and others are containers, and you want to treat both the same way (e.g. UI hierarchies, document structures, expressions).

**Our guidance:** Name composite and leaf classes by their domain role (e.g. `MenuItem`, `Menu`; `File`, `Directory`). Keep the component interface minimal so leaves don’t have to implement irrelevant methods (e.g. use default no-op for child management in leaves).

---

## Behavioral Patterns

### Strategy

**Intent:** Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

**Structure:** *Context* holds a reference to a *Strategy* (interface). *ConcreteStrategies* implement the interface. The context delegates the varying behavior to the strategy. Clients configure the context with the desired strategy (often via constructor or setter).

**When to use:**
- Multiple algorithms or behaviors for the same concern (e.g. pricing, validation, serialization) and you want to switch or extend them without changing client code.
- You want to avoid large conditionals or switch statements that select behavior.

**Our guidance:** Name strategies by the behavior they represent (e.g. `PricingStrategy`, `TaxStrategy`). Prefer injecting the strategy into the context (dependency inversion) rather than the context creating it.

---

### Observer

**Intent:** Define a one-to-many dependency between objects so that when one object (subject) changes state, all its dependents (observers) are notified and updated automatically.

**Structure:** *Subject* maintains a list of *Observers* and notifies them when its state changes. *Observer* defines an update interface. Concrete subjects and concrete observers implement the interfaces. Often used with events/callbacks in modern APIs.

**When to use:**
- Multiple parts of the system must react to changes in one object without being tightly coupled to it.
- Model-View separation: the model is the subject; views are observers.

**Our guidance:** Be aware of memory leaks and lifetime (observers that don’t unregister can keep subjects alive). Prefer event/listener naming where it fits the language (e.g. `onOrderPlaced`, `addOrderPlacedListener`). Document the notification contract (when and what is notified).

---

### Command

**Intent:** Encapsulate a request as an object, so you can parameterize clients with different requests, queue or log requests, and support undoable operations.

**Structure:** *Command* interface typically declares `execute()` (and optionally `undo()`). *ConcreteCommand* holds a receiver reference and implements execute (and undo) by calling the receiver. *Invoker* holds a command and calls `execute()`. *Receiver* performs the actual work.

**When to use:**
- Parameterize operations (e.g. menu actions, macro recording).
- Queue requests (e.g. job queues, async processing).
- Support undo/redo or audit logs of operations.

**Our guidance:** Name commands by the operation (e.g. `PlaceOrderCommand`, `CancelSubscriptionCommand`). Keep commands thin—delegate to domain services or receivers; don’t put full business logic inside the command class.

---

### State

**Intent:** Allow an object to alter its behavior when its internal state changes. The object appears to change its class.

**Structure:** *Context* holds a reference to a *State* (interface). *ConcreteState* classes implement the interface and represent distinct states. The context delegates state-dependent behavior to the current state object. State transitions can be done in the context or in the states themselves (by setting the context’s current state).

**When to use:**
- Object behavior depends on state and you have many conditionals or switches on that state.
- You want to model clear state transitions (e.g. order lifecycle: Draft → Submitted → Shipped → Delivered).

**Our guidance:** Name state classes by the state they represent (e.g. `OrderDraftState`, `OrderShippedState`). Prefer moving transition logic into state classes when it keeps the context simpler. Consider whether a simple state enum + strategy is enough before introducing full State pattern.

---

## Relations Between Patterns

- **Factory Method** often evolves into **Abstract Factory** when you have multiple related product families. Start with Factory Method when one creation point is enough.
- **Decorator** and **Composite** share a similar structure (component + recursive composition) but differ in purpose: Decorator adds responsibilities; Composite models part-whole hierarchies.
- **Strategy** and **State** both use composition to vary behavior. Strategy is usually chosen by the client and fixed for the context; State changes at runtime as the context’s state changes.
- **Adapter** changes an interface; **Decorator** adds behavior while keeping the same interface; **Facade** simplifies a subsystem’s interface.

For the full GoF catalog and more detail, see *Design Patterns: Elements of Reusable Object-Oriented Software* (Addison-Wesley, 1994) or refactoring.guru/design-patterns.
