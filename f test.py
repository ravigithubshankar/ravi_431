

maximum,minimum=1000,-1000
def aplha_beta(d,node,maxp,v,a,b):
    if d==3:
        return v[node]
    if maxp:
        best=minimum
        for i in range(0,2):
            value=aplha_beta(d+1,node*2+i,False,v,a,b)
            #print(value)
            best=max(best,value)
            #print(best)
            a=max(a,best)
            print(a)
            if b<=a:
                break
        return best
    else:
        best=maximum
        for i in range(0,2):
            value=aplha_beta(d+1,node*2+i,True,v,a,b)
            best=min(best,value)
            b=min(b,best)
            if b<=a:
                break
        return best
src=[]
x=int(input("enter total no.of leaf nodes:"))
for i in range(x):
    y=int(input("enter the node:"))
    src.append(y)
d=int(input("depth value:"))
node=int(input("node_value:"))
print("the optimal_value is:",aplha_beta(d,node,False,src,minimum,maximum))
from re import S
import matplotlib.pyplot as plt
k=aplha_beta(d,node,False,src,minimum,maximum)
plt.plot(k)
plt.show()
