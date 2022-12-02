"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730555056"


class Simpy:
    """Simping for Numpy :)."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, floats: list[float]):
        """Storing a list of floats to attribute."""
        self.values = floats
    
    def __repr__(self) -> str:
        """Python representation of string object."""
        return f"Simpy({self.values})"
    
    def fill(self, rep: float, times: int) -> None:
        """Fill values attribute 'times' number of times."""
        difference: int = times - len(self.values)
        if times > len(self.values):
            for i in range(len(self.values)):
                self.values[i] = rep
            for _ in range(difference):
                self.values.append(rep)
        else:
            for i in range(times):
                self.values[i] = rep
            for _ in range(abs(difference)):
                self.values.pop(-1)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Basically the range function for Simpy."""
        assert step != 0.0
        difference: float = (stop - start) / step
        for i in range(int(difference)):
            self.values.append(start + i * step)
    
    def sum(self) -> float:
        """Sum of all values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds two Simpies together or adds a Simpy and a float."""
        Sum: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in range(len(self.values)):
                Sum.values.append(self.values[item] + rhs)
            return Sum

        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                Sum.values.append(self.values[item] + rhs.values[item])
            return Sum
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Simpy to the power of rhs."""
        Pow: Simpy = Simpy([])
        if type(rhs) == float:
            for item in range(len(self.values)):
                Pow.values.append(self.values[item] ** rhs)
            return Pow
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                Pow.values.append(self.values[item] ** rhs.values[item])
            return Pow
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks and returns a list[bool] if identical to rhs."""
        c: list[bool] = []
        if type(rhs) == float:
            for item in self.values:
                c.append(item == rhs)
            return c
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                c.append(self.values[item] == rhs.values[item])
            return c
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks and returns a list[bool] if greater than rhs."""
        c: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                c.append(item > rhs)
            return c
            
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                c.append(self.values[item] > rhs.values[item])
            return c
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """If rhs is an int, will return the value at subscription notation. If rhs is list[bool], will return a new Simpy object from self.values that corresponds with the boolean value stored at rhs if that value is True."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            c: Simpy = Simpy([])
            i: int = -1
            for each in rhs:
                i += 1
                if each:
                    c.values.append(self.values[i])
            return c
            