from behave import *                                                                                          

@given(u'Exists a user "marc" with password "1234"')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    for row in context.table:
        user = User(username=row['alias'], email=row['email'], first_name=row['name'])
        user.set_password(row['password'])
        user.save()

        client = Client.objects.get(user=user)
        client.address =row['address']
        client.DNI = row['DNI'] 
        client.cardNumber = row['cardNumber']
        client.telephone = row['phoneNumber']
        client.save()


@when(u'I login as "marc" with password "1234"')
def step_impl(context):
    for row in context.table:
        # Go to login page
        context.browser.visit(context.get_url('login'))
        
        # Get login form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()


@then(u'I\'m viewing the home page')
def step_impl(context):
    assert context.browser.url == context.get_url('home')


@then(u'The user "marc" has logged succesfully')
def step_impl(context):
    from django.contrib.auth.models import User
    user = User.objects.get(username='marc')
    assert user.is_authenticated


@when(u'I login with a user that is not registered')
def step_impl(context):
    for row in context.table:
        # Go to login page
        context.browser.visit(context.get_url('login'))
        
        # Get login form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()

@then(u'I\'m viewing the login page with an error message')
def step_impl(context):
    assert context.browser.is_text_present('didn\'t match')
