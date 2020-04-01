# /usr/bin/env python3

import argparse

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script returns the Fibonacci number at a specified position in the Fibonacci sequence")

# add positional argument for teh input position in the Fib sequence
parser.add_argument("num", help="The Fibonacci number you wish to caluculate", type=int)
parser.add_argument("name", help="Name of the user")

# add some optional arguments
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="print verbose output")
group.add_argument("-s", "--simple", action="store_true", help="print simple output (default)")

# parse the arguments
args = parser.parse_args()


# calculate the Fibonacci number
a,b = 0,1

for i in range(args.num):
	a,b = b, a+b

# print the output as requested by the user
if(args.verbose):
	# print the verbose output
	print("hello", args.name, "for position", str(args.num), "the Fibonacci number is", a)
else:
	# print the simple output
	print(str(args.num), a)