"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt


__author__ = "730555056"  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Calculates the distance between two points."""
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Cell:
    """An individual subject in the simulation."""

    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Updates the model every second."""
        self.location = self.direction.add(self.location)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()

    def contract_disease(self) -> None:
        """Sickness value is assigned to INFECTED constant when cells contract disease."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Returns true if cell is vulnerable, False otherwise."""
        return self.sickness == constants.VULNERABLE

    def is_infected(self) -> bool:
        """Returns true if cell is infected."""
        return self.sickness >= constants.INFECTED

    def is_immune(self) -> bool:
        """Returns true if cell is immune."""
        return self.sickness == constants.IMMUNE

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_immune():
            return "black"
        return "red"

    def contact_with(self, other: Cell) -> None:
        """If one of the cells that is infected makes contact with another cell, the other cell is infected."""
        if other.is_immune() is False and self.is_immune() is False:
            if other.is_infected() or self.is_infected():
                if other.is_vulnerable():
                    other.contract_disease()
                else:
                    self.contract_disease()

    def immunize(self) -> None:
        """Assigns the immune value to a cell."""
        self.sickness = constants.IMMUNE


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infect: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infect <= 0 or infect >= cells:
            raise ValueError("The number of cells you start with must be greater than 0.")
        if infect + immune > cells:
            raise ValueError("The number of infected and immune cells should not exceed the amount of total cells.")
        if immune < 0:
            raise ValueError("The number of immune cells must be greater than zero.")
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(10)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        i: int = 0 
        while i < infect:
            self.population[i].contract_disease()
            i += 1
        j: int = i + 1
        for _ in range(immune):
            self.population[j].immunize()
            j += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        # Do for min and max for x and y
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
        
    def check_contacts(self) -> None:
        """Checks if any infected cell makes contact with another cell."""
        i: int = 0
        for each_cell in self.population:
            for element in range(i + 1, len(self.population)):
                if each_cell.location.distance(self.population[element].location) < constants.CELL_RADIUS:
                    each_cell.contact_with(self.population[element])
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_immune() is False:
                if cell.is_vulnerable() is False:
                    return False
        return True