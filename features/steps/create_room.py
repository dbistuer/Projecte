from behave import *

@Given(u'The user has logged in')
def step_impl(context):
    from django.contrib.auth.models import User
    from Teatre.models.account import Client

    for row in context.table:

        # Register user
        user = User(username=row['alias'], email=row['email'], first_name=row['name'])
        user.set_password(row['password'])

        if row['alias'] == 'employee':
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False

        user.save()

        client = Client.objects.get(user=user)
        client.address = row['address']
        client.DNI = row['DNI']
        client.cardNumber = row['cardNumber']
        client.telephone = row['phoneNumber']
        client.save()

@Then (u'The staff logs in')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('login'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()


@Given(u'A cinema exists')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'])
        cinema.save()
    context.browser.visit(context.get_url('list_cinemas'))

@When(u'We look into the cinema details and press try to create a button')
def step_impl(context):
    context.browser.find_by_value('Room list').first.click()
    context.browser.find_by_value('Nueva sala').first.click()


@Then(u'We fulfill the form and create the room')
def step_impl(context):
    from Teatre.models.cinema_ import Room
    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])

    context.browser.find_by_xpath('//select[@id="cinema"]//option["Lauren"]').last.click()
    context.browser.find_by_value('save').first.click()
    room = Room.objects.get(number='1')


    assert Room.objects.filter(capacity=room.capacity).exists()
    assert Room.objects.filter(id=room.id).exists()
    assert not Room.objects.filter(number=500).exists()