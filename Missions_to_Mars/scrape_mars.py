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


def scrape_info():
    browser = init_browser()

 # Go to website
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    time.sleep(1)  
    
    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

# Iterate through all pages
# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve first element that contain title information
news_title = soup.find("li", class_="slide").find('div', class_='content_title').text
#print(news_title)

# Retrieve first element that contains paragraph text
news_p = soup.find("li", class_="slide").find('div', class_= "article_teaser_body").text
#print(news_p)


# In[5]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[6]:


news_title = "NASA Updates Mars 2020 Mission Environmental Review"
news_p = "NASA and the Department of Energy have completed a more detailed risk analysis for the Mars 2020 rover launch from Florida"


# In[7]:


# Use the parent element to find the first 'a' tag and save it as `news_title`
slide_elem = soup.select_one('ul.item_list li.slide')

news_title = slide_elem.find("div", class_='content_title').text
news_title
news_p = soup.find("li", class_="slide").find('div', class_= "article_teaser_body").text
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


# Mars Facts



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


# Mars Hemispheres


# Go to url
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# HTML Object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Create empty list to store info
mars_hemispheres = []

  # Retrieve the parent divs for all articles
results = soup.find("div", class_ = "result-list")
hemispheres = results.find_all("div", class_="item")  

# Create empty list to store info
mars_hemispheres = []

  # Retrieve the parent divs for all articles
results = soup.find("div", class_ = "result-list")
hemispheres = results.find_all("div", class_="item")  

# Loop through results to retrieve hemisphere title and full image
for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    
    # Save base url
    base_url = 'https://astrogeology.usgs.gov'
    
    # Iterate through images
    browser.find_by_id('a.product-item')
    full_image = hemisphere.find("a")["href"]
    image = base_url + full_image
    
    mars_hemispheres.append({"title":title, "image":image}) 
   
 # Return results
print(mars_hemispheres) 
