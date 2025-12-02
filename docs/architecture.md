# Architecture

The Modular Reasoning Scaffold (MRS) provides a stable, multi-step recursive reasoning framework for small and mid-sized language models. The core architecture has five major components:

---

## 1. Recursion Nodes
Each reasoning step runs inside a “node” that carries:
- local state
- the current prompt context
- constraint settings
- slot references

Nodes chain together into a stable reasoning graph.

---

## 2. State Slots (Persistent Memory)
Slots are small, persistent containers that survive across recursion steps.

They allow:
- intermediate result storage  
- condition propagation  
- branch comparison  
- recursive loop awareness  

---

## 3. Constraint Layers
Constraints define:
- what a step is allowed to output  
- what formats are legal  
- what conditions must remain true  

They prevent drift, hallucination, and runaway recursion.

---

## 4. Flow Engine (Topology)
Determines:
- step → step transitions  
- branching  
- merging  
- halting conditions  

Equivalent to a lightweight computational graph optimized for reasoning.

---

## 5. Drift Monitor
Tracks:
- semantic deviation  
- logical inconsistency  
- recursion instability  

If drift exceeds the threshold → halting or correction is triggered.

---

# Summary Diagram (High-Level)

```mermaid
flowchart TD
    A[Input] --> B[Recursion Node]
    B --> C[State Slots]
    C --> D[Constraint Layer]
    D --> E[Flow Engine]
    E --> F[Next Node]ooo
