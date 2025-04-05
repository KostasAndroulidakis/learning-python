from __future__ import annotations


from typing import Self


class Rectangle:

	def __init__(self,
		width: float,
		height: float,
	):
		self.width = width
		self.height = height

	def __repr__(self) -> str:
		return f"Rectangle({self.width}, {self.height})"

	def __add__(self, other: Self) -> Self:
		return self.__class__(
			self.width + other.width,
			self.height + other.height,
		)


	@property
	def perimeter(self: Rectangle) -> float:
		return 2 * (self.width + self.height)

	@property
	def area(self: Rectangle) -> float:
		return self.width * self.height
