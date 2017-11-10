#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Base(unittest.TestCase):
    #initialize webdriver and inherit metods from unittest
    def __init__(self, driver):
        super(Base, self).__init__()
        self.driver = driver
    #global method - find and return element if this element is visible
    def findVisibleElement(self, locator):
        element = WebDriverWait(self.driver, 10).\
            until(expected_conditions.visibility_of_element_located(locator))
        return element    
    #global method - find and return element if this element is present in DOM
    def findElement(self, locator):
        element = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_element_located(locator))
        return element
    #global method - find and return list of elements if this elements is present in DOM
    def findElems(self, locator):
        elements = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_all_elements_located(locator))
        return elements
    #global method - Check text present in element
    def checkTextPresentInElem(self, locator, text):
        WebDriverWait(self.driver,10).\
            until(expected_conditions.\
                text_to_be_present_in_element(locator, text))
    #locators    
    ADRESS = 'https://rozetka.com.ua'
    SEARCH_RESULT_PAGE = 'http://rozetka.com.ua/search/?section_id=80004&section=&text=notebooks&rz-search-button='
    RUBRIC_HEADLINE = (By.TAG_NAME,"h1")
    CATALOG_BUTTON = (By.ID, "fat_menu_btn")
    SEARCH_FIELD_LOCATOR = (By.NAME, 'text')    
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, "div[data-location='searchResults']")
    REQUEST_NOT_FOUND = (By.XPATH, "//*[@id='head_banner_container']/div/div[2]/div[3]/div/p[2]")
    BY_BUTTONS_LOCATOR = (By.NAME, "buy_search")
    CHECKBOX_ASUS = (By.CSS_SELECTOR, "span.filter-parametrs-i-l-i-text.filter-parametrs-i-l-i-checkbox.sprite-side")
    CHECKOUT_BUTTON = (By.ID,"popup-checkout")
    ITEMS_COUNT = (By.NAME,"quantity")
    EDIT_ORDER_LINK = "edit"
    LOGIN_TEXTBOX = (By.NAME,"login")
    PASSWORD_TEXTBOX = (By.NAME,"password")
    LOGIN_BUTTON = (By.CSS_SELECTOR,"span.btn-link-i")
    ERROR_MESSAGE = (By.XPATH,"//*[@id='auth']/div/div[1]/div")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH,"//*[@id='cart-popup']/div[2]/div[1]/div[3]/span/span/a")
    
                   
class MainPage(Base):
    def search(self, text):
        search_field = self.findElement(self.SEARCH_FIELD_LOCATOR)
        search_field.clear()
        # enter search keyword and submit
        search_field.send_keys(text)
        search_field.submit()
        time.sleep(5)

    def search_catalog(self, text1, text2):
        Elem1 = (By.LINK_TEXT, text1)
        Elem2 = (By.LINK_TEXT, text2)
        # wait for Men menu to appear, then hover it
        men_menu = self.findVisibleElement(Elem1)
        ActionChains(self.driver).move_to_element(men_menu).perform()
        # wait for Fastrack menu item to appear, then click it
        fastrack = self.findVisibleElement(Elem2)
        fastrack.click()
        time.sleep(10)
        
        
class CatalogPage(MainPage):
    #check catalog-requests results
    def assert_page(self, text):
        self.checkTextPresentInElem(self.RUBRIC_HEADLINE, text)
    #search from catalog
    def search_catalog2(self, textarg1, textarg2):
        catalog_btn = self.findVisibleElement(self.CATALOG_BUTTON)
        ActionChains(self.driver).move_to_element(catalog_btn).perform()
        self.search_catalog(textarg1, textarg2)


class ProductsPage(CatalogPage):
    def checkResults(self, query_value):
        if(query_value.isdigit()):
            assert len(self.findElems(self.SEARCH_RESULT_ITEMS)) >= int(query_value)
        else:
            self.checkTextPresentInElem(self.REQUEST_NOT_FOUND, query_value)
    #specified method for only one test cart.feature
    def clickOnCheckBoxAsus(self):
        checkbox_asus = self.findElement(self.CHECKBOX_ASUS)
        checkbox_asus.click()
        WebDriverWait(self.driver, 10).until( \
            lambda el: el.find_element_by_xpath("//*[@id='title_page']/div/div/div[4]/ul/li[2]/a").is_displayed(),\
                'Timeout while we are wait pop-up menu.')

    def chooseProducts(self):
        buyButtons = self.findElems(self.BY_BUTTONS_LOCATOR)
        self.assertEqual(32, len(buyButtons))
        cart = cart_popup(self.driver)
        buyButtons[0].click()
        time.sleep(5) 
        cart.findButtonAndClick(self.CONTINUE_SHOPPING_BUTTON)  
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 3250);")
        buyButtons[31].click() 
        time.sleep(5)   
        cart.findButtonAndClick(self.CHECKOUT_BUTTON)  
        time.sleep(10)


class cart_popup(Base):   
    def findButtonAndClick(self, locat):
        button = self.findVisibleElement(locat)
        button.click()

    def delete_product(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        number_field = WebDriverWait(self.driver, 10).\
            until(expected_conditions.visibility_of_element_located(self.ITEMS_COUNT))
        number_field.clear()
        number_field.send_keys("0", Keys.ENTER)
        time.sleep(5)

    def checkRedirectAfterCleaningTheCart(self):
        WebDriverWait(self.driver,10).\
            until(expected_conditions.\
                text_to_be_present_in_element(self.RUBRIC_HEADLINE,"Вход в интернет-магазин"))


class OrderPage(Base):
    def editMyOrder(self):
        editLink = self.driver.find_element_by_name(self.EDIT_ORDER_LINK)
        editLink.click()
        cart = cart_popup(self.driver)
        for i in range(2):
            cart.delete_product()
        time.sleep(5)
        cart.checkRedirectAfterCleaningTheCart()


class SigninPage(Base):
    def login(self, logName, password):
        textbox1 = self.findElement(self.LOGIN_TEXTBOX)
        textbox1.clear()
        textbox1.send_keys(logName)
        textbox2 = self.findElement(self.PASSWORD_TEXTBOX)
        textbox2.clear()
        textbox2.send_keys(password)
        btn = self.findElement(self.LOGIN_BUTTON)
        btn.click()

    def checkFailLogin(self):
        WebDriverWait(self.driver,10).\
            until(expected_conditions.\
                text_to_be_present_in_element(self.RUBRIC_HEADLINE,"Вход в интернет-магазин"))
        #WebDriverWait(self.driver,10).\
        #    until(expected_conditions.\
        #        text_to_be_present_in_element(self.ERROR_MESSAGE,"Необходимо подтвердить, что вы не робот"))