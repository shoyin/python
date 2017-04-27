# -*-coding:Utf-8 -*-

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('hello,world')
	elif len(args) ==2:
		print('Hello, %s!' % args[1])
	else:
		print 'xxxxxxxxxx'	

__author__ = 'Michael Liao'

if  __name__=='__main__':
	test()
