from behave import *

@Given(u'The user has logged')
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

@Then (u'The staff logs')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('login'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()


@given(u'Given the following room of a cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema, Room

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'])
        cinema.save()
        room = Room(number=row['number'],capacity=row['capacity'],Cinema_id=cinema.id)
        room.save()

@when(u'We enter the details of a room')
def step_impl(context):
    context.browser.visit(context.get_url('list_cinemas'))
    context.browser.find_by_value('Room list').last.click()

@then(u'I modify the details of a room from the database')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema, Room

    context.browser.find_by_value('detalles').last.click()
    cinema = Cinema.objects.get(name='Cinema persa')
    room = Room.objects.get(number='7')
    assert context.browser.url == context.get_url('modify_room',cinema.id,room.id)
    assert Room.objects.filter(id=room.id).exists()

    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])

    context.browser.find_by_value('modify').last.click()

    assert Room.objects.filter(capacity=100).exists()
    assert not Room.objects.filter(capacity=225).exists()