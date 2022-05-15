from Projecte.settings.base import BASE_DIR
from behave import *


@when (u'The staff logs in')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('login'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Login').first.click()


@Then(u'We look into the add movie')
def step_impl(context):
    context.browser.find_by_value('Add movie').first.click()

@When(u'We look into the navbar and apears the menu item "Add movie" click on it')
def step_impl(context):
    context.browser.find_by_value('Add movie').first.click()


@Then(u'We fulfill the form and create the movie')
def step_impl(context):
    from Teatre.models.movie_ import Movie
    for row in context.table:
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            if heading != 'gender' and heading != 'classification':
                if heading != 'image':
                    context.browser.fill(heading,row[heading])
                else:
                    context.browser.fill(heading, (str(BASE_DIR) + row[heading]))
            else:
                context.browser.find_by_xpath('//select[@name="'+heading+'"]//option[@value="'+row[heading]+'"]').last.click()
    context.browser.find_by_value('Add').first.click()
    movie = Movie.objects.get(name=context.table[0][0])

    assert Movie.objects.filter(name=movie.name).exists()
    assert Movie.objects.filter(gender=movie.gender).exists()
    assert Movie.objects.filter(classification=movie.classification).exists()
    assert Movie.objects.filter(duration=movie.duration).exists()
    assert Movie.objects.filter(image=movie.image.name).exists()
    assert Movie.objects.filter(synopsis=movie.synopsis).exists()
    assert Movie.objects.filter(id=movie.id).exists()
    assert not Movie.objects.filter(id=500).exists()
    finaly(context)

def finaly(context):
    from Teatre.models.movie_ import Movie
    movie = Movie.objects.get(name=context.table[0][0])
    movie.delete()
    context.browser.find_by_text('Home').first.click()