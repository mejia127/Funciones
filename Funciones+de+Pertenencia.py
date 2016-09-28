
# coding: utf-8

# FUNCIONES DE PERTENENCIA

# MARCELA MURILLO MEJIA

# Funcion Triangular $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<a \\ (x-a) &\mbox{si } a<=x<b\\ (c-x) & \mbox{si } b<=x<=c\\ 0 & \mbox{si } x>=c 
# \end{cases} 
# $$

# In[6]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[296]:

x=np.linspace(0,100)
a=5
b=50
c=95


# In[300]:

def f(x,a,b,c):
    if ((x<a) | (x>=c)):
        ans=1
    if ((a<=x) & (x<b)):
         ans=(x-a)
    if ((b<=x) & (x<=c)):
        ans=(c-x)
    return ans


# In[301]:

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c)


# In[303]:

plt.plot(x,f_vec(x,a,b,c),'>:b')
plt.grid(True)
plt.xlabel ("Valor x")
plt.ylabel ("Valor y")
plt.title("Funcion Triangular")


# Funcion Trapezoidal $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<=a \\ \frac {(x-a)}{(b-a)} &\mbox{si } a<=x<=b\\ 1 & \mbox{si } b<=x<=c\\ \frac{(d-x)}{(d-c)} & \mbox{si } c<=x<=d\\ 0 & \mbox{si } x>d
# \end{cases} 
# $$

# In[661]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[662]:

x=np.linspace(0,70)
a=30
b=20
c=50
d=20


# In[663]:

def f(x,a,b,c,d):
    if ((x<=a) | (x>d)):
        ans=0.8
    if ((a<=x) & (x<=b)):
         ans=(x-a)/(b-a)
    if ((b<=x) & (x<=c)):
        ans=1
    if ((c<=x) & (x<=d)):
         ans=(d-x)/(d-c)
    return ans


# In[664]:

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c,d)


# In[667]:

plt.plot(x,f_vec(x,a,b,c,d),'r')
plt.grid(True)
plt.xlabel ("Valor x")
plt.ylabel ("Valor y")
plt.title("Funcion Trapezoidal")


# Funcion Tipo Hombro Derecha $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<=\alpha  \\ \frac{(x-\beta)}{(\alpha-\beta)} & \mbox{si } \\ 1 & \mbox{si } x>=\beta
# \end{cases} 
# $$

# In[677]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[678]:

x=np.linspace(0,50)
alfa=5
beta=25


# In[679]:

def f(x,alfa,beta):
    if (x<=alfa):
        
        m=0
   
    if (alfa<=x)&(x<=beta):
        m=(x-beta)/(alfa-beta)
    
    if (x>=beta):
        m=1
   
    return m


# In[680]:

f_vec = np.vectorize(f)
func=f_vec(x,alfa,beta)


# In[681]:

plt.plot(x,f_vec(x,alfa,beta),'m:o')
plt.grid(True)
plt.xlabel ("Valor x")
plt.ylabel ("Valor y")
plt.title("Funcion Hombro Derecho")


# Funcion Hombro Izquierda $$f(x) = 
# \begin{cases} 
# 1 & \mbox{si } x<=\alpha  \\ \frac{(x-\alpha)}{(\beta-\alpha)} & \mbox{si } \\ 0 & \mbox{si } x>=\beta
# \end{cases} 
# $$

# In[682]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[683]:

x=np.linspace(0,50)
alfa=25
beta=60


# In[684]:

def f(x,alfa,beta):
    if (x<=alfa):
        
        p=1
   
    if (alfa<=x)&(x<=beta):
        p=(x-alfa)/(beta-alfa)
    
    if (x>=beta):
        p=0
   
    return p


# In[685]:

f_vec = np.vectorize(f)
func=f_vec(x,alfa,beta)


# In[686]:

plt.plot(x,f_vec(x,alfa,beta),'m:o')
plt.grid(True)
plt.xlabel ("Valor x")
plt.ylabel ("Valor y")
plt.title("Funcion Hombro Izquierdo")


# Funcion Tipo Saturacion $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<a \\ \frac {(x-a)}{(b-a)} &\mbox{si } a<=x<=b\\ 1 & \mbox{si } b<=x<=d\\ \frac{(x-d)}{(c-d)} & \mbox{si } d<=x<c\\ 0 & \mbox{si } x>=c
# \end{cases} 
# $$

# In[692]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[722]:

x=np.linspace(0,100)
a=5
b=30
c=0
d=70


# In[723]:

def f(x,a,b,c,d):
    
    if (x<a)|(x>=c):
        m=0
   
    if (a<=x)&(x<=b):
        m=(x-a)/(b-a)
    
    if (b<=x)&(x<=d):
        m=1
    
    if (d<=x)&(x<c):
        m=(x-d)/(c-d)
    return m


# In[724]:

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c,d)


# In[725]:

plt.plot(x,f_vec(x,a,b,c,d),'g:o')
plt.grid(True)
plt.xlabel ("Valor x")
plt.ylabel ("Valor y")
plt.title("Funcion Saturacion")


# Funcion Sigmoidal

# In[811]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[812]:

x = np.arange(-5.0, 5.0, 0.5)


# In[813]:

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a


# In[814]:

sig = sigmoid(x)


# In[815]:

plt.plot(x, sigmoid(x), 'm:*')
plt.grid(True)
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Sigmoidal')


# Funcion S o Sigmoidal $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<a \\ 2\frac {(x-a)}{(c-a)} &\mbox{si } a<=x<b\\  1-2\left ( \frac{(x-c)}{(c-a)}\right )^{2} & \mbox{si } b<=x<=c\\ 1 & \mbox{si } x>c
# \end{cases} 
# $$

# In[816]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[817]:

x=np.linspace(0,60)
a=10
c=30


# In[818]:

def f(x,a,c):
    
    if (x<=a):
        p=0
        
    if (a<=x)&(x<=((a+c)/2)):
        p=2*(((x-a)/(c-a))**2)
        
    if (((a+c)/2)<=x)&(x<=c):
        p=1-2*(((x-a)/(c-a))**2)
        
    if (x>=c):
        p= 1
        
    return p


# In[819]:

f_vec = np.vectorize(f)
func=f_vec(x,a,b)


# In[823]:

plt.plot(x,f_vec(x,a,c), 'b:o')
plt.grid(True)
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion S')


# In[ ]:



