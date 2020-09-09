from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage


use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    # HomePageLocators.TITLE is a tuple but the method is looking for 2 args
    # so we use * to unpack the tuple
    # title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    #title_tag = context.browser.find_element(*HomePageLocators.TITLE)

    page = BasePage(context.driver)
    assert page.title.is_displayed()


#@then('The title tag has content "(.*)"')
@step('The title tag has content "(.*)"')  #@step means it can be used anywhere (as a then, given)
def step_impl(context, content):
    # HomePageLocators.TITLE is a tuple but the method is looking for 2 args
    # so we use * to unpack the tuple
    # title_tag = context.browser.find_element(*HomePageLocators.TITLE)

    page = BasePage(context.driver)
    assert page.title.text == content

@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()

@then('I can see there is a post with the title "Test Post" in the post section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [posts for post in page.posts if post.text == title]
    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])