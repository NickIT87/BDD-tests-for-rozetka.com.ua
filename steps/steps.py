#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
from pages import pageClasses

#_____________Global step - get page url_____________

@given('I am on home page')
def step_i_am_on_home_page(context):
    context.driver.maximize_window()
    context.driver.get(pageClasses.Base.ADRESS)

#_____________Steps of catalog.feature_______________

@when('find catalog i search for {text1} and {text2}') 
def step_i_search_on_catalog(context, text1, text2):
    main_page = pageClasses.MainPage(context.driver)
    main_page.search_catalog(text1, text2)

@then('Check rubric headline and catalog btn {text} next {text2} next {text3} next {text4}')
def step_check_catalog_result(context, text, text2, text3, text4):
    catalog_page = pageClasses.CatalogPage(context.driver)
    catalog_page.assert_page(text)
    catalog_page.search_catalog2(text2, text3)
    catalog_page.assert_page(text4)

#_____________Steps of search.feature________________

@then('I search for {text}') 
def step_i_search_for(context, text):
    main_page = pageClasses.MainPage(context.driver)
    main_page.search(text)

@when('I should see results {my_request_result}')
def step_check_results(context, my_request_result):
    search_results_page = pageClasses.ProductsPage(context.driver)
    search_results_page.checkResults(my_request_result)

#_____________Steps of cart.feature__________________

@given('I am on search result page')
def step_i_am_on_search_result_page(context):
    context.driver.maximize_window()
    context.driver.get(pageClasses.Base.SEARCH_RESULT_PAGE)

@then('after click on checkbox_asus, i chose product and accept my order') 
def step_i_search_for(context):
    product_page = pageClasses.ProductsPage(context.driver)
    product_page.clickOnCheckBoxAsus()
    product_page.chooseProducts()

@when('I going to order_page, i edit my order and delete all products')
def step_edit_my_order(context):
    order_page = pageClasses.OrderPage(context.driver)
    order_page.editMyOrder()

#_____________Steps of login.feature__________________

@then('after redirect on cart we login on shop {logtext} and {passText}')
def step_login(context, logtext, passText):
    signin_page = pageClasses.SigninPage(context.driver)
    signin_page.login(logtext, passText)

@when('login fail we can see error message')
def step_Check_failLogin(context):
    signin_page = pageClasses.SigninPage(context.driver)
    signin_page.checkFailLogin()