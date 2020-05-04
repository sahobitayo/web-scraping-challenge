# Web-scraping-challenge
- [Scraping](https://github.com/sahobitayo/web-scraping-challenge#scraping)
- [MongoDB and Flask Application](https://github.com/sahobitayo/web-scraping-challenge#mongodb-and-flask-application)
- [Tools Used](https://github.com/sahobitayo/web-scraping-challenge#tools-used)


# Mission to Mars
A Flask web application that scrapes various websites for data related to Mars and displays the information in a single HTML page.


## Scraping
The [Jupyter notebook file](https://github.com/sahobitayo/web-scraping-challenge/blob/master/Missions_to_Mars/mission_to_mars.ipynb) contains all of the scraping code for this project. BeautifulSoup, Pandas, and Requests/Splinter were used to scrape the following information about Mars from the following websites:

### [NASA Mars News](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
- Script collects the latest News Title and Paragraph Text.

### [Mars Space Images - Featured Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
- Script finds the image url for the current Featured Mars Image and assigns the url string of the full size image.

### [Mars Weather](https://twitter.com/marswxreport?lang=en)
- Script visits the Mars Weather twitter account and scrapes the latest Mars weather tweet.

### [Mars Facts](https://space-facts.com/mars/)
-Script visit the Mars Facts webpage and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Then, used Pandas to convert the data to a HTML table string

### [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
- Script visits the USGS Astrogeology site and obtains the full resolution images for each of Mar's hemispheres.


## MongoDB and Flask Application
After scraping the various sites for the information needed for the project, I used MongoDB with Flask  to create a new HTML page that displays all of the information that was scraped from the URLs above. The following steps were taken:

1. Convert the jupyter notebook into a python script using ``` jupyter nbconvert --to script mission_to_mars.ipynb``` then changed the name of the file to scrape.py. In this file, there is a function called scrape which executes all the scraping code and returns one python dictionary conting the scraped data.
2. Create a route called /scrape, which imports the [scrape.py](https://github.com/sahobitayo/web-scraping-challenge/blob/master/Missions_to_Mars/scrape_mars.py) script.
3. Create a route /, which queries the Mongo database and passes the mars data into an HTML template to display the data.
4. Create a template HTML file, [index.html](https://github.com/sahobitayo/web-scraping-challenge/blob/master/Missions_to_Mars/templates/index.html) that takes the mars data dictionary and displays all of the data in the appropriate HTML elements.


## Tools Used
- **Splinter/Requests**
- **Pandas**
- **Flask**
- **Beautiful Soup**
- **Jupyter Notebook**
- **Python**
- **MongoDB**
- **HTML**





