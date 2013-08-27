# -*- coding: UTF-8 -*-

for x in range(0, 10):
    for n in range(2, x/2+1):
        if(x % n == 0):
            print x,"is not a prime."
            break;
    else:
        print x,"is a prime."         