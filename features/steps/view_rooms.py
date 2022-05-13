from behave import *
@Given(u'The staff has logged in')
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

@Then (u'The staff logs in the account')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('login'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()



@given(u'Exists the following room in a cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema, Room

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'])
        cinema.save()
        room = Room(number=row['number'],capacity=row['capacity'],Cinema_id=cinema.id)
        room.save()

@when(u'I visit the cinema list')
def step_impl(context):
    context.browser.visit(context.get_url('list_cinemas'))
    context.browser.find_by_value('Room list').first.click()

@then(u'I look up the rooms in the cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema
    cinema = Cinema.objects.get(name='Llauren')
    assert context.browser.url == context.get_url('room_list',cinema.id)

    for row in context.table:
        for heading in row.headings:
            assert context.browser.is_text_present(row[heading])
