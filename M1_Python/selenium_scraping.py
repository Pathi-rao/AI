from selenium import webdriver

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.bodylab24.de/100-whey-gold-standard-908g.html")

#driver.close() #closes the tab
#driver.quit() #closes the browser
print(driver.title)

content = driver.find_element_by_id("pdp-content-nutrition")
print(content)

driver.quit()