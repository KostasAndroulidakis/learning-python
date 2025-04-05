from __future__ import annotations


import math


class Rectangle:

	def __init__(self: Rectangle,
		width: float,
		height: float,
	):
		self.width = width
		self.height = height

		self.angle = math.pi / 2

	def __repr__(self) -> str:
		return f"Rectangle({self.width}, {self.height})"

	def __add__(self: Rectangle, other: Rectangle) -> Rectangle:
		return Rectangle(
			self.width + other.width,
			self.height + other.height,
		)


	def perimeter(self: Rectangle) -> float:
		return 2 * (self.width + self.height)

	def area(self: Rectangle) -> float:
		return self.width * self.height

