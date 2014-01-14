# -*- coding: UTF-8 -*-

import re

class MyClass:
    field = ''

def fn(cl1):
    cl1.field = 'bbb'

def main():
    cl = MyClass()
    cl.field = 'a'
    print(cl.field)
    fn(cl)
    print(cl.field)

main()