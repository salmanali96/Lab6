#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random

count = 0;

def FastestWay(a,t1,t2,t3,e,x,n):

    f1 = []
    f2 = []
    f3 = []
    f1.append(e[0] + a[0][0])
    f2.append(e[1] + a[1][0])
    f3.append(e[2] + a[2][0])
    I1 = []
    I2 = []
    I3 = []
    string1 = "line 1"
    string2 = "line 2"
    string3 = "line 3"
    for i in range(1,n):

        if f1[i-1] + a[0][i] <= f2[i-1] + t2[0][i-1] + a[0][i] and f1[i-1] + a[0][i] <= f3[i-1] + t3[0][i-1] + a[0][i]:
            f1.append(f1[i-1] + a[0][i])
            I1.append(1)
            string1 = string1 + " ->line1 "
        elif f2[i-1] + t2[0][i-1] + a[0][i] <= f3[i-1] + t3[0][i-1] + a[0][i]:

            f1.append(f2[i-1] + t2[0][i-1] + a[0][i])
            I1.append(2)
            string1 = string1 + " ->line 2 to line 1 "
        else:
            f1.append(f3[i-1] + t3[0][i-1] + a[0][i])
            I1.append(3)
            string1 = string1 + " ->line 3 to line 1 "



        if f2[i-1] + a[1][i] <= f1[i-1] + t1[0][i-1] + a[1][i] and f2[i-1] + a[1][i] <= f3[i-1] + t3[1][i-1] + a[1][i]:
            f2.append(f2[i-1] + a[1][i])
            I2.append(2)
            string2 = string2 + " ->line 2 "

        elif f1[i-1] + t1[0][i-1] + a[1][i] <=  f3[i-1] + t3[1][i-1] + a[1][i]:
            f2.append(f1[i-1] + t1[0][i-1] + a[1][i])
            I2.append(1)
            string2 = string2 + " ->line 1 to line 2 "
        else:
            f2.append(f3[i-1] + t3[1][i-1] + a[1][i])
            I2.append(3)
            string2 = string2 + " ->line 3 to line 2 "



        if f3[i-1] + a[2][i] <= f1[i-1] + t1[1][i-1] + a[2][i] and f3[i-1] + a[2][i] <= f2[i-1] + t2[1][i-1] + a[2][i]:
            f3.append(f3[i-1] + a[2][i])
            I3.append(3)
            string3 = string3 + " ->line 3 "

        elif f1[i-1] + t1[1][i-1] + a[2][i] <= f2[i-1] + t2[1][i-1] + a[2][i]:
            f3.append(f1[i-1] + t1[1][i-1] + a[2][i])
            I3.append(1)
            string3 = string3 + " ->line 1 to line 3 "


        else:
            f3.append(f2[i-1] + t2[1][i-1] + a[2][i])
            I3.append(2)
            string3 = string3 + " ->line 2 to line 3 "

           
    n = n -1
    if f1[n] + x[0] <= f2[n] + x[1] and f1[n] + x[0] <= f3[n] + x[2]:
        #print("f1")
        print("Total Cost: ",f1[n] + x[0])
        print (string1)
        #print(?1)
    elif f2[n] + x[1] <= f3[n] + x[2]:
        #print("f2")
        print("Total Cost: ",f2[n] + x[1])
        print (string2)

    else:
        #print("f3")
        print("Total Cost: ",f3[n] + x[2])
        print (string3)


def base(a,t1,t2,t3,e,x,n):
    
    f1 = []
    f2 = []
    f3 = []
    f1.append(e[0] + a[0][0])
    f2.append(e[1] + a[1][0])
    f3.append(e[2] + a[2][0])
    I1 = []
    I2 = []
    I3 = []
    j = 1 

    Recursive(f1,f2,f3,j,a,t1,t2,t3,n,x,I1,I2,I3)

def Recursive(f1,f2,f3,i,a,t1,t2,t3,n,x,I1,I2,I3):

    if i > n-1:

        

        n = n -1
        if f1[n] + x[0] <= f2[n] + x[1] and f1[n] + x[0] <= f3[n] + x[2]:
            
            print("Total Cost: ",f1[n] + x[0])
            #print(?1)
        elif f2[n] + x[1] <= f3[n] + x[2]:
           
            print("Total Cost: ",f2[n] + x[1])

        else:
         
            print("Total Cost: ",f3[n] + x[2])
      
      
    else:


        if f1[i-1] + a[0][i] <= f2[i-1] + t2[0][i-1] + a[0][i] and f1[i-1] + a[0][i] <= f3[i-1] + t3[0][i-1] + a[0][i]:
            f1.append(f1[i-1] + a[0][i])
            I1.append(1)
        elif f2[i-1] + t2[0][i-1] + a[0][i] <= f3[i-1] + t3[0][i-1] + a[0][i]:

            f1.append(f2[i-1] + t2[0][i-1] + a[0][i])
            I1.append(2)

        else:
            f1.append(f3[i-1] + t3[0][i-1] + a[0][i])
            I1.append(3)



        if f2[i-1] + a[1][i] <= f1[i-1] + t1[0][i-1] + a[1][i] and f2[i-1] + a[1][i] <= f3[i-1] + t3[1][i-1] + a[1][i]:
            f2.append(f2[i-1] + a[1][i])
            I2.append(2)

        elif f1[i-1] + t1[0][i-1] + a[1][i] <=  f3[i-1] + t3[1][i-1] + a[1][i]:
            f2.append(f1[i-1] + t1[0][i-1] + a[1][i])
            I2.append(1)

        else:
            f2.append(f3[i-1] + t3[1][i-1] + a[1][i])
            I2.append(3)



        if f3[i-1] + a[2][i] <= f1[i-1] + t1[1][i-1] + a[2][i] and f3[i-1] + a[2][i] <= f2[i-1] + t2[1][i-1] + a[2][i]:
            f3.append(f3[i-1] + a[2][i])
            I3.append(3)

        elif f1[i-1] + t1[1][i-1] + a[2][i] <= f2[i-1] + t2[1][i-1] + a[2][i]:
            f3.append(f1[i-1] + t1[1][i-1] + a[2][i])
            I3.append(1)

        else:
            f3.append(f2[i-1] + t2[1][i-1] + a[2][i])
            I3.append(2)


        i = i + 1

        Recursive(f1,f2,f3,i,a,t1,t2,t3,n,x,I1,I2,I3)


def SimpleRecursive(a,t1,t2,t3,e,x,n,line):
    try:
        if n == 0:
            return e[line] + a[line][0]
    
        else:

            T0 = 999999
            T1 = 999999
            T2 = 999999

            if line == 0:
                        T0= min(SimpleRecursive(a,t1,t2,t3,e,x,n-1,0) + a[0][n],SimpleRecursive(a,t1,t2,t3,e,x,n-1,1) + t2[0][n-1] + a[0][n],SimpleRecursive(a,t1,t2,t3,e,x,n-1,2)+ t3[0][n-1] + a[0][n])
            elif line == 1:
                        T1 = min(SimpleRecursive(a,t1,t2,t3,e,x,n-1,1) + a[1][n],SimpleRecursive(a,t1,t2,t3,e,x,n-1,0) + t1[0][n-1] + a[1][n],SimpleRecursive(a,t1,t2,t3,e,x,n-1,2) + t3[1][n-1] + a[1][n])

            elif line == 2:              
                        T2 = min(SimpleRecursive(a,t1,t2,t3,e,x,n-1,2) + a[2][n],SimpleRecursive(a,t1,t2,t3,e,x,n-1,0) + t1[1][n-1] + a[2][n],SimpleRecursive(a,t1,t2,t3,e,x,n-1,1) + t2[1][n-1] + a[2][n])


            return min(T0,T1,T2)

    except IndexError:

        print('Index out of bound')



a = []
a.append([])
a.append([])
a.append([])

for i in range(1,10):
    a[0].append(random.randint(15,25))
    a[1].append(random.randint(15,25))
    a[2].append(random.randint(15,25))
#a[0].append(20)
#a[0].append(25)
#a[0].append(15)
#a[0].append(18)

#a[1].append(22)
#a[1].append(23)
#a[1].append(25)
#a[1].append(28)

#a[2].append(13)
#a[2].append(18)
#a[2].append(22)
#a[2].append(25)


t1 = []
t1.append([])
t1.append([])

t2 = []
t2.append([])
t2.append([])

t3 =[]
t3.append([])
t3.append([])
for i in range(1,10):
    t1[0].append(random.randint(0,5))
    t1[1].append(random.randint(0,5))

    t2[0].append(random.randint(0,5))
    t2[1].append(random.randint(0,5))

    t3[0].append(random.randint(0,5))
    t3[1].append(random.randint(0,5))



#t1[0].append(5)
#t1[0].append(4)
#t1[0].append(3)

#t1[1].append(2)
#t1[1].append(3)
#t1[1].append(4)





#t2[0].append(4)
#t2[0].append(6)
#t2[0].append(5)

#t2[1].append(2)
#t2[1].append(3)
#t2[1].append(4)

#t3 =[]
#t3.append([])
#t3.append([])

#t3[0].append(2)
#t3[0].append(3)
#t3[0].append(4)

#t3[1].append(4)
#t3[1].append(2)
#t3[1].append(1)

e = [2,2,2]
x = [3,3,3]

n  = 9

print('Through Dynamic Programming')
FastestWay(a,t1,t2,t3,e,x,n)

print('Through Recursion with memoization')
base(a,t1,t2,t3,e,x,n)

print('Only Recursion')
base(a,t1,t2,t3,e,x,n)
SimpleRecursive(a,t1,t2,t3,e,x,8,1)