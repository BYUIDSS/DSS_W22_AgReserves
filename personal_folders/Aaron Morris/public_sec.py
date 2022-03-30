# %%
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import lxml.html as lh
import requests


# %%
# highlight function
def highlight(element):

    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    sleep(2)
    apply_style(original_style)

# %%
url = "http://ir.farmlandpartners.com/sec-filings/Docs/default.aspx"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()

# %%
sleep(2)
driver.find_element_by_xpath('//*[@id="filtertypeDropdown"]').click()
driver.find_element_by_xpath('//*[@id="filtertypeDropdown"]/option[3]').click()
sleep(2)

# %%
sleep(2)
driver.find_element_by_xpath('//*[@id="docsPanelResults"]/table/tbody/tr[1]/td[1]/a').click()
driver.find_element_by_xpath('//*[@id="_ctrl0_ctl47_hrefItemXBRLHTMLDownload"]').click()

# %%
handles = driver.window_handles
window1 = handles[0]
window2 = handles[1]
driver.switch_to.window(window2)

# %%

# consolidated balance sheet 
 
sleep(2)
driver.find_element_by_xpath('//*[@id="statementsAnchor"]').click()
driver.find_element_by_xpath('//*[@id="statementsMenu"]/div/ul/li[1]/a').click()
#table1 = driver.find_element_by_xpath('//*[@id="idm140656664396024"]')
url1 = driver.current_url
page = requests.get(url1)
soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find('table', id = 'idm140656664396024')
headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)
balance_sheet = pd.DataFrame(columns = headers)
for i in table1.find_all('tr')[1:]:
    row_data = i.find_all('td')
    row = [j.text for j in row_data]
    length = len(balance_sheet)
    balance_sheet.loc[length] = row

balance_sheet.to_csv('farmland_balance_sheet.csv')

# %%

# acre perecentages

# driver.find_element_by_xpath('//*[@id="disclosuresTablesAnchor"]').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="disclosuresTablesMenu"]/div/ul/li[3]/a').click()
# url2 = driver.current_url
# page = requests.get(url2)
# soup = BeautifulSoup(page.text, 'lxml')
# table2 = soup.find('table', style = 'border-collapse:collapse;font-size:16pt;height:max-content;padding-left:0pt;padding-right:0pt;width:100%;')
# headers2 = []
# for i in table2.find_all('th'):
#     title = i.text
#     headers.append(title)

# acre_percent = pd.DataFrame(columns = headers2)
# for i in table2.find_all('tr')[1:]:
#     row_data = i.find_all('td')
#     row = [j.text for j in row_data]
#     length = len(acre_percent)
#     acre_percent.loc[length] = row




