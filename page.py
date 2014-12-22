# -*- coding: utf8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.ch/")
driver.set_window_size(1500, 1000)
driver.find_element(By.XPATH, '//*[@id="gbqfq"]').send_keys("showroomprivee")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="gsr"]').submit()