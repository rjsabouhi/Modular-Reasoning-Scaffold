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

# mrs/nodes.py

from .core import MRSState
from .operators import Op, Sequence, Conditional, Halt


class Node(Op):
    """
    Base Node.
    A Node is an operator with:
    - a name (useful for debugging)
    - an execution function that receives and mutates the state
    """

    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def run(self, state: MRSState):
        try:
            return self.fn(state)
        except Exception as e:
            raise RuntimeError(f"Node '{self.name}' failed: {e}")


class ComputationNode(Node):
    """
    Node used for stable, deterministic operations.
    Example: numeric transforms, parsing, cleaning, formatting.
    """

    def __init__(self, name, fn):
        super().__init__(name, fn)


class DecisionNode(Node):
    """
    Node that decides branching or gating behavior.
    Its fn must return a boolean or truthy/falsey value.
    """

    def __init__(self, name, fn):
        super().__init__(name, fn)

    def run(self, state: MRSState):
        result = self.fn(state)
        if not isinstance(result, bool):
            raise ValueError(
                f"DecisionNode '{self.name}' must return a boolean, got: {type(result)}"
            )
        return result


class ReasoningChain:
    """
    A chain is a compiled, ordered list of nodes.
    Execute with .run(state).
    """

    def __init__(self, *nodes: Node):
        self.sequence = Sequence(*nodes)

    def run(self, state: MRSState):
        return self.sequence.run(state)
