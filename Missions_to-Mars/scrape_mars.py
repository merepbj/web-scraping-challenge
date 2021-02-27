#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from splinter import Browser
import time
browser = Browser('chrome','chromedriver')

def scrape(): 
    title, paragraph = mars_news(browser)
   
    data = {
        "news_title": title, 
        "news_paragraph": paragraph,
        "news_image": mars_images(browser),
        "news_facts": mars_facts(),
        "news_hemisphere": mars_hemisphere(browser)
    }
    return data


# In[2]:


# ### NASA Mars News
# 
# * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[3]:

def mars_news(browser): 

    browser.visit('https://mars.nasa.gov/news/')
    title = browser.find_by_css('div.content_title a').text
    paragraph = browser.find_by_css('div.article_teaser_body').text
    return title, paragraph
    

# ### JPL Mars Space Images - Featured Image
# 
# * Visit the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).
# 
# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# 
# * Make sure to find the image url to the full size `.jpg` image.
# 
# * Make sure to save a complete url string for this image.

# In[4]:

def mars_images(browser):

    browser.visit('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html')
    browser.links.find_by_partial_text('FULL IMAGE').click()
    image = browser.find_by_css('img.fancybox-image')['src']
    return image

# ### Mars Facts
# 
# * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# 
# * Use Pandas to convert the data to a HTML table string.

# In[5]:

def mars_facts():
    return pd.read_html('https://space-facts.com/mars/')[0].to_html(classes='table table-stripped')


# ### Mars Hemispheres
# 
# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
# 
# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# 
# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# In[6]:

def mars_hemisphere(browser):
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')


    # In[7]:


    links = browser.find_by_css('a.itemLink h3')


    # In[8]:


    hemispheres = []
    for i in range(len(links)):
        hemisphere = {}
        
        hemisphere['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)
        browser.back()
    browser.quit()
    return hemispheres


# In[ ]:




