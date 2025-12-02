# Math Core

The mathematical core of MRS defines the formal structure behind stable, multi-step recursive reasoning.  
It turns a language model (LM) into a **state machine with constraint-guided transitions**.

---

# 1. Recursion Node (Formal Definition)

A recursion node \( R_t \) at step \( t \) is:

\[
R_t = \left( C_t,\; S_t,\; K_t,\; M_t \right)
\]

Where:
- \( C_t \) — content (task text or transformed instruction)
- \( S_t \) — state slots (persistent intermediate memory)
- \( K_t \) — active constraint set
- \( M_t \) — metadata (optional semantic/structural hints)

A single reasoning step is:

\[
O_t = f_{\text{LM}}(R_t)
\]

---

# 2. State Slot Dynamics

A slot \( s_i \) is updated by:

\[
s_i^{(t+1)} =
\begin{cases}
s_i^{(t)}, & \text{if locked} \\
g_i(O_t), & \text{otherwise}
\end{cases}
\]

Slots allow the model to:
- accumulate intermediate results  
- divide tasks into components  
- maintain counters  
- preserve facts across steps  

This is the “working memory” that small LMs normally lack.

---

# 3. Constraint System

Constraints act as **mathematical guards** on each step.

Typical constraint types:

### Structural
\[
\text{output must be JSON}
\]

### Semantic
\[
\text{must include an explicit reasoning trace}
\]

### Logical
\[
\text{monotonic reasoning: do not contradict past steps}
\]

### Depth
\[
t \le t_{\max}
\]

Constraints are evaluated as:

\[
K_t(O_t) = \text{True or False}
\]

If a constraint fails:

- the step is rejected  
- the node is reissued with context + correction hint  
- the system stays stable  

This is how MRS prevents drift.

---

# 4. Drift Metric

Define drift \( D_t \) as:

\[
D_t = d(O_t,\; C_t)
\]

Where \( d \) is a similarity or structural-distance function.

If:

\[
D_t > \tau
\]

→ MRS triggers a constraint correction step.

This is the **self-stabilizing property** that prevents the model from “wandering.”

---

# 5. Flow Controller (Transition Function)

The transition function:

\[
R_{t+1} = T(R_t,\; O_t)
\]

Where \( T \) performs:

1. Slot updates  
2. Constraint evaluation  
3. Branching decisions  
4. Halting detection  

Branching example:

\[
T = \{R_{t+1}^{(1)},\; R_{t+1}^{(2)},\ldots\}
\]

Halting condition:

\[
H(R_t) = \text{True when task is solved}
\]

---

# 6. Full Reasoning Chain

With everything together:

\[
\{R_0,\; R_1,\; \ldots,\; R_T\}
\]

Forms a **transparent reasoning chain** that can be inspected at any point.

MRS guarantees:

- bounded drift  
- structural consistency  
- traceability  
- deterministic halting behavior (given constraints)  

---

# Summary

The Math Core is what turns MRS into more than a prompt trick.  
It gives a small model:

- memory  
- structure  
- flow control  
- guardrails  
- the ability to reason across multiple steps  

All while remaining simple, finite, and fast.
