#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

def before_all(context):
	# for selenium server standalone
    desired_caps = {}
    desired_caps['platform'] = 'WINDOWS'
    desired_caps['browserName'] = 'chrome'
    context.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
    context.driver.implicitly_wait(10)
    
    # for local driver
    #context.driver = webdriver.Firefox()
    #context.driver.implicitly_wait(10)
   
def after_all(context):
    context.driver.quit()