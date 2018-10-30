# -*- coding: utf-8 -*-

class test():
	def __init__(self):
		print("__init__")

	def fun(self):
		print("fun")


if __name__ == "__main__":
	ts = test()
	ts.fun()