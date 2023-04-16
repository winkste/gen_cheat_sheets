# Markdown Mermaid Cheat Sheet
This cheat sheet gives an overview on the most popular diagrams in markdown - mermaid. An overview can be found at: [mermaid](https://mermaid.js.org/intro/)

## Table of Content
- [Markdown Mermaid Cheat Sheet](#markdown-mermaid-cheat-sheet)
  - [Table of Content](#table-of-content)
  - [Flow chart](#flow-chart)
  - [Sequence Diagram](#sequence-diagram)
  - [Class Diagram](#class-diagram)
  - [State diagram](#state-diagram)

## Flow chart
> Find more details on:
> [Mermaid FlowCharts](https://mermaid.js.org/syntax/flowchart.html)
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

## Sequence Diagram
> Find more details on:
> [Mermaid Sequence Diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html)
```mermaid
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
```

## Class Diagram
>Find more details on:
[Mermaid Class Diagrams](https://mermaid.js.org/syntax/classDiagram.html)
```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
Class08 <--> C2: Cool label
```

## State diagram
>Find more details on:
>[Mermaid State Diagram](https://mermaid.js.org/syntax/stateDiagram.html)
```mermaid
---
title: Simple sample
---
stateDiagram-v2
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]

```