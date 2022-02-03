
#%%
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#%%
def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)


#%%
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.sec.gov/edgar/search/')
text_bar = driver.find_element_by_id("entity-short-form").send_keys("Gladstone land corp")
driver.find_element_by_id("search").click()

## Need to put a sleep before looking for element

driver.find_element_by_id("category-select").click()
# %%
