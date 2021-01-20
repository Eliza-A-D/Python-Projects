#!/usr/bin/env python
# coding: utf-8

# # Exploring Hacker News Posts
# The data set describes user-submitted posts to the site Hacker News. 
# 
# I will be analysing the data set to answer two key questions:
# 
# - Which has more user response: `Ask HN` or `Show HN`?
# - Does the time of day of post influence user interaction with the post?
# 
# The columns in the dataset are:
# 
# |Index|Column name|Description|
# |:----|:----|:----|
# |0|`id`|The unique identifer from Hacker News for the post|
# |1|`title`|Post title|
# |2|`url`|URL for post, if any|
# |3|`num_points`|Number of points the post acquired. Calculated as total number of upvotes minus total number of downvotes|
# |4|`num_comments`|Number of comments on post|
# |5|`author`|Username for the person who submitted the post|
# |6|`created_at`|Date and time of post submission (in the eastern US timezone)|
# 

# In[45]:


HN_Posts = open('C:\\Users\\eliza\\OneDrive\\Documents\\Grayce\\Training\\Guided_Project2\\HN_posts_year_to_Sep_26_2016.csv', encoding="utf8")
from csv import reader
read_file = reader(HN_Posts)
hn = list(read_file)

# removing the header
headers = hn[0]
HN_ds = hn[1:]

# printing the first five rows including the header
print(hn[:5])

# printing headers and data separately
print(headers)
print(HN_ds)

#print(len(hn))


# Filtering data

# Creating list for data containing `Ask HN` and `Show HN`

# In[42]:


# Creating empty lists
ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    
    # Assigning to lists
    #if (title.lower()).startswith('ask hn'):
    if title.startswith('Ask HN'):
        ask_posts.append(row)
    #elif (title.lower()).startswith('show hn'):
    elif title.startswith('Show HN'):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
# Checking number of posts in each list
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# # Finding total number of comments in posts

# In[71]:


total_ask_comments = 0

for row in ask_posts:
    num_comments = int(row[4])
    total_ask_comments += num_comments
    
avg_ask_comments = total_ask_comments / len(ask_posts)

print(avg_ask_comments)


# In[14]:


total_show_comments = 0

for row in show_posts:
    num_comments = int(row[4])
    total_show_comments += num_comments
    
avg_show_comments = total_show_comments / len(show_posts)

print(avg_show_comments)


# On average the ask posts get more user comments than the show posts. The ask posts get an average of 10.4 comments per post, whereas the show posts get an average of 4.89 comments per post.

# So I'll focus the rest of my analysis on ask posts!

# # Finding total number of points in posts

# In[74]:


def avg_number_points(posts):
    total_number_points = 0
    for row in posts:
        num_points = int(row[3])
        total_number_points += num_points
    avg_num_points = total_number_points / len(posts)
    return avg_num_points    


# In[76]:


avg_number_points(ask_posts)


# In[77]:


avg_number_points(show_posts)


# The `Ask HN` posts have a higher average number of points at 14.9, whereas the `Show HN` are at 11.3.

# I ask the question: do ask posts created at a certain time attract more comments or more points?

# In[94]:


# Looking at comments per hour
import datetime as dt

result_list = []
for row in ask_posts:
    created_at = row[6]
    num_comments = int(row[4])
    num_points = int(row[3])
    result_list.append([created_at, num_comments, num_points])


# In[95]:


counts_by_hour = {}
comments_by_hour = {}
points_by_hour = {}

#print(result_list[0])

#print(result_list[0][0])

#print(dt.datetime.strptime(result_list[0][0], "%m/%d/%Y %H:%M"))

for row in result_list:
    time = dt.datetime.strptime(row[0], "%m/%d/%Y %H:%M")
    hour = time.strftime('%H')
    
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = row[1] # adding comments number
        points_by_hour[hour] = row[2] # adding points
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += row[1] # incrementing by comments number
        points_by_hour[hour] += row[2] # incrementing by points


# Calculating the average number of comments per post for posts created during each hour of the day

# In[96]:


#print(comments_by_hour)
#print(counts_by_hour)

avg_by_hour = []
avg_points_by_hour = []
for i in comments_by_hour:
    hour = i
    avg_comments = comments_by_hour[i] / counts_by_hour[i]
    avg_by_hour.append([hour, avg_comments])
    avg_points = points_by_hour[i] / counts_by_hour[i]
    avg_points_by_hour.append([hour, avg_points])
    
print(avg_by_hour) # average comments per hour
print(avg_points_by_hour) # average points per hour


# In[98]:


swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
print(swap_avg_by_hour)



swap_avg_points_by_hour = []
for row in avg_points_by_hour:
    swap_avg_points_by_hour.append([row[1], row[0]])
print(swap_avg_points_by_hour)


# In[100]:


# Returning a sorted function:
sorted_swap = sorted(swap_avg_by_hour, reverse=True) # Showing average number of comments per hour in descending hour
sorted_swap_points = sorted(swap_avg_points_by_hour, reverse=True) # Sorted swap points


# In[50]:


print("Top 5 Hours for Ask Posts Comments")


# In[52]:


print(sorted_swap[:5])


# In[59]:


template = "{hour}:00: {comment_num:.2f} average comments per post"
for row in sorted_swap[:5]:
    update = template.format(hour=row[1],comment_num=row[0])
    print(update)


# In[ ]:


print("Top 5 Hours for Ask Posts Points")


# In[101]:


template = "{hour}:00: {point_num:.2f} average points per post"
for row in sorted_swap_points[:5]:
    update = template.format(hour=row[1],point_num=row[0])
    print(update)


# # Conclusion
# 
# The best hour to post to gain most user interaction would be at 3pm, followed by 1pm. 
# 
# `Ask HN` posts get a higher response than `Show HN` posts.
# 
# The top three hours for the number of average comments per post for `Ask HN` are also the top three hours for the average number of points per post.
