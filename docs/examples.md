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

# Examples

This page shows how to use the Modular Reasoning Scaffold (MRS) in realistic scenarios.  
Each example illustrates core operators and how the engine manages structure, state, and stability.

---

# 1. Basic Reasoning Example  
Simple use of `INFER` + `UPDATE` to produce a multi-step chain.

### Input
```
What is the average of 12 and 20?
```

### MRS Reasoning (conceptual)
```
STEP 1:
INFER → Identify task.
"Compute the average of two numbers."

STEP 2:
INFER → Extract numbers.
12 and 20

STEP 3:
UPDATE(slot="sum", value=32)

STEP 4:
UPDATE(slot="average", value=16)

STEP 5:
HALT
EMIT(16)
```

### Output
```
16
```

---

# 2. Branching Example  
Demonstrates `BRANCH` + `SELECT`.

### Input
```
Summarize this in one sentence:
"The cat sat on the mat because it was warm."
```

### MRS Reasoning
```
STEP 1:
BRANCH(
  path1 = "Cat sat on mat to stay warm.",
  path2 = "Warmth caused the cat to sit on the mat.",
  path3 = "Cat found warm mat and sat on it."
)

STEP 2:
SELECT(best semantic compression)

→ returns path1
```

### Output
```
"The cat sat on the mat to stay warm."
```

---

# 3. Constraint + Repair Loop Example  
Demonstrates `CHECK` + `REPAIR`.

### Input
```
Return a JSON object with fields:
"name", "age", "city"
```

### MRS Reasoning
```
STEP 1:
INFER → attempt to create JSON
{"name": "Bob", "city": "LA"}     ✗ missing "age"

STEP 2:
CHECK(JSON schema)
→ fail

STEP 3:
REPAIR → regenerate object
{"name": "Bob", "age": 32, "city": "LA"}   ✓

STEP 4:
HALT
EMIT
```

### Output
```
{"name": "Bob", "age": 32, "city": "LA"}
```

---

# Notes

- These examples are conceptual: MRS does not force a specific syntax.  
- They show the internal *structure* of how reasoning unfolds.  
- Real implementations will embed this logic inside prompt templates, evaluators, or agent frameworks.
