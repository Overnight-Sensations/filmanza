#!/usr/bin/env python
# coding: utf-8

# In[46]:


import colorama
from colorama import Fore,Style
l="FILMANZA"
print(f"{Fore.RED} {Style.BRIGHT}")
import time
print('\t\t',end='')
for i in l:
    time.sleep(0.9)
    print(i,end='\t')
time.sleep(5)   



# In[84]:


print(f"{Fore.BLUE}{Style.BRIGHT} 1.BOLLYWOOD\n\n {Fore.BLUE}{Style.BRIGHT}2.HOLLYWOOD\n\n{Fore.MAGENTA}{Style.BRIGHT}PRESS 1 FOR BOLLYWOOD\n\n{Fore.MAGENTA}{Style.BRIGHT}PRESS 2 FOR HOLLYWOOD\n\n{Fore.BLUE}{Style.BRIGHT}INPUT:  ")


# In[57]:


print(f"{Fore.BLUE}{Style.BRIGHT}M O D E S:\n\n {Fore.YELLOW}{Style.BRIGHT} \tEASY\n\n {Fore.GREEN}{Style.BRIGHT} \t\tMEDIUM\n\n {Fore.CYAN}{Style.BRIGHT} \t\t\t\tHARD")


# In[67]:


a='LOADING.....'
print(f"{Fore.MAGENTA}{Style.BRIGHT}")
print("\n")
print("\t",end='')
for i in a:
    time.sleep(1)
    print(i,end='\t')


# In[79]:


E="/EASY/"
print(f"{Fore.YELLOW}{Style.BRIGHT}")
print("\t\t\t\t",end='')
for i in E:
    time.sleep(0.5)
    print(i,end=' \t')


# In[80]:


M='/MEDIUM/'
print(f"{Fore.GREEN}{Style.BRIGHT}")
print("\t\t\t",end='')
for i in M:
    time.sleep(0.5)
    print(i,end=' \t')


# In[78]:


H='/HARD/'
print(f"{Fore.CYAN}{Style.BRIGHT}")
print("\t\t\t\t",end='')
for i in H:
    time.sleep(0.5)
    print(i,end=' \t')


# In[ ]:




