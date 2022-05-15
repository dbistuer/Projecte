from behave import *

@given(u'the following cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema

    for row in context.table:

        cinema = Cinema(adress=row['adress'],name=row['name'],description=row['description'])
        cinema.save()
        
@when(u'We enter the list of cinemas')
def step_impl(context):
    context.browser.visit(context.get_url('list_cinemas'))
    context.browser.find_by_value('Details').last.click()
    
@then(u'I press delete')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema

    cinema = Cinema.objects.get(name='a')
    assert Cinema.objects.filter(id=cinema.id).exists()
    context.browser.find_by_value('Delete').last.click()

    assert not Cinema.objects.filter(id=cinema.id).exists()
