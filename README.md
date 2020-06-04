# CT Error Correcting Codes Coursework

Coursework for the Error Correcting Codes submodule of the Computational Thinking 1st Year Module at Durham University

All of the functions are stored in the one file `codes.py`

## Hamming Codes

### Task 1

Write a function `message(a)`, where `a` is a vector of any positive length that converts a to a message for a Hamming code

### Task 2

Write a function `hammingEncoder(m)` where `m` is a vector of length 2<sup>r</sup>-r-1 for some r≥2 that acts as an encoder for Hamming codes.

### Task 3

Write a function `hammingDecoder(v)` where `v` is a vector of length 2<sup>r</sup>-1 for some r≥2 that acts as a decoder for Hamming codes.

### Task 4

Write a function `messageFromCodeword(c)`, where `c` is a vector of length 2<sup>r</sup>-1 for some r≥2 that recovers the message from the codeword of a Hamming code.

### Task 5

Write a function `dataFromMessage(m)`, where `m` is a vector of length 2<sup>r</sup>-r-1 for some r≥2 that recovers the raw data from the message.

## Repetition Codes

### Task 1

Write a function `repetitionEncoder(m,n)`, where `m` is a vector of length 1 and `n` is a positive integer that acts as an encoder for repetition codes.

### Task 2

Write a function `repetitionDecoder(v)`, where `v` is a vector of any positive length that acts as a decoder for repetition codes.
