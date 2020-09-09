from behave import *
from selenium import webdriver

# allows the steps to receive arguments from the navigation.feature file
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage
from video_code.tests.acceptance.pages.blog_page import BlogPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()  #Chrome('c:/user/glenn/anaconda/)  if it is not in path, you must give path.
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome()  #Chrome('c:/user/glenn/anaconda/)  if it is not in path, you must give path.
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url

@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


