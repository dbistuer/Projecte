from behave import *

@When(u'We go to cinema list and press new')
def step_impl(context):
    context.browser.find_by_value('+New').first.click()
    
@Then(u'We fulfill the form and create the cinema')
def step_impl(context):
    from Teatre.models.cinema_ import Cinema
    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])

    context.browser.find_by_value('save').first.click()
    cinema = Cinema.objects.get(number='1')


    assert Cinema.objects.filter(name=cinema.name).exists()
    assert Cinema.objects.filter(id=cinema.id).exists()
    assert not Cinema.objects.filter(adress=a).exists()
