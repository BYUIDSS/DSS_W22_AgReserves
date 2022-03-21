# %%
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup


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
sleep(2)
driver.find_element_by_xpath('//*[@id="statementsAnchor"]').click()
driver.find_element_by_xpath('//*[@id="statementsMenu"]/div/ul/li[1]/a').click()
html = driver.page_source
soup = BeautifulSoup(html)
tables = soup.find_all('table')
df = pd.read_html(str(tables))[0]







