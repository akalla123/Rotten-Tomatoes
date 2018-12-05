
# coding: utf-8

# In[7]:


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from bs4 import BeautifulSoup


#make browser
ua=UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

all_movie = 'https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=100&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=2&sortBy=release'
driver.get(all_movie)

webLink = 'https://www.rottentomatoes.com'

movies = set()

#genre = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="genre-dropdown"]/div/div/div[1]/span')))
#genre.click()

for i in range (0,60):
    try:
        #print(movies)
        showMoreButton = WebDriverWait(driver, 0.01).until(EC.presence_of_element_located((By.XPATH,'//*[@id="show-more-btn"]/button')))
        #click on the showMore Button
        showMoreButton.click()
        print('click: ',i)
    except: None
        #print ('missing show More button')
    
html=driver.page_source# get the html
soup = BeautifulSoup(html, "lxml") # parse the html 
all_movies=soup.findAll('div', {'class':re.compile('movie_info')}) # get all the review divs
        
for x in all_movies:
    link=x.find('a',{'href':re.compile('/m/')})
    movLink = webLink + str(link).split('"')[1]
    #print(movLink)
    movies.add(str(movLink))    #creating the distinct list of movies
            
#writing the set entries to movie file
try:
    fw=open('animation.txt','w') # output file
    
    for x in movies:
        fw.write(x +"\n")
        
    fw.close()
except:
    print("Error while trying to create movie_link.txt file")

