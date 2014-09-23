'''
Tyrone Swinnie
Design for Web
Final Project: Application with API
9/22/14
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')
        p = UserInput()
        p.inputs = [['recipe', 'text', 'Search Recipe'], ['Submit', 'submit']]
        self.response.write(p.print_out())

# I am going to create my page class

class Page(object):
    def __init__(self):

        self._head = '''

<!DOCTYPE HTML>

<html>

    <head>

        <title></title>

    </head>
    <body> '''

        self._body = 'Test'
        self._close = '''

    </body>

</html>

        '''
#created function to print out my page
    def print_out(self):
        return self._head + self._body + self._close


#I am going to create my form class that will hold the user input value

class UserInput(Page):
    def __init__(self):
        #run the constructor function for my Page class
        super(UserInput, self).__init__()
        self._form_open = '<form method="GET"'
        self._form_close = '</form>'
        self.__inputs = []
        #<input type="text" value = "" name="recipe" placeholder="Search Recipes" />
        #<input type="submit" value="Submit" />

        @property
        def inputs(self):
            pass

        @inputs.setter
        def inputs(self, arr):
            #change my input variables from private
            self.__inputs = arr
            #now I am going to sort through my array of inputs
            print arr















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
