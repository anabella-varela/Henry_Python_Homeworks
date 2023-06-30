import sys


if len(sys.argv) == 4:
    filename, arg1, arg2, arg3 =sys.argv
    print(filename, arg1, arg2, arg3)
else:
    n= len(sys.argv) - 1
    print(f' You introduced {n} arguments. Insert exactly 3 arguments')