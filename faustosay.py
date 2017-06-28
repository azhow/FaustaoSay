#!/usr/bin/env python3
from generator import main as pais_da_europa

if __name__ == '__main__':
    frase = pais_da_europa()
    lis = frase.split()
    s = 0
    print("/---------------------------------------------\\")
    for i in lis:
        s += len(i)
        if i == lis[0]:
            print('| ', end='')
        if s > 40:
            s -= len(i)
            for j in range(40-s):
                print(end=' ')
            print('|\n|', end=' ')
            print(i, end=' ')
            s = 0
            s += len(i)
        else:
            print(i, end=' ')
        if i == lis[-1]:
            for j in range(40-s):
                print(end=' ')
            print('|')
    print("\---------------------------------------------/")
