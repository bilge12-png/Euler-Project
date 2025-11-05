#!/usr/bin/env python
# coding: utf-8

# In[18]:


list=[]
for i in range(1,1000):
    if i%3==0 or i%5==0:
        list.append(i)
print(sum(list))



# In[56]:


list=[0,1]
for i in range(1,100):
    list[i]=list[i-1]+list[i-2]
    if list[i]//4000000==1:
        break
    list.append(list[i])
    
print(list)
list.pop(34)
fib=[]
for i in range(0,len(list)):
    if list[i] % 2 == 0:
        fib.append(list[i])
        
    
print(sum(fib))


# In[3]:


#boolean logic
prime=[]
for i in range(3, 60008):
    is_prime = True
    for inte in range(2, i):
        if i % inte == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)


m=600851475143
list=[]
for i in range(len(prime)):
    if 600851475143%prime[i]==0:
        list.append(prime[i])
print(max(list))
        


# In[16]:


list=[]
for i in range(100,1000):
    for m in range(100,1000):
        l=str(i*m)
        if len(l)==6 and l[0]==l[5] and l[2]==l[3] and l[1]==l[4]:
            list.append(l)
print(max(list))
    




# In[30]:


def delbart(t,n):
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not delbart(i,20):
    i +=20

print(i)


# In[37]:


#the same logic i used when doing pen/paper but did not know how to write it
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print(i)


# In[97]:


prime=[]
for i in range(2, 150008):
    is_prime = True
    for inte in range(2, int(i ** 0.5) + 1):
        if i % inte == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
print(len(prime))
print(prime[10000])


# In[43]:


ans1=0
ans2=0
for i in range(1,101):
    ans1+=(i**2)
    ans2+=i
calc=(ans2)**2-(ans1)
print(calc)


# In[86]:


num=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
num=str(num)
print(len(num))
list=[]
for i in range(0,988):
    m=int(num[i])*int(num[i+1])*int(num[i+2])*int(num[i+3])*int(num[i+4])*int(num[i+5])*int(num[i+6])*int(num[i+7])*int(num[i+8])*int(num[i+9])*int(num[i+10])*int(num[i+11])*int(num[i+12])
    list.append(m)
print(max(list))


# In[91]:


import numpy as np
for a in range(1,1000):
    for b in range(1,1000):
            m=np.sqrt(a**2+b**2)
            if m+b+a==1000:
                print([a,b])
                print(m*a*b)
            else:
                continue


# In[98]:


prime=[]
for i in range(2, 2000000):
    is_prime = True
    for inte in range(2, int(i ** 0.5) + 1):
        if i % inte == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
print(sum(prime))


# In[ ]:




