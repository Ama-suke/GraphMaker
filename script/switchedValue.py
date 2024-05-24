# switchedValue.py
# Author: hoshina
# Created: 2024/04/14
# brief: 有効かどうかを同時に持つ値

class SwitchedValue:
    def __init__(self, value):
        self.value = value
        self.enabled = False
