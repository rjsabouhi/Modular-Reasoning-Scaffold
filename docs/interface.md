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
