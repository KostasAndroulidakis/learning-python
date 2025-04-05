from __future__ import annotations


import math


# Lets start with a rectangle where we need to floats for the width and the height:

def perimeterReactangle(rectangle: tuple[float, float]) -> float:
	width, height = rectangle

	return 2 * (width + height)

def areaReactangle(rectangle: tuple[float, float]) -> float:
	width, height = rectangle

	return width * height


# For the square we need to know only one side so we keep a single float:

def perimeterSquare(square: float) -> float:
	return 4 * square

def areaSquare(square: float) -> float:
	return square ** 2


# For the rombus we need to know the side and the angle so its again two floats but different floats:

def perimeterRombus(rombus: tuple[float, float]) -> float:
	side, angle = rombus

	return 4 * side

def areaRombus(rombus: tuple[float, float]) -> float:
	side, angle = rombus

	return side * side * math.cos(angle)




