from behave import *

@given(u'Exists the following room in a cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema, Room

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'])
        cinema.save()
        room = Room(number=row['number'],capacity=row['capacity'],Cinema_id=row['cinema'])
        room.save()

@when(u'I visit the cinema list')
def step_impl(context):
    context.browser.visit(context.get_url('list_cinemas'))
    context.browser.find_by_value('Room list').first.click()

@then(u'I look up the rooms in the cinema')
def step_impl(context):
    assert context.browser.url == context.get_url('room_list',1)

    for row in context.table:
        for heading in row.headings:
            assert context.browser.is_text_present(row[heading])
