## List or String Processing
Minesweeper is a single-player video game played on a board containing hidden bombs. The bombs are located in some cells that are unknown by the player. The goal is to find all the bombs without detonation any of them. To do this, the player can click on a chosen field, which can lead to one of two scenarios:

    1. If a bomb was located in this field, the bomb explodes and the player loses the game;
    2. If there was no bomb, one digit is revealed in this field. The digit('0' - '8') indicates the number of bombs in the neighbourhood of this field.
    
Two fields are neighbours if they share a side or a corner. For example, in the image below, neighbours of the black field are marked in gray.

![Image](https://github.com/user-attachments/assets/f9f89bb7-64c6-4a94-9792-109d8ccef30e)

You are given a square board with N rows and N columns (both numbered from 0 to N-1). The upper left field is located at (0,0). M bombs (numbered from 0 to M-1) are hidden on the board. The K-th bomb is located in row R[K] and column c[K].

Print the description of the board with in N lines. The K-th line describes the K-th row and consists of N characters. Denote bombs with the character 'B', and in  places with no bombs, print the number of bombs in their nieghbourhood, as explained above.

Write a function:
    
    def solution(N,R,C)
    
that, given an Integer N and two arrays R and C, both consisting of M integers, prints the description of the Minesweeper board.

Examples:

1. Given N=3, R=[2,1,0,2] and C=[0,2,1,2], your function should print:

        1B2
        24B
        B3B

2. Given N=5, R=[2,3,2,3,1,1,3,1] and C=[3,3,1,1,1,2,2,3] your Functions should print:

        12321
        2BBB2
        3B8B3
        2BBB2
        12321

