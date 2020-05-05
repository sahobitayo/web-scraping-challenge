#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import BeautifulSoup
from bs4 import BeautifulSoup as bs
import os
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import time
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


##Check path of the chromedriver
#!which chromedriver


# In[3]:


# executable_path = {"executable_path": "chromedriver.exe"}

# def init_browser():
#     executable_path = {"executable_path": "chromedriver.exe"}
#     return Browser("chrome", **executable_path, headless=False)


def scrape():

    # Assign path for chromedriver
    executable_path = {'executable_path': '/c/Program Files/Chrome_extension/chromedriver'}
    browser = Browser('chrome')


    # In[ ]:


    # selenium==3.5.0
    # splinter==0.7.6

    # URL of the website being scraped
    url= 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[ ]:


    # Retrieve page with the requests module
    # response = requests.get(url)

    # Wait for 5 seconds
    time.sleep(5)

    html= browser.html


    # In[ ]:


    # Create BeautifulSoup object; parse with 'html.parser'
    # soup = bs(response.text, 'html.parser')
    soup = bs(html, 'html.parser')


    # In[ ]:


    # Examine the results, then determine element that contains sought info
    # print(soup.prettify())


    # In[ ]:


    # results are returned as an iterable list
    # news_title = soup.find_all('div', class_="content_title")
    # print(news_title)


    # In[ ]:


    # Print and choose which news title you want to access and get the latest title
    latest_news_title = soup.find_all('div', class_="content_title")[1].text
    print(latest_news_title)


    # In[ ]:


    # news_paragraph= soup.find_all('div', class_="content_title")
    # print(news_paragraph)


    # In[ ]:


    # Print and choose which news paragraph you want to access and get the latest news paragraph
    latest_news_paragraph= soup.find_all('div', class_="article_teaser_body")[0].text
    print(latest_news_paragraph)


    # In[11]:


    # URL of the website being scraped
    url_2= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)
    # Wait for 5 seconds
    time.sleep(5)

    html_2= browser.html
    # Create BeautifulSoup object; parse with 'html.parser'

    soup = bs(html_2, 'html.parser')
    # Examine the results, then determine element that contains sought info
    # print(soup.prettify())


    # In[12]:


    # Get image url for featured image.
    base_url = "https://www.jpl.nasa.gov"
    featured_image_url= soup.find('li', class_='slide').a['data-fancybox-href']
    featured_image_url= base_url + featured_image_url
    print(f"Featured image url: {featured_image_url}")


    # In[11]:


    # URL of the website being scraped
    url_5= "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_5)
    # Wait for 10 seconds
    time.sleep(5)

    html_5= browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html_5, 'html.parser')

    ##First Method that worked
    # tweet= soup.find('article', class_= 'css-1dbjc4n')
    # mars= tweet.find_all('span', class_= 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    ## Grab text of most recent tweet
    # mars1= mars[-3]
    # print(mars1.text)


    #Easier Way
    # Search for most recent tweet
    tweet= soup.find_all('div', attrs={"lang":"en", "dir":"auto", "class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
    tweet= tweet[-2].text
    print(tweet)


    # In[ ]:


    # URL of the website being scraped
    url_3= 'https://space-facts.com/mars/'
    browser.visit(url_3)
    # Wait for 5 seconds
    time.sleep(5)

    html_3= browser.html
    # Create BeautifulSoup object; parse with 'html.parser'

    soup = bs(html_3, 'html.parser')
    # Examine the results, then determine element that contains sought info
    # print(soup.prettify())


    # In[ ]:


    # Get the table being scraped
    tables= pd.read_html(url_3)
    print(tables)


    # In[ ]:


    df= tables[0]
    df.columns = ["Measurement", "Value"]
    df.set_index("Measurement", inplace=True)
    df.head()


    # In[ ]:


    # Convert DataFrame to HTML
    # html_table= df.to_html("templates/mars_facts_table.html")
    html_table = df.to_html()
    print(html_table)


    # In[ ]:


    # URL of the website being scraped
    url_4= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_4)
    # Wait for 5 seconds
    time.sleep(5)

    html_4= browser.html
    # Create BeautifulSoup object; parse with 'html.parser'

    soup = bs(html_4, 'html.parser')

    # Examine the results, then determine element that contains sought info
    # print(soup.prettify())


    # In[ ]:


    # Get hemisphere name and image url for the full resolution image.
    hemispheres = soup.find_all('div', class_='item')
    hemisphere_image_urls = []

    for hemisphere in hemispheres:
        text = hemisphere.find('h3').text
    #     split_text = text.split('Enhanced')
    #     title = split_text[0]
        title= text
        browser.click_link_by_partial_text(text)
        hemisphere_page_html = browser.html
        soup = bs(hemisphere_page_html, "html.parser")
        downloads = soup.find('div', class_="downloads")
        img_url = downloads.a["href"]
        hemisphere_dict = { 
            "title": title, 
            "img_url": img_url
        }
        hemisphere_image_urls.append(hemisphere_dict)
        browser.back()
        
    print(hemisphere_image_urls)

    scraped_data = {
        "news_title": latest_news_title,
        "news_p": latest_news_paragraph,
        "hemisphere_image_urls": hemisphere_image_urls,
        "html_table": html_table,
        "mars_weather": tweet,
        "featured_image_url": featured_image_url
    }
    print(scraped_data)
    browser.quit()
    return scraped_data

# In[ ]:




