#!/usr/bin/env python
# coding: utf-8

# # Reading the dataset

# In[152]:


import pandas as pd
file = "C:\\Users\\varsh\\Downloads\\kdrama movies.csv"
df = pd.read_csv(file)
df.head(20)


# # Regular Expressions

# In[153]:


import regex as re

def tokenize(text):
    return re.findall(r'[\w-]*[a-z|A-Z][\w-]*', text)


# In[154]:


def remove_stop(tokens):
    return [t for t in tokens if t.lower() not in stopwords]


# # Example

# In[155]:


testtext= "One:Two:Three:Four"
testtokens = tokenize(testtext)
print(testtokens)


# # 1. Removing the stopwords using regex

# In[156]:


import nltk
nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('english'))
print(stopwords)


# # Function to remove stopwords

# In[157]:


#Defining a Function to Remove Stop Words
def remove_stop(tokens):
    return [t for t in tokens if t.lower() not in stopwords]
#Just testing it
cleantokens= remove_stop(testtokens)
print(cleantokens)


# # Creating a Text processing Pipeline

# In[158]:


def prepare(Tags, pipeline):
    tokens = Tags
    for fun in pipeline:
        tokens = fun(tokens)
    return tokens
df['tokens'] = df['Tags'].apply(prepare, pipeline=pipeline)


# In[159]:


#columns
df.columns


# In[160]:


df.dtypes


# In[161]:


#printing the datatypes
df.info()


# In[162]:


df.describe()


# In[163]:


df['length'] = df['Tags'].str.len()
df.describe()


# In[164]:


##Checking for missing data
df.isna().sum()


# In[165]:


#fill the missing data
df['Rating'].fillna('unknown', inplace=True)
df['Synopsis'].fillna('unknown', inplace=True)


# In[166]:


df.isna().sum()


# In[167]:


##stats about text fields
df.describe(include='O')


# In[168]:


df['Synopsis'] = df['Synopsis'].str.upper()

df


# In[169]:


#uppercase all the text
df['Tags'] = df['Tags'].str.upper()
df


# In[ ]:





# In[170]:


##running pipeline
df['tokens'] = df['Tags'].apply(prepare,pipeline=pipeline)
df['num_tokens'] = df['tokens'].map(len)
df.tail()


# # applying pipeline to df coloumn

# In[171]:


df['tokens'] = df['Tags'].apply(prepare, pipeline=pipeline)


# In[172]:


from collections import Counter
counter = Counter()


# # Word frequency analysis

# In[173]:


from collections import Counter


# In[174]:


tokens = tokenize("She likes action and horror movies.")


# In[175]:


testcount= Counter(tokens)
print(testcount)


# In[176]:


#adding new data to current count

more_tokens=tokenize("She likes action and horror movies.")
testcount.update(more_tokens)
print(testcount)


# In[177]:


counter = Counter()
df['tokens'].map(counter.update)
print(counter.most_common(5))


# In[178]:


##Put the word frequency in it’s owndataframe 
df['tokens'].map(counter.update)
print(counter.most_common(5))
freq_df = pd.DataFrame.from_dict(counter,orient='index', columns=['freq'])
freq_df = freq_df.query('freq >= 1')
freq_df.index.name = 'token'


# In[179]:


## Sort and display

freq_df = freq_df.sort_values('freq', ascending=False)
freq_df.head(10)


# In[180]:


freq_df.describe()


# # Plots

# In[196]:


#chart
df['length'].plot()
df


# In[195]:


#chart
df['length'].plot(kind='box', vert=False)
df


# In[194]:


#bar plot
import seaborn as sns
where = df['Aired On'].isin(['Friday','Thursday'])
g = sns.catplot(data=df[where], x="Aired On", y="length", kind='box')
g.fig.set_size_inches(10, 8) ###


# In[ ]:


#Histogram
df['Number of Episodes'].plot(kind='hist', bins=30)
df


# # Statistics

# In[ ]:


import seaborn as sns
where = df['Rating'].isin(['9.1', '9.2'])
g = sns.catplot(data=df[where], x="Year of release", kind='box')
g.fig.set_size_inches(10, 8) ###


# In[ ]:


## Sort and display

freq_df = freq_df.sort_values('freq', ascending=False)
freq_df.head(10)
freq_df.describe()


# In[ ]:


# bar plot
ax = freq_df.head(15).plot(kind='barh', width=0.95, figsize=(12,8))
ax.invert_yaxis()
ax.set(xlabel='Frequency', ylabel='Token', title='Top Words')


# # Word Cloud

# In[ ]:


get_ipython().system('pip install wordcloud')


# In[186]:


from wordcloud import WordCloud
from matplotlib import pyplot as plt
wc = WordCloud(background_color='white', width = 300, height=300, margin=2)
wc.fit_words(freq_df['freq'].to_dict() )
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()


# # 4.Taking 5 random strings and performing regex on them.

# In[187]:


import re

email = "john.doe@example.com"
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(regex, email):
    print("Valid email address")
else:
    print("Invalid email address")


# In[188]:


url = "https://www.example.com"
regex = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}(/.*)?$'
if re.match(regex, url):
    print("Valid URL")
else:
    print("Invalid URL")


# In[189]:


phone_number = "(555) 123-4567"
regex = r'^\(\d{3}\) \d{3}-\d{4}$'
if re.match(regex, phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")


# In[190]:


date = "2024-04-27"
regex = r'^\d{4}-\d{2}-\d{2}$'
if re.match(regex, date):
    print("Valid date")
else:
    print("Invalid date")


# In[191]:


file_path = "/path/to/file.txt"
regex = r'^\/(?:[^\/\n]+\/)*[^\/\n]+\.[a-zA-Z0-9]{2,5}$'
if re.match(regex, file_path):
    print("Valid file path")
else:
    print("Invalid file path")


# In[ ]:




