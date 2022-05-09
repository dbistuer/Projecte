from behave import *

@when(u'I visit the delete account page')
def step_impl(context):
    context.browser.visit(context.get_url('delete_user'))


@then(u'I click the confirmation button in order to delete the account')
def step_impl(context):
    form = context.browser.find_by_tag('form').first
    form.find_by_value('delete').first.click()


@then(u'The user "marc" has been deleted, it does not exist in the database')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client
    
    assert not User.objects.filter(username='marc').exists() 
    assert not Client.objects.filter(DNI='78101067J').exists() 
