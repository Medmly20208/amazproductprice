from selenium import webdriver
from time import sleep as sp

path = "C:\Program Files (x86)\chromedriver.exe"
print("give a product name to get its price in amazon")
d = input("=========>")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browse = webdriver.Chrome(executable_path=path, options=options)
browse.set_window_position(0, 0)
browse.set_window_size(1550,1080)
browse.get("https://amazon.com")
sp(5)
browse.find_element_by_id("twotabsearchtextbox").send_keys(d)
sp(5)
browse.find_element_by_id("nav-search-submit-button").click()
sp(5)
browse.find_element_by_css_selector(".a-section.aok-relative.s-image-fixed-height").click()
sp(5)
price = browse.find_element_by_xpath('//*[@id="price_inside_buybox"]')
print("the price of "+d+" is :")
print("======================>"+price.text)
sp(1)
browse.quit()
