from __future__ import annotations


def divide(a: int | float, b: int | float) -> float:
	try:
		return a / b

	except ZeroDivisionError:
		return float("inf") if a >= 0 else float("-inf")
