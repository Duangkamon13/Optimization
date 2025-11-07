"""
Given a message containing only M possible states,
if we want to represent this message using a binary code,
write a program to calculate a minimal number of bits needed to sufficiently represent a message.
[Hint: 1 bit, i.e., 0 or 1, can represent 2 states.
2 bits, i.e., 00, 01, 10, or 11, can represent 4 states.
3 bits, i.e., 000, 001, 010, ..., or 111, can represent 8 states.
And, so on.]
"""

import math

def find_num_bits(num_states):
    '''
    param:
    num_states: a number of possible states

    return:
    num_bits: a number of bits sufficient to all states
    '''

    ## [!!Marker 1!!]
    ## Do not change anything above this line.
    ## ----------------------------------------

    num_bits = math.ceil(math.log(num_states , 2))

    # Fill in your code.


    ## Do not change anything below this line.
    ## [!!Marker 2!!]
    ## ----------------------------------------

    return num_bits



if __name__ == '__main__':

    g = lambda f: f(int(input('Enter # possible states:')))
    print(g(find_num_bits))



