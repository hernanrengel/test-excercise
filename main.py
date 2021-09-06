import math

# get the result of the operation
def getSquare(n):
    calc = (3 + math.sqrt(5))**n
    # format the entire result
    result = "{:.5f}".format(calc)
    # return a string splitted by "."
    # and getting the last 3 characters of the result
    return str(result).split(".")[0][-3:]

for n in range(1, 31):
    print(" with n={} result {}".format(n, getSquare(n).zfill(3)))
