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


if __name__ == "__main__":
	print("Result is:", io_binary_search(0, 64, stdin, stdout))