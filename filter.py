#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(n):

    n = str(abs(n))
    return n == n[::-1]

output = filter(is_palindrome, range(-100, 10000))
print(list(output))
print(range(-1111, 10000))