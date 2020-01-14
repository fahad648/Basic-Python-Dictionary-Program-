
# coding: utf-8

# # LAB 08 (Dictionaries In Python)

# # program1

# In[3]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006'}
print("dict['Name]:",dict['Name'])
print(("dict['Age']:",dict ['Age']))
print("dict['DOB']:",dict['DOB'])
print("dict['Class']:",dict['Class'])


# # Program2

# In[4]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006'}
for x in dict:
    print(dict[x])


# # Program3

# In[5]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006'}
for x in dict.values():
    print(x)


# # program4

# In[6]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006'}
for x,y in dict.items():
    print(x,y)


# In[7]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006'}
if 'DOB'in dict.keys():
    print("Yes,'DOB is one of the keys in the dict dictionary'")


# # Program 6

# In[11]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006'}
dict['Age']=12.5
dict['School']='The Seeds School'
print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])
dict['Friend1']='MOhib'
dict['Friend2']='Akbar'
dict['Friend3']='Jazil'
print("dict['Friend1']:",dict['Friend1'])
print("dict['Friend2']:",dict['Friend2'])
print("dict['Friend3']:",dict['Friend3'])


# # Program7

# In[13]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006','Age':'12.5','Friend1':'MOhib','Friend2':'Akbar','Friend3':'Jazil'}
for x,y in dict.items():
    print(x,y)
dict.pop('Friend1')
print(dict)


# # Program8

# In[14]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006'}
dict['Age']=12.5
dict['School']='The Seeds School'
print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])
dict['Friend1']='MOhib'
dict['Friend2']='Akbar'
dict['Friend3']='Jazil'
print("dict['Friend1']:",dict['Friend1'])
print("dict['Friend2']:",dict['Friend2'])
print("dict['Friend3']:",dict['Friend3'])
del dict['Friend1']
print(dict)


# # Program9

# In[20]:


dict={'Name':'Jibran','Age':'12','Class':'Sixth','DOB':'16 April 2006','Age':'12.5','Friend1':'MOhib','Friend2':'Akbar','Friend3':'Jazil'}
print(dict)
for x,y in dict.items():
    print(x,y)
for z in dict.popitem():
    print("After popping from the the dictionary the remaining elements are:",z)


# In[25]:


family={'Father':'Farooq','Brothers':'Umer,Subhan','Sister':'Anusha','Mother':'Rubina'}
print(family)
print("AFTER updating")
print("-----------------------------------------")
family['Khala']='Sumaira,Naila,Kiran'
family['Phupo']='Yasmeen,Salma,Fehmida'
family['Mamu']='Khurram,Waqas'
print(family)
        


# In[37]:


number={'fahad':'03212465','ahe':'03251','aerrrd':'0163411111','qwre':'21532011010','aee':'00101010','sewerw':'.3110100','dfrff':'021111','ssdaff':'201221200222'}
print(len(number))
del number['fahad']
print(number)
print(len(number))


# In[49]:


def hexASCII():
    for i in range(ord('a'),ord('z')+1):
        print('|Chr:"{}" Hex-Notation:"{:X}"|'.format(chr(i),i))
hexASCII()


# In[30]:


my_choice={'1':'Qeema','2':'zinger','3':'Broast','4':'lazania'}
cooked={'1':'chicken karahi','2':'chicken qorma','3':'zinger','4':'lazania'}
n=0
for i in cooked.values():
    if i  in my_choice.values():
        n+=1
        print(i,"is match from my choice")
print("total number of dishes in my choice",n)


# In[38]:


parents={'1':'kamal','2':'anila','3':'faisal','4':'fahad','5':'birjees','6':'saif','7':'muhib','8':'waqar',}
my_choice={'1':'kamal','2':'farhan','3':'faisal','4':'birjees','5':'saif','6':'saima','7':'waqar','8':'wajid'}
total_list={'1':'kamal','2':'anila','3':'faisal','4':'fahad','5':'saif','6':'saima','7':'waqar','8':'wajid','9':'farhan','10':'birjess'}
n=0
for i in parents.values():
    if i in my_choice.values():
        n+=1
        print(i,"these are same guest in both list")            
print(n,"number of guest are common")
print(len(total_list),"the length of total number of guest")

