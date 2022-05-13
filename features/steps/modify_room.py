from behave import *

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