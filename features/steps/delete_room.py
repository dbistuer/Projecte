from behave import *

@given(u'Given the following room in a cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema, Room

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'])
        cinema.save()
        room = Room(number=row['number'],capacity=row['capacity'],Cinema_id=cinema.id)
        room.save()

@when(u'We enter the cinema list')
def step_impl(context):
    context.browser.visit(context.get_url('list_cinemas'))
    context.browser.find_by_value('Room list').last.click()

@then(u'I look up the details of a room of a cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema, Room

    context.browser.find_by_value('detalles').last.click()
    cinema = Cinema.objects.get(name='Cinemax')
    room = Room.objects.get(number='3')
    assert context.browser.url == context.get_url('modify_room',cinema.id,room.id)
    assert Room.objects.filter(id=room.id).exists()
    context.browser.find_by_value('eliminar').last.click()

    assert not Room.objects.filter(id=room.id).exists()