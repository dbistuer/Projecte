from behave import *



@when(u'I visit the profile page')
def step_impl(context):
    context.browser.visit(context.get_url('profile'))


@then(u'I login as user "marc"')
def step_impl(context):
    for row in context.table:
        # Get login form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()
    

@then(u'I click the edit profile button in order to go to the edit profile page')
def step_impl(context):
    # Get form
    form = context.browser.find_by_tag('form').first
    # Click button
    form.find_by_value('Edit profile').first.click()
    


@then(u'I edit my profile with this new data')
def step_impl(context):
    for row in context.table:
        # Get form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('confirm_changes').first.click()
    
@then(u'The user "marc" has been modified with the previous new data')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    user = User.objects.get(username='maria')
    client = Client.objects.get(user=user)

    for row in context.table:

        assert client.user.first_name == row['name']
        assert client.user.username == row['alias']
        assert client.user.email == row['email']
        assert client.address == row['address']
        assert client.telephone == row['phoneNumber']
        assert client.cardNumber == row['cardNumber']
        assert client.DNI == row['DNI']

@then(u'I can see an error')
def step_impl(context):
    assert context.browser.is_text_present('is not valid')
