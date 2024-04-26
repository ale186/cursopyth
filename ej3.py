def asig(cad):
    c=[]
    for i in range(0, len(cad), 1):
        c.append(ord(cad[i]))
    return c
def orden(ls):
    c=[]
    d=[]
    aux=0
    for i in range(0, len(ls), 1):
        c.append(ord(ls[i]))
        if i>=1:
            if c[i]<c[i-1]:
                aux=c[i-1]
                c[i-1]=c[i]
                c[i]=aux
n=int(input())
a, b = map(str, input().split())
diga=asig(a)
digb=asig(b)