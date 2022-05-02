from behave import *                                                                                          
# https://www.tutorialspoint.com/behave/behave_quick_guide.htm

@when(u'I register client')
def step_impl(context):
    
    for row in context.table:
        
        # Go to register page
        #url = context.get_url('Projecte:register')
        #print(url )
        context.browser.visit('https://www.google.com/')
        
        # Get register form
        form = context.browser.find_by_tag('form').first
        
        for heading in row.headings:
            print(heading)
            print(row[heading])
            print(form)

@then(u'I\'m viewing the login page')
def step_impl(context):
    pass

@then(u'there\'s a new client with the previous data')
def step_impl(context):
    pass

