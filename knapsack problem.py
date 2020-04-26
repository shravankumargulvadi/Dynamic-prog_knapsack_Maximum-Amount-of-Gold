
# coding: utf-8

# In[16]:


import sys
def knapsack(W,w):
    value=dict()
    n=len(w)
    for i in range(n):
        value[0,i]=0
    for x in range(W+1):
        value[x,0]=0
    for i in range(1,n+1):
        for x in range(1,W+1):
            value[x,i]=value[x,i-1]
            if w[i-1]<=x:
                val=value[x-w[i-1],i-1]+w[i-1]
                if val>value[x,i]:
                    value[x,i]=val
    #print(value)
    return value[W,n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(knapsack(W, w))
                


# In[14]:


knapsack(10,[1,4,8])

