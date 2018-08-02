

# coding: utf-8

# # Part 1

# NASA Mars News

# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
import pymongo
import os

def scrape():

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    response = requests.get(url)
    print(response)

    soup = bs(response.text, 'html.parser')
    print(soup.prettify())

    results = soup.find_all('div', class_='content_title')
    print(results)

    news_title = []

    for title in results:
        if(title.a):
            if(title.a.text):
                news_title.append(title.a.text.strip())
    print(news_title)

    for x in range(len(news_title)):
        print(news_title[x])

    soup = bs(response.text, 'html.parser')
    print(soup.prettify())

    text_results = soup.find_all('div', class_='rollover_description_inner')
    print(text_results)

    news_p = []

    for words in text_results:
            if(words.text):
                news_p.append(words.text.strip())
    print(news_p)

    for x in range(len(news_p)):
        print(news_p[x])


    # # JPL Mars Space Images - Featured Image

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('FULL IMAGE')

    time.sleep(5)

    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    result = soup.find('figure', class_='lede')

    featured_image_url = "https://www.jpl.nasa.gov" + str(result.find('a')['href'])

    print(featured_image_url)


    # # Mars Weather

    url = 'https://twitter.com/marswxreport?lang=en'

    response = requests.get(url)
    print(response)

    soup = bs(response.text, 'html.parser')
    print(soup.prettify())

    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)

    weather_html = browser.html
    weather_soup = bs(weather_html, 'html.parser')

    twitter_results = weather_soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

    # print(twitter_results)
    mars_weather = []
    for twitter in twitter_results:
        if "Sol" in str(twitter):
            mars_weather.append(twitter.text)

    mars_weather[0]
            
    # # Mars Facts

    url = "https://space-facts.com/mars/"

    tables = pd.read_html(url)

    #Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

    df = tables[0]
    df.columns = ['Label', "Values"]
    df.head()

    # Use Pandas to convert the data to a HTML table string.

    html_table = df.to_html(header=False, index=False)
    html_table

    # # Mars Hemispheres

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    response = requests.get(url)
    print(response)

    soup = bs(response.text, 'html.parser')
    print(soup.prettify())

    hem_results = soup.find_all('a', class_='itemLink product-item')
    hem_results

    links = []

    for title in hem_results:
        if(title.h3):
            if(title.h3.text):
                links.append(title.h3.text)
    print(links)

    hemisphere_image_urls = []

    for x in range(len(links)):
        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)

        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        browser.click_link_by_partial_text(links[x])
        title = links[x][0:-9]

        images_html = browser.html
        images_soup = bs(images_html, "html.parser")
        img_url = images_soup.find('div', class_='downloads').find('li').a['href']

        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = img_url
        
        hemisphere_image_urls.append(image_dict)

    hemisphere_image_urls

    data = {
    "id": 1,
    "news_title": news_title[0],
    "news_p": news_p[0],
    "featured_image_url": featured_image_url,
    "mars_weather": mars_weather[0],
    "fact_table": html_table,
    "hemisphere_image_urls": hemisphere_image_urls
    }

    return data

