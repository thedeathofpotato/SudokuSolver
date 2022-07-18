from typing import Type
from __future__ import annotations

class Cell:
    def __init__(self, value=0) -> None:
        if(value == 0):
            self._possible=[value]
            self.defined=True
            self.preDefined=True
        else:
            self._possible = [1,2,3,4,5,6,7,8,9]
            self.defined = False
            self.preDefined = False
        self._connected = []

    def setConnected(self, other:Type[Cell]):
        self._connected.append(other)

    def removePosibility(self, value:int):
        self._possible.remove(value)
        if(len(self._possible)==1):
            self.defined=True
            for c in self._connected:
                c.removePosibility(self._possible[0])
        if(len(self._possible)==0):
            raise ImmposibleStateException()

    def toString(self) -> str:
        if(not self.defined):
            return " "
        else:
            return self._possible[0]

class ImmposibleStateException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)