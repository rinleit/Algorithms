#!/usr/bin/env python3
import os


def runtests():
    os.system("python3 -m unittest discover -s 'MarsRoverTests' -p '*Test.py'")


if __name__ == '__main__':
    runtests()