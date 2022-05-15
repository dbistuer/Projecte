from behave import *

@Then(u'Create a movie on database and go to edit page')
def step_impl(context):
    from Teatre.models.movie_ import Movie
    from Projecte.settings.base import BASE_DIR
    movie = Movie(name='test', duration=120, synopsis='test synopsis', classification='X', gender='War',
                  image=str(BASE_DIR) + '\'features\'image\'test.png')
    movie.save()
    assert Movie.objects.filter(name='test').exists()
    context.browser.find_by_text('List of movies').first.click()
    context.browser.find_by_text('Detail').first.click()
    context.browser.find_by_text('Edit').last.click()


@Given(u'those data fulfill on form')
def step_impl(context):
    from Projecte.settings.base import BASE_DIR
    from Teatre.models.movie_ import Movie
    for row in context.table:
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            if heading != 'gender' and heading != 'classification':
                if heading != 'image':
                    context.browser.fill(heading, row[heading])
                else:
                    context.browser.fill(heading, (str(BASE_DIR) + row[heading]))
            else:
                context.browser.find_by_xpath(
                    '//select[@name="' + heading + '"]//option[@value="' + row[heading] + '"]').last.click()
    context.browser.find_by_value('Edit').first.click()
    movie = Movie.objects.get(name='test')

    assert Movie.objects.filter(name=movie.name).exists()
    assert Movie.objects.filter(gender=movie.gender).exists()
    assert Movie.objects.filter(classification=movie.classification).exists()
    assert Movie.objects.filter(duration=movie.duration).exists()
    assert Movie.objects.filter(image=movie.image.name).exists()
    assert Movie.objects.filter(synopsis=movie.synopsis).exists()
    assert Movie.objects.filter(pk=movie.id).exists()
    assert not Movie.objects.filter(pk=500).exists()
    finaly(context)


def finaly(context):
    from Teatre.models.movie_ import Movie
    movie = Movie.objects.get(name='test')
    movie.delete()
    context.browser.find_by_text('Home').first.click()