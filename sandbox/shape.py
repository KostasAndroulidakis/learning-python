from __future__ import annotations


import math
from typing import Self


class Parallelogram:

	def __init__(self,
		width: float,
		height: float,
		angle: float,
	):
		self.width = width
		self.height = height
		self.angle = angle

	def __repr__(self) -> str:
		return self.__class__.__name__ + str(vars(self))

	def __add__(self, other: Self) -> Self:
		return self.__class__(
			self.width + other.width,
			self.height + other.height,
			(self.angle + other.angle) / 2,
		)


	@property
	def perimeter(self) -> float:
		return 2 * (self.width + self.height)

	@property
	def area(self) -> float:
		return self.width * self.height * math.cos(self.angle)


class Rectangle(Parallelogram):

	def __init__(self,
		width: float,
		height: float,
	):
		super().__init__(
			width,
			height,
			math.pi / 2,
		)


	@property
	def area(self) -> float:
		return self.width * self.height


class Rombus(Parallelogram):

	def __init__(self,
		side: float,
		angle: float,
	):
		super().__init__(
			side,
			side,
			angle,
		)


class Square(Rectangle):

	def __init__(self,
		side: float,
	):
		super().__init__(
			side,
			side,
		)
