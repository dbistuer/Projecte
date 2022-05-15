from behave import *

@given(u'Given the following cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'],description=row['description'])
        cinema.save()
        
@when(u'We enter the details of a cinema')
def step_impl(context):
    context.browser.visit(context.get_url('list_cinemas'))
    context.browser.find_by_value('Details').last.click()
    
@then(u'I modify the details of a cinema from the database')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema

    context.browser.find_by_value('Edit').last.click()
    cinema = Cinema.objects.get(name='a')
    #assert context.browser.url == context.get_url('modify_room',cinema.id,room.id)
    #assert Cinema.objects.filter(id=cinema.id).exists()

    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])

    context.browser.find_by_value('Save').last.click()

    assert Cinema.objects.filter(description='b').exists()
    assert not Cinema.objects.filter(description='a').exists()
