import math

#Exercise 1

def repeater(s1,s2,n):
       return '_'+((s1 + s2)*n)+'_'

#Exercise 2

def roots(a,b,c):
    root1 =(-b + (math.sqrt(b**2 - (4*a*c))))/(2*a)
    root2 = (-b - (math.sqrt(b**2 - (4*a*c))))/(2*a)
    print ('The quadratic equation with coefficients',' a =',a,'b =',b,'c =',c, 'has the following solutions (i.e. roots):')
    print (root1,'and', root2)


#Exercise 3
       
def real_roots(a,b,c):
    real_roots = b**2 - (4*a*c)
    return real_roots >= 0

#Exercise 4

def reverse(x):
    a = x//10
    b = x%10
    return b*10 + a
                  
