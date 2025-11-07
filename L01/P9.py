"""
Write a program to calculate a simple triad chord.
The program takes 1 input: the 1st note marked by a number from 1 o 7.
Then, it computes other 2 notes and report all 3 notes.
Note: 1st Chord has 1, 3, 5; 2nd Chord has 2, 4, 6; ...; 7th Chord has 7, 2, 4.

"""

def find_triad(note1):

    ## Do not change anything above this line.
    ## ----------------------------------------

    # note1: the first note (init: 1, ..., 7)
    # note2: the second note (init: 1, ..., 7)
    # note3: the third note (init: 1, ..., 7)

    note2 = ((note1+2-1) % 7 )+1
    note3 = ((note1+4-1) % 7 )+1 

    # Fill in your code to have note2 and note3 the correct values.


    ## Do not change anything below this line.
    ## ----------------------------------------

    return note2, note3



if __name__ == '__main__':
    n1 = int(input('The first note:'))

    n2, n3 = find_triad(n1)

    scale = 'CDEFGAB'
    print('Triad: ', str(n1), str(n2), str(n3))
    print(scale[n1-1]+','+scale[n2-1]+','+scale[n3-1])
