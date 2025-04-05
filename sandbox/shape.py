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
		return f"{self.__class__.__name__}({self.width}, {self.height})"

	def __add__(self, other: Self) -> Self:
		return self.__class__(
			self.width + other.width,
			self.height + other.height,
		)


	@property
	def perimeter(self) -> float:
		return 2 * (self.width + self.height)

	@property
	def area(self) -> float:
		return self.width * self.height


class Square(Rectangle):

	def __init__(self,
		side: float,
	):
		self.width = side
		self.height = side


class DummySquare:

	def __init__(self,
		side: float
	):
		self.width = side
		self.height = side

	def __repr__(self) -> str:
		return f"Square({self.width})"

	def __add__(self, other: Self) -> Self:
		return self.__class__(self.width + other.height)


	@property
	def perimeter(self) -> float:
		return 2 * (self.width + self.height)

	@property
	def area(self) -> float:
		return self.width * self.height
