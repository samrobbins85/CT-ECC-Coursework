import numpy as np
import math

def hammingGeneratorMatrix(r):
    n = 2 ** r - 1

    # construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2 ** (r - i - 1))
    for j in range(1, r):
        for k in range(2 ** j + 1, 2 ** (j + 1)):
            pi.append(k)

    # construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i + 1))

    # construct H'
    H = []
    for i in range(r, n):
        H.append(decimalToVector(pi[i], r))

    # construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n - r):
        GG.append(decimalToVector(2 ** (n - r - i - 1), n - r))

    # apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    # transpose
    G = [list(i) for i in zip(*G)]

    return G


# function decimalToVector
# input: numbers n and r (0 <= n<2**r)
# output: a string v of r bits representing n
def decimalToVector(n, r):
    v = []
    for s in range(r):
        v.insert(0, n % 2)
        n //= 2
    return v


# -------------------------------------------------------------------------------------------------------------------- #


def checkvalid(a):
    return all(elem in [0, 1] for elem in a) and len(a)!=0


def message(a):
    if not checkvalid(a):
        return []
    l = len(a)
    r = 2
    while (2 ** r - 2 * r - 1) < l:
        r += 1
    k = 2 ** r - r - 1
    length = list(bin(l)[2:])
    length = [int(x) for x in length]
    length = [0] * (r - len(length)) + length
    end = [0] * (k - r - l)
    return length + a + end


def repetitionEncoder(m, n):
    return m * n if m == [1] or m == [0] else []


def repetitionDecoder(v):
    return [0] if v.count(0) > v.count(1) else [1] if v.count(0) < v.count(1) else []


def dataFromMessage(m):
    if not checkvalid(m):
        return []
    k = len(m)
    r = 2
    # Check the message is of the correct length
    while 2 ** r - r - 1 < k:
        r += 1
    # If it isn't of the correct length, return an empty list
    if 2 ** r - r - 1 != k:
        return []
    l = 0
    for i in range(0, r):
        l += m[i] * 2 ** (r - i - 1)
    # If r+l is bigger than the message, then there is an error so an empty list should be returned
    if r + l > len(m):
        return []
    # Check all elements in the padding are 0
    if not all(elem==0 for elem in m[r+l:k]):
        return []
    return m[r:r + l]


def hammingEncoder(m):
    if not checkvalid(m):
        return []
    l = len(m)
    r = 2
    # Ensuring that the list is of the correct length
    while 2 ** r - r - 1 < l:
        r += 1
    # If not return an empty list
    if 2 ** r - r - 1 != l:
        return []
    # Turn the two lists into numpy arrays so they can be multiplied
    message = np.array(m)
    matrix = np.array(hammingGeneratorMatrix(r))
    # Multiply the message by the hamming generator matrix mod 2 and turn it back to a python list
    return (message.dot(matrix) % 2).tolist()


def hammingDecoder(v):
    if not checkvalid(v):
        return []
    r = math.log(len(v) + 1, 2)

    if not r.is_integer():
        return []
    r = int(r)
    matrix = []
    # Create the parity check matrix
    for i in range(1, 2 ** r):
        matrix.append(decimalToVector(i, r))
    # Turn that matrix into a numpy data structure
    matrix = np.matrix(matrix)
    a = np.matrix(v)
    # Multiply the message by the parity check matrix mod 2
    # The line below this has errors when using test_up_to, errors on 2
    number = (a.dot(matrix) % 2).tolist()[0]
    # Convert the list representing a number to the actual number
    number = int("".join(str(x) for x in number), 2)
    if number==0:
        return v
    # Flip the bit in the message corresponding to number
    v[number - 1] = int(not v[number - 1])
    return v


def messageFromCodeword(c):
    if not checkvalid(c):
        return []
    r = 0
    l = len(c)
    count = 0
    # Ensure the message is of length 2^r-r-1
    while 2 ** r - 1 < l:
        r += 1
    # If it is not of correct length, return an empty list
    if 2 ** r - 1 != l:
        return []
    for i in range(0, r):
        # Removing indices corresponding to powers of 2
        c.pop(2 ** i - 1 - count)
        count += 1
    return c





