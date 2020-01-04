#!/usr/bin/env python
# coding: utf-8

# In[46]:


# Dependencies
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests


# In[47]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[48]:


# Go to url
url = 'https://mars.nasa.gov/news'
browser.visit(url)


# In[49]:


# Iterate through all pages
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve first element that contain title information
    news_title = soup.find('div', class_='content_title').get_text()
    # Retrieve first element that contains paragraph text
    # news_p = soup.find('div', class_= "article teaser body").get_text()


# In[50]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[51]:


news_title = "NASA Updates Mars 2020 Mission Environmental Review"
news_p = "NASA and the Department of Energy have completed a more detailed risk analysis for the Mars 2020 rover launch from Florida"


# In[52]:


# Use the parent element to find the first 'a' tag and save it as `news_title`
slide_elem = soup.select_one('ul.item_list li.slide')

news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# ## JPL Mars Space Images - Featured Image

# In[53]:


# Go to url
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[54]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[55]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()


# In[56]:


# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[57]:


#Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# ## Mars Weather

# In[58]:


# Go to url
twit_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(twit_url)


# In[59]:


# Parse with Beautiful Soup
html = browser.html
soup = BeautifulSoup(html,'html.parser')


# In[60]:


# Find tweet
mars_weather = soup.find('div', class_='js-tweet-text-container').find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.split('pic')[0] 
mars_weather


# ## Mars Facts

# In[ ]:


# Go to url
url = 'https://space-facts.com/mars/'


# In[ ]:


# Use pandas to import data
facts = pd.read_html(url)
facts


# In[ ]:


# Use pandas to convert HTML to dataframe
facts_df = facts[0]
facts_df


# In[ ]:


# Use pandas to convert df to a HTML table string
mars_facts = facts_df.to_html()
print(mars_facts)


# ## Mars Hemispheres

# In[25]:


# Go to url
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[26]:


# Parse with Beautiful Soup
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[44]:


# Get hemisphere title
search = soup.find('div', id='product-section')
#title = search.find_all('div', class_= 'item')
for heading in soup.find_all("h3"):
    print(heading.text.strip())


# In[45]:


image = soup.find('div', class_='item')
for link in soup.find_all("a", "href"):
    print(link.text.strip())


# In[ ]:


# For loop
# Empty list
hemispheres = []
# Save urls
title = 
# Iterate through images
browser.find_by('a.product-item')
# Return to top of list
browser.back()
hemisphere_urls.append{"title":title, "image":image}


# In[ ]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]


# In[ ]:


# Convert notebook into Python script

