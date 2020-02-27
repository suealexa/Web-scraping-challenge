#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[3]:


# Go to url
url = 'https://mars.nasa.gov/news'
browser.visit(url)


# In[4]:


# Iterate through all pages
# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# Retrieve first element that contain title information
news_title = soup.find('div', class_='content_title').get_text()
# Retrieve first element that contains paragraph text
# news_p = soup.find('div', class_= "article teaser body").get_text()


# In[5]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[6]:


news_title = "NASA Updates Mars 2020 Mission Environmental Review"
news_p = "NASA and the Department of Energy have completed a more detailed risk analysis for the Mars 2020 rover launch from Florida"


# In[7]:


# Use the parent element to find the first 'a' tag and save it as `news_title`
slide_elem = soup.select_one('ul.item_list li.slide')

news_title = slide_elem.find("div", class_='content_title').get_text()
news_title
news_paragraph = slide_elem.find("div", class_="article_teaser_body").get_text()
print(news_paragraph)


# ## JPL Mars Space Images - Featured Image

# In[8]:


# Go to url
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[10]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[12]:


#Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# ## Mars Weather

# In[13]:


# Go to url
twit_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(twit_url)


# In[14]:


# Parse with Beautiful Soup
html = browser.html
soup = BeautifulSoup(html,'html.parser')


# In[15]:


# Find tweet
#mars_weather = soup.find('div', class_='js-tweet-text-container').find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.split('pic')[0] 
#temp = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

mars_weather


# ## Mars Facts

# In[16]:


# Go to url
url = 'https://space-facts.com/mars/'


# In[17]:


# Use pandas to import data
facts = pd.read_html(url)
facts


# In[18]:


# Use pandas to convert HTML to dataframe
facts_df = facts[0]
facts_df


# In[19]:


# Use pandas to convert df to a HTML table string
mars_facts = facts_df.to_html()
print(mars_facts)


# ## Mars Hemispheres

# In[20]:


# Go to url
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[21]:


# HTML Object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[22]:


# Get hemisphere title
search = soup.find('div', id='product-section')

for heading in soup.find_all("h3"):
    print(heading.text.strip())


# In[23]:


image = soup.find('div', class_='item')
for link in soup.find_all("a", "href"):
   print(link.text.strip())


# In[24]:


# For loop
for i in search:
# Empty list
    mars_hemispheres = []
# Get titles 
    title = search.find_all('div', class_= 'item')  
# Save url
    url = 'https://astrogeology.usgs.gov'
# Iterate through images
    browser.find_by_id('a.product-item')
#Store data in dictionary   
    mars_hemispheres.append({"title":title, "image":image})
# Return results
    return mars_hemispheres    
# Return to top of list    
    browser.back()

# In[ ]:


# Convert notebook into Python script


# In[26]:


# Close the browser after scraping
browser.quit()


# In[ ]:
