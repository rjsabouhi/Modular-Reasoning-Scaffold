# Overview

The Modular Reasoning Scaffold (MRS) is a lightweight, extensible framework for building stable, multi-step reasoning systems in Python. It provides a controlled execution environment for recursion, state management, functional operators, and node-based reasoning flows.

## 1. Architecture

MRS consists of five core components:

### 1. State
A persistent key/value store that survives across recursion steps and node executions.

```python
from mrs.state import State

s = State()
s.update("x", 5)
print(s.get("x"))   # -> 5
```

### 2. Operators
Pure functions that transform or evaluate values.

```python
from mrs.operators import add, sub

print(add(3, 4))   # -> 7
print(sub(10, 2))  # -> 8
```

Custom operators can be defined easily:

```python
def double(x):
    return x * 2
```

### 3. Nodes
Nodes wrap a reasoning step.  
Each node receives:
- the global State
- the input to that step

```python
from mrs.nodes import Node

def step_fn(state, x):
    state.update("latest", x)
    return x * 2

n = Node("double_step", step_fn)
```

### 4. Chain
Chains execute a sequence of nodes, passing State + outputs step to step.

```python
from mrs.chain import Chain
from mrs.nodes import Node

def a(state, x): return x + 1
def b(state, x): return x * 3

chain = Chain([Node("a", a), Node("b", b)])
result = chain.run(5)   # ((5 + 1) * 3) = 18
```

### 5. MRS (High-level Interface)
Simple wrapper combining State + execution.

```python
from mrs import MRS

m = MRS()
m.update("score", 10)
print(m.get("score"))   # -> 10
```

## Summary

MRS provides:
- persistent state
- functional operators
- node-based reasoning
- sequential chains
- a simple high-level interface

Together these form a controlled, stable recursive reasoning loop.
