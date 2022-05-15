from behave import *

@given(u'Exists the following cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema, Room

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'],description=row['description'])
        cinema.save()
        
@when(u'I visit the list of cinemas')
def step_impl(context):
    context.browser.visit(context.get_url('list_cinemas'))
    context.browser.find_by_value('Details').first.click()
    
@then(u'I look up the cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema
    cinema = Cinema.objects.get(name='a')
    assert context.browser.url == context.get_url('cinema_detail',cinema.id)

    for row in context.table:
        for heading in row.headings:
            assert context.browser.is_text_present(row[heading])
