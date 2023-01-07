from math import floor
from sys import stdin, stdout
from typing import TextIO


def io_binary_search(liml: int, limr: int, istream: TextIO, ostream: TextIO, f = None):
	if f is None:
		f = lambda x: x
	while liml < limr-1:
		index = floor((limr+liml)/2)
		guess = f(index)

		ostream.write(str(guess))
		ostream.flush()

		result = istream.read()
		try:
			result = int(result)
		except TypeError:
			print("Unknown integer return, aborting...")
			return
		
		if result:
			limr = index
		else:
			liml = index
	
	return liml



def function_binary_search(x, liml: int, limr: int, f = None):
	if f is None:
		f = lambda x: x
	
	while liml < limr-1:
		index = floor((limr+liml)/2)
		guess = f(index)
		
		if x < guess:
			limr = index
		else:
			liml = index
	

	return liml


def inverse_search(x, f = None):
	if f is None:
		f = lambda x: x
	
	liml = -1
	limr = 1
	
	if f(0) == x:
		return 0
	

	if f(0) < x:
		while f(limr) < x:
			liml = limr
			limr *= 2
	else:
		while f(liml) > x:
			limr = liml
			liml *= 2

	return function_binary_search(x, liml, limr, f)


if __name__ == "__main__":
	print("Result is:", inverse_search(-1000000, lambda x: x**3))