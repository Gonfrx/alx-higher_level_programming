#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    iteration = len(sys.argv) - 1
    if iteration == 0:
        print("0 arguments.")
    elif iteration == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(iteration))
    for i in range(iteration):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
