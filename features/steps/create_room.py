from behave import *

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