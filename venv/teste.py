import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

#variáveis
url = 'https://www.basketball-reference.com/contracts/GSW.html'
option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)

driver.get(url)
element = driver.find_element_by_xpath('//*[@id="div_contracts"]')
content = element.get_attribute('outerHTML')

html = bs(content, 'html.parser')
table = html.find(name='table')


print(table)



#driver.quit()

#//div[@class='table_container is_setup']//table//thead//tr//th
