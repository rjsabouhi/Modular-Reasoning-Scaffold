# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 RJ Sabouhi
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Operators

MRS defines a small, finite set of operators that control the flow of reasoning.  
Each operator transforms the current recursion node \( R_t \) in a predictable, interpretable way.

Think of them as **the instruction set** of the MRS reasoning engine.

---

# 1. `INFER`

Produces the next logical step in the reasoning chain.

**Purpose:**  
Generate new content from the current context and state.

**Formal form:**

\[
O_t = \text{INFER}(R_t)
\]

**Examples:**
- step-by-step deduction  
- combining slot values  
- deriving a new intermediate result  

---

# 2. `UPDATE(slot, value)`

Writes a new value into a state slot.

**Purpose:**  
Maintain persistent intermediate memory.

**Formal form:**

\[
s_{\text{slot}}^{(t+1)} = value
\]

**Examples:**
- storing a partial computation  
- keeping a counter  
- saving extracted entities  

---

# 3. `BRANCH(options…)`

Creates multiple child recursion paths.

**Purpose:**  
Explore alternative solutions, interpretations, or strategies.

**Formal:**

\[
\{R_{t+1}^{(1)}, R_{t+1}^{(2)}, \ldots \}
\]

**Examples:**
- exploring multiple summaries  
- trying alternate decompositions  
- generating alternate proofs  

---

# 4. `SELECT(condition)`

Chooses the best branch based on constraints or fit.

**Purpose:**  
Prune the tree and stabilize the chain.

\[
R_{t+1} = \operatorname*{argmin}_{i}\; D(R_i)
\]

Where \( D \) is a drift or error metric.

---

# 5. `CHECK(constraint)`

Evaluate whether the output matches a constraint.

**Purpose:**  
Keep the reasoning chain aligned with rules.

**Formal:**

\[
CHECK(K_t, O_t) \rightarrow \{pass, fail\}
\]

**Examples:**
- structure must be JSON  
- no contradictions allowed  
- step must follow chain-of-thought structure  

If fail:  
→ trigger **repair loop**.

---

# 6. `REPAIR`

When a step violates constraints, `REPAIR` regenerates or corrects output.

**Purpose:**  
Self-stabilization.

**Behavior:**
- regenerate the step  
- re-check constraints  
- preserve state slots  

This prevents drift across long chains.

---

# 7. `HALT`

Stops the reasoning chain.

**Purpose:**  
Signal final output is complete.

**Formal:**

\[
H(R_t) = \text{True}
\]

**Examples:**
- final answer reached  
- all constraints satisfied  
- no further steps needed  

---

# 8. `EMIT(output)`

Return the final formatted output to the user.

**Purpose:**  
Provide the end result of the reasoning chain.

---

# Operator Summary Table

| Operator | Purpose |
|---------|---------|
| **INFER** | Generate next reasoning step |
| **UPDATE** | Write/update intermediate memory |
| **BRANCH** | Fork reasoning into parallel paths |
| **SELECT** | Choose best branch |
| **CHECK** | Validate constraints |
| **REPAIR** | Fix violations / drift |
| **HALT** | Stop computation |
| **EMIT** | Return final answer |

---

# Notes

- Operators are intentionally minimal.  
- They form a complete set for multi-step reasoning.  
- This is not a programming language — it is a **flow control system for LMs**.  
- The simplicity keeps it robust and generalizable.
