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

# mrs/state.py

class State:
    """
    Persistent intermediate memory for the MRS engine.
    Stores named 'slots' that Nodes can read from and write into.
    """

    def __init__(self):
        self.slots = {}

    def set(self, key, value):
        """
        Store a value in a slot.
        If key does not exist, it is created.
        """
        self.slots[key] = value

    def get(self, key, default=None):
        """
        Retrieve a value.
        If the slot doesn't exist, return default.
        """
        return self.slots.get(key, default)

    def update(self, key, fn):
        """
        Safely update an existing slot value using a function.
        Example: state.update("score", lambda x: x + 1)
        """
        old = self.slots.get(key)
        self.slots[key] = fn(old)

    def exists(self, key):
        """Check if a slot already exists."""
        return key in self.slots

    def snapshot(self):
        """Return a copy of current state (for debugging / drift-check)."""
        return dict(self.slots)
