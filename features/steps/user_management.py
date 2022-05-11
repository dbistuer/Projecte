from behave import *

@given(u'Exists the following users')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    for row in context.table:

        # Register user
        user = User(username=row['alias'], email=row['email'], first_name=row['name'])
        user.set_password(row['password'])
        
        if row['alias'] == 'normal_user':
            user.is_active = True
            user.is_staff = False
            user.is_superuser = False

        elif row['alias'] == 'employee':
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False

        elif row['alias'] == 'admin':
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True

        user.save()

        client = Client.objects.get(user=user)
        client.address =row['address']
        client.DNI = row['DNI'] 
        client.cardNumber = row['cardNumber']
        client.telephone = row['phoneNumber']
        client.save()

@when(u'I visit the user management page')
def step_impl(context):
    context.browser.visit(context.get_url('user_management'))


@then(u'I login as user "normal_user"')
def step_impl(context):
    for row in context.table:
        # Get login form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()

@then(u'I see that this account does not have access to this page')
def step_impl(context):
    assert context.browser.is_text_present('To proceed, please login with an account that has access.')

@then(u'I login as user "employee"')
def step_impl(context):
    for row in context.table:
        # Get login form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()

@then(u'I login as user "admin"')
def step_impl(context):
    for row in context.table:
        # Get login form
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()

@then(u'I change the role of the user "employee" to admin')
def step_impl(context):        
        context.browser.find_by_xpath('//select[@id="user_role"]//option[@value="admin"]').last.click()
        context.browser.find_by_name('username').last.click()

@then(u'The user "employee" has admin permissions')
def step_impl(context):
    from django.contrib.auth.models import User

    assert User.objects.get(username='employee').is_superuser
    assert User.objects.get(username='employee').is_staff
    assert User.objects.get(username='employee').is_active

@then(u'I change the role of the user "employee" to normal_user')
def step_impl(context):
    context.browser.find_by_xpath('//select[@id="user_role"]//option[@value="normal_client"]').last.click()
    context.browser.find_by_name('username').last.click()

@then(u'The user "employee" has normal user permissions')
def step_impl(context):
    from django.contrib.auth.models import User

    assert not User.objects.get(username='employee').is_superuser
    assert not User.objects.get(username='employee').is_staff
    assert User.objects.get(username='employee').is_active

@then(u'I change the role of the user "employee" to employee')
def step_impl(context):
    context.browser.find_by_xpath('//select[@id="user_role"]//option[@value="employee"]').last.click()
    context.browser.find_by_name('username').last.click()

@then(u'The user "employee" has employee permissions')
def step_impl(context):
    from django.contrib.auth.models import User

    assert not User.objects.get(username='employee').is_superuser
    assert User.objects.get(username='employee').is_staff
    assert User.objects.get(username='employee').is_active

@then(u'I change the role of the user "normal_client" to admin')
def step_impl(context):
    context.browser.find_by_xpath('//select[@id="user_role"]//option[@value="admin"]').first.click()
    context.browser.find_by_name('username').first.click()

@then(u'the user "normal_client has admin permissions')
def step_impl(context):
    from django.contrib.auth.models import User

    assert User.objects.get(username='normal_user').is_superuser
    assert User.objects.get(username='normal_user').is_staff
    assert User.objects.get(username='normal_user').is_active

@then(u'I delete the user "employee"')
def step_impl(context):
    context.browser.find_by_name('delete').last.click()


@then(u'The user "employee" is not in the database')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    assert not User.objects.filter(username='employee').exists()
    assert not Client.objects.filter(telephone='642897512').exists()


@then(u'I delete the user "normal_user"')
def step_impl(context):
    context.browser.find_by_name('delete').first.click()


@then(u'The user "normal_user" is not in the database')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    assert not User.objects.filter(username='normal_user').exists()
    assert not Client.objects.filter(telephone='642897511').exists()