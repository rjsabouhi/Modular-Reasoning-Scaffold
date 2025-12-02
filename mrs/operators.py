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

# mrs/operators.py

class Op:
    """
    Base operator class.
    Every reasoning action implements `.run(state)`.
    """

    def run(self, state):
        raise NotImplementedError("Operator must define run()")


class Sequence(Op):
    """
    Run a list of operators in order.
    Equivalent of a reasoning chain.
    """

    def __init__(self, *ops):
        self.ops = ops

    def run(self, state):
        for op in self.ops:
            result = op.run(state)
            # If any operator returns HALT, stop execution.
            if result == "__HALT__":
                return "__HALT__"
        return None


class Conditional(Op):
    """
    Run an operator only if the condition predicate is True.
    """

    def __init__(self, predicate, op):
        self.predicate = predicate
        self.op = op

    def run(self, state):
        if self.predicate(state):
            return self.op.run(state)
        return None


class Halt(Op):
    """
    Immediately stop all further execution in a Sequence.
    """

    def run(self, state):
        return "__HALT__"
