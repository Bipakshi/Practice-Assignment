#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# #1. Given the code below, insert the correct negative index on line 3 in order to get the last character in the string.

# In[5]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string [-1])


# #2. Given the code below, insert the correct positive index on line 3 in order to return the comma character from the string.

# In[7]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string [7])


# #3. Given the code below, insert the correct negative index on line 3 in order to return the w character from the string.

# In[14]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string [-10])


# #4. Given the code below, insert the correct method on line 3 in order to return the index of the B character in the string.

# In[20]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.index("B"))


# #5.Given the code below, insert the correct method on line 3 in order to return the number of occurrences of the letter o in the string.

# In[43]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.count("o"))


# #6. Given the code below, insert the correct method on line 3 in order to convert all letters in the string to uppercase.

# In[25]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.upper())


# #7. Given the code below, insert the correct method on line 3 in order to get the index at which the substring Bitcoin starts.

# In[27]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.index('Bitcoin'))


# #8. Given the code below, insert the correct method on line 3 in order to check of the string starts with the letter X.

# In[45]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.startswith('p'))


# #9. Given the code below, insert the correct method on line 3 in order to convert all uppercase letters to lowercase and all lowercase letters to uppercase.

# In[47]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas xbar."
print(my_string.swapcase())


# #10.given the code below, insert the correct method on line 3 in order to remove all spaces (single Space characters from the keyboard) from the string.g

# In[50]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas xbar."
print(my_string.replace(" ",""))


# #11. Given the code below, insert the correct method on line 3 in order to replace all the occurrences of letter i with the substring btc.

# In[52]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas xbar."
print(my_string.replace("i","btc"))


# #12. Given the code below, insert the correct method on line 3 in order to split the entire string in two parts, using the comma as a delimiter.

# In[60]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas xbar."

print(my_string.split(','))


# #13. Given the code below, insert the correct method on line 3 in order to join the characters of the string using the & symbol as a delimiter.

# In[59]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print('&'.join(my_string))


# #14. Given the code below, insert the correct code on line 4 in order to concatenate my_string with the following string:
# 
# #my_other_string = "Poor guy!"
# 
# 

# In[64]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
my_other_string = "Poor guy!"
print(my_string + my_other_string)


# #15. Given the code below, insert the correct method on line 3 in order to convert the first letter of each word in the string to uppercase.

# In[65]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.title())


# #16. Given the code below, use string formatting with the % operator on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.

# In[66]:


my_string = "In %s, someone paid %s %s for two pizzas."

print(my_string %('2010', '10K', 'Bitcoin'))


# #17. Given the code below, use string formatting with the format() method on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.
# 
# 

# In[67]:


my_string = "In {}, someone paid {} {} for two pizzas."

print(my_string.format('2010', '10K', 'Bitcoin'))


# #18. Given the code below, use slicing and insert the correct code on line 3 in order to return the substring 2010 from the string. Use positive indexes!

# In[69]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[3:7])


# #19. Given the code below, use slicing and insert the correct code on line 3 in order to return the substring Bitcoin from the string. Use negative indexes!

# In[79]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."


print(my_string[-23:-16])


# #20. Given the code below, use slicing and insert the correct code on line 3 in order to return the first 12 characters in the string. Use a single, positive index!

# In[85]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."


print(my_string[:13])


# #21. Given the code below, use slicing and insert the correct code on line 3 in order to return the last 9 characters of the string. Use a single, negative index!

# In[86]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."


print(my_string[-9:])


# #22. Given the code below, use slicing and insert the correct code on line 3 in order to return the entire string in reversed order.

# In[97]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."


print(my_string[::-1])


# #23. Given the code below, use slicing and insert the correct code on line 3 in order to return every 7th character of the string, starting with the first character.
# 
# The final result should be I,n top
# 
# 

# In[100]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[::7])


# #24. Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the first 10 characters. Use a single, positive index!

# In[102]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[10:])


# #25. Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the last 4 characters. Use a single, negative index!
# 
# 

# In[104]:


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[:-4])


# In[ ]:




