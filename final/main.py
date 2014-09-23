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
        self.response.write(p.show_form())

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

        self._body = ''
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
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
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
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]

            if len(item) > 2:
                self._form_inputs += '" placeholder="' + item[2] + '" />'

            else:
                self._form_inputs += '" />'

            print self._form_inputs

#now I am going to create a function that will print out my form
    def show_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
