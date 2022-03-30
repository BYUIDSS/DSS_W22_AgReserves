# %%
from asyncio import subprocess
import pandas as pd
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import os
# %%

# navigate to property list 
url = "http://www.farmlandpartners.com/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()
sleep(1)
driver.find_element_by_xpath('//*[@id="menu-item-26"]/a').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="listing"]').click()

# %%

# scrape property table 

html = driver.page_source
soup = BeautifulSoup(html)
table = soup.find_all('table')

dat = pd.read_html(str(table))[0]

dat.to_csv('farmland_acres.csv')

driver.close()
# %%
rscript_path = os.getcwd() + "/" + "farmland_acre_clean.R"
executable_path = "/Library/Frameworks/R.framework/Versions/4.0/Resources/Rscript"
arg = "--vanilla"
cmd = [executable_path, arg, rscript_path]
subprocess.check_output(cmd)
# %%
