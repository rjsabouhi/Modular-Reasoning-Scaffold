# Interface

The MRS interface defines how a language model interacts with recursion nodes, slots, constraints, and the flow engine.  
It is intentionally minimal, so even small models can use it without overhead.

---

# Core Interface Objects

## 1. `NodeContext`
Holds all information a single reasoning step needs.

Fields:
- `content`: current text or instruction
- `slots`: dictionary of state slot values
- `step`: current step index
- `constraints`: active constraint set
- `metadata`: free-form metadata for advanced use

---

## 2. `StateSlot`
A small persistent memory cell.

Properties:
- `name`
- `value`
- `locked` (prevents accidental overwrite)
- `history` (optional tracking of past values)

---

## 3. `ConstraintSet`
Defines structural and semantic rules.

Examples:
- output must be JSON  
- output must contain “reasoning” and “answer” sections  
- recursion depth ≤ N  
- forbid speculation  
- enforce monotonic reasoning  

---

## 4. `FlowController`
Determines step transitions.

Responsibilities:
- `next_step()`
- `halt()`
- `branch()`
- `merge()`

---

# Execution Loop

The full reasoning cycle for one task:

```python
while not controller.halted:
    node = create_node(context)
    output = model(node)
    context = update_context(node, output)
    controller.next_step(context)
