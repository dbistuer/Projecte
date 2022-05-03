from behave import *

@given(u'Exists the following user')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    for row in context.table:

        # Register user
        user = User(username=row['alias'], email=row['email'], first_name=row['name'])
        user.set_password(row['password'])
        user.save()

        client = Client.objects.get(user=user)
        client.address =row['address']
        client.DNI = row['DNI'] 
        client.cardNumber = row['cardNumber']
        client.telephone = row['phoneNumber']
        client.save()



@when(u'I visit the profile page and I login')
def step_impl(context):
    context.browser.visit(context.get_url('profile'))
    for row in context.table:
        # Get login form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()
    



@then(u'I\'m viewing the user details')
def step_impl(context):
    assert context.browser.url == context.get_url('profile')
    
    for row in context.table:
        for heading in row.headings:
            assert context.browser.is_text_present(row[heading])
    



