---
name: applying-gang-of-four-patterns
description: Applies Gang of Four (GoF) design pattern opinions for object-oriented design. Use when designing classes, refactoring code, discussing OO design, or when the user mentions design patterns, GoF, or pattern names (e.g. Factory, Strategy, Observer).
---

# Gang of Four Design Patterns

We draw heavily from the Gang of Four (GoF) design patterns. These are the vocabulary of object-oriented design.

## Pattern Categories and Common Applications

| Category   | Patterns we use                          |
|-----------|-------------------------------------------|
| Creational | Factory, Builder, Singleton (sparingly)  |
| Structural | Adapter, Decorator, Facade, Composite     |
| Behavioral | Strategy, Observer, Command, State       |

## Guidance

- **Prefer composition over inheritance.**
- **Use patterns to solve actual problems, not speculatively.** Do not introduce patterns "just in case."
- **Name classes and methods to reveal pattern usage** (e.g. `OrderFactory`, `PricingStrategy`).
- **Document pattern usage in code comments when non-obvious.**

## When to Apply

- Choosing between inheritance and composition → prefer composition; consider Decorator, Strategy, or State.
- Encapsulating algorithms or behaviors that vary → Strategy.
- Decoupling producers and consumers of events → Observer.
- Wrapping or adapting external or legacy interfaces → Adapter, Facade.
- Constructing complex objects step-by-step or with many options → Builder; avoid giant constructors.
- Single shared instance (rare) → Singleton, and use sparingly.

## Naming Examples

| Concern | Pattern | Example class or method names |
|---------|---------|-------------------------------|
| Creation | Factory | `OrderFactory`, `createButton()` |
| Construction | Builder | `OrderBuilder`, `HttpRequestBuilder` |
| Behavior that varies | Strategy | `PricingStrategy`, `TaxStrategy` |
| Operation as object | Command | `PlaceOrderCommand`, `CancelSubscriptionCommand` |
| Wrapping interface | Adapter | `LegacyPaymentAdapter`, `ExternalApiAdapter` |
| Adding responsibility | Decorator | `LoggingDecorator`, `CachingDecorator` |

## Relation to Other Principles

- Aligns with **SOLID**: patterns support Single Responsibility, Open/Closed, and Dependency Inversion.
- Domain logic stays in the domain layer; use patterns there and in application/orchestration layers, not as a substitute for clear boundaries.

## Additional Resources

- **[reference.md](reference.md)**: Intent, structure, when-to-use, and relations for each pattern. Read it when implementing or refactoring with a specific pattern, when choosing between similar patterns (e.g. Strategy vs State, Adapter vs Decorator), or when you need the full structure and guidance for a pattern.
