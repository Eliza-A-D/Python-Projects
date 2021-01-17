#!/usr/bin/env python
# coding: utf-8

# # Profitable App Profiles for the App Store and Google Play Markets
# 
# Data Analysis of which types of apps are more likely to attract more users.
# 
# The goal of this project is to increase revenue by identifying the most profitable apps.

# In[2]:


fileApple = open('C:\\Users\\eliza\\OneDrive\\Documents\\Grayce\\Training\\Guided_Project1\\AppleStore.csv', encoding="utf8")
fileGoogle = open('C:\\Users\\eliza\\OneDrive\\Documents\\Grayce\\Training\\Guided_Project1\\googleplaystore.csv', encoding="utf8")
from csv import reader
read_file_Apple = reader(fileApple)
read_file_Google = reader(fileGoogle)
Apple_data = list(read_file_Apple)
Google_data = list(read_file_Google)
print(Google_data)

#removing the header
Apple_ds = Apple_data[1:]
Google_ds = Google_data[1:]


# Explore dataset function

# In[3]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


# In[6]:


explore_data(Apple_ds, 0, 4)


# In[8]:


explore_data(Apple_ds, 0, 4, True)


# In[10]:


explore_data(Google_ds, 0, 4, True)


# In[3]:


Apple_data[0]


# In[4]:


Google_data[0]


# # Columns and rows in datasets
# 
# | Apple Dataset   | Google Dataset |
# | --------------- | -------------- |
# | id              | App            |
# | track_name      | Category       |
# | size_bytes      | Rating         |
# | currency        | Reviews        |
# | price           | Size           |
# | rating_count_tot| Installs       |
# | rating_count_ver| Type           |
# | user_rating     | Price          |
# | user_rating_ver | Content Rating |
# | ver             | Genres         |
# | cont_rating     | Last Updated   |
# | prime_genre     | Current Ver    |
# | sup_devices.num | Android Ver    |
# | ipadSc_urls.num |                |
# | lang.num        |                |
# | vpp_lic         |                |
# 
# # Documentation
# 
# Apple Data set [Link](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) 
# 
# Google Data set [link](https://www.kaggle.com/lava18/google-play-store-apps)

# In[ ]:


# data cleaning


# In[5]:


# delete inaccurate data, delete duplicate data, remove non-English apps, remove apps that aren't free


# In[6]:


# Google Play data set


# In[8]:


print(Google_ds[10472]) # incorrect entry


# In[10]:


print(Google_ds[10471])


# In[11]:


print(Google_ds[10473])


# In[13]:


# deleting row 10472 as it's incorrect


# In[16]:


# del Google_ds[10472]


# In[19]:


# removing duplicate entries


# In[ ]:


# finding duplicate entries in Google store


# In[20]:


duplicate_apps = []
unique_apps = []

for app in Google_ds:
    name = app[0] #App
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
    
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])


# removing duplicate app rows based on ratings - keep apps with higher ratings - more reliable

# In[ ]:


# build dictionary for highest number of reviews


# In[48]:


reviews_max = {} # creating empty dictionary to store max number of reviews per app


# In[56]:


for app in Google_ds:
    name = app[0]
    n_reviews = float(app[3])
    if (name in reviews_max) and (reviews_max[name] < n_reviews): 
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews
        
print(len(reviews_max))


# In[58]:


# removing duplicates 
android_clean = [] # stores newly cleaned data set
already_added = [] # stores app names

# looping through data set
for app in Google_ds:
    name = app[0]
    n_reviews = float(app[3])
    if n_reviews == reviews_max[name] and name not in already_added:
        android_clean.append(app)
        already_added.append(name)
print(len(android_clean))


# In[ ]:


# finding duplicate entries in Apple store


# In[34]:


duplicate_apps = []
unique_apps = []

index = 0
duplicate_apps_index = []

for app in Apple_ds:
    index += 1
    name = app[1] #track name
    if name in unique_apps:
        duplicate_apps.append(name)
        duplicate_apps_index.append(index)
    else:
        unique_apps.append(name)
    
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])
print(duplicate_apps_index)


# In[47]:


print(Apple_ds[2948]) # Mannequin Challenge
print(Apple_ds[4463]) # Mannequin Challenge
#print(Apple_ds[5277]) # Mannequin Challenge Maker
print('\n')
#print(Apple_ds[1839]) # VR Roller Coaster
#print(Apple_ds[3693]) # VR Roller Coaster
print(Apple_ds[4442]) # VR Roller Coaster
#print(Apple_ds[4623]) # VR Roller Coaster
#print(Apple_ds[4716]) # VR Roller Coaster
print(Apple_ds[4831]) # VR Roller Coaster
#print(Apple_ds[5718]) # VR Roller Coaster

# these are not duplicates


# In[ ]:


# Apple data set


# Removing non-English apps

# In[59]:


def IsEnglishLanguage(app_name):
    for character in app_name:
        if ord(character) > 127: # character number
            return False
    return True


# In[63]:


# checking examples
IsEnglishLanguage('Instagram')
IsEnglishLanguage('爱奇艺PPS -《欢乐颂2》电视剧热播')
IsEnglishLanguage('Docs To Go™ Free Office Suite') # is English language but returning false
IsEnglishLanguage('Instachat 😜') # is English language but returning false


# In[73]:


def IsEnglishLanguageUpdated(app_name): # function for if more than three characters fall out of > 127
    no_characs = 0
    for character in app_name:
        if ord(character) > 127: # character number
            no_characs += 1
            if no_characs > 3:
                return False
    return True


# In[74]:


# checking examples
IsEnglishLanguageUpdated('Instagram')
IsEnglishLanguageUpdated('爱奇艺PPS -《欢乐颂2》电视剧热播')
IsEnglishLanguageUpdated('Docs To Go™ Free Office Suite') # is English language but returning false
IsEnglishLanguageUpdated('Instachat 😜') # is English language but returning false


# # Updating data sets

# In[76]:


Apple_ds_English = []
Google_ds_English = []
for row in Apple_ds:
    name = row[1]
    if IsEnglishLanguageUpdated(name):
        Apple_ds_English.append(row)
    
for row in android_clean:
    name = row[0]
    if IsEnglishLanguageUpdated(name):
        Google_ds_English.append(row)
        
print(len(Apple_ds_English))
print(len(Google_ds_English))


# # Isolating free apps

# In[84]:


Apple_free = []
Google_free = []

for row in Apple_ds_English:
    price = row[4]
    if price == '0.0':
        Apple_free.append(row)
        
for row in Google_ds_English:
    price = row[7]
    if price == '0':
        Google_free.append(row)
    
print(len(Apple_free))
print(len(Google_free))

#price index 4 in apple
#price index 7 in google


# Have finished cleaning apps

# # Analysis
# 
# Our goal is to place the app on the Google Play store to start with. If it gets a good user response we'll develop it further. If it's profitable after 6 months we'll build an Apple version and add it to the Apple store.
# 
# We would like to find an app that is profitable on both markets.

# # Most Common Genres For Both Stores

# In[85]:


# apple use index 11 "prime_genre"
# Google use index 9 "Genres" and index 1 "Category"


# In[87]:


Google_free[0]


# # Frequency Tables

# In[97]:


def freq_table(dataset, index):
    ratings = {}
    total = 0
    for row in dataset:
        total += 1
        variable = row[index]
        if variable in ratings:
            ratings[variable] += 1
        else:
            ratings[variable] = 1
            
    # expressing frequencies as percentages
    percentages = {}
    for i in ratings:
        ratings[i] /=total # divide by total number of apps
        ratings[i] *= 100 # multiply by 100
        ratings[i] = round(ratings[i], 2) # displaying to 2d.p.
       
    
    print(ratings)


# In[105]:


def freq_table1(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    #table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages


# In[107]:


freq_table(Apple_free, 11)


# In[106]:


freq_table1(Apple_free, 11)


# In[92]:


freq_table(Google_free, 1)


# In[93]:


freq_table(Google_free, 9)


# # Display table from most common to least common

# In[108]:


def display_table(dataset, index):
    table = freq_table1(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


# In[109]:


display_table(Apple_free, 11)


# For the Apple apps Games are the most common genre at 58.2% and Entertainment are the second most common genre at 7.88%
# 
# Market is dominated by fun apps rather than practical apps.

# In[110]:


display_table(Google_free, 1)


# In[111]:


display_table(Google_free, 9)


# Family and tools apps are the most common in the Google Store. The Google Store has a higher percentage of practical apps and less fun apps as a proportion.

# # Average number of installs per app genre

# In[119]:


Apple_genre = freq_table1(Apple_free, 11)
for genre in Apple_genre:
    total = 0
    len_genre = 0
    for app in Apple_free:
        genre_app = app[11]
        #print(genre_app)
        if genre_app == genre:
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
            #print(len_genre)
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)


# In[123]:


# perhaps make an app that is popular but not too popular so it would stand out - perhaps a Health & Fitness App
for app in Apple_free:
    if app[11] == 'Health & Fitness':
        print(app[1], ':', app[5])


# In[121]:


Google_genre = freq_table1(Google_free, 1)
for category in Google_genre:
    total = 0
    len_category = 0
    for app in Google_free:
        category_app = app[1]
        if category_app == category:
            n_installs = app[5]
            # removing + and , characters
            n_installs = n_installs.replace('+','')
            n_installs = n_installs.replace(',','')
            # converting the string to a float
            n_installs = float(n_installs)
            total += n_installs
            len_category += 1
    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)


# In[126]:


for app in Google_free:
    if app[1] == 'HEALTH_AND_FITNESS':
        print(app[0], ':', app[5])


# In[ ]:


# maybe do a weight loss app but combine with another popular area like communication and social networking as this is popular in both. 

