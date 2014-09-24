'''
Tyrone Swinnie
Design for Web
Final Project: Application with API
9/22/14
'''


import webapp2
import urllib2  #imported libray to help get data
import json  #added library to pars json data


class MainHandler(webapp2.RequestHandler):
    def get(self):

        # self.response.write('Hello world!')
        p = UserInput()
        p.inputs = [['recipe', 'text', 'Search Recipe'], ['Submit', 'submit']]
        self.response.write(p.show_form())

        if self.request.GET:
            #get info from api
            recipe = self.request.GET['recipe']





            url = "http://www.recipepuppy.com/api/?i=onions,garlic&q=" + recipe


            request = urllib2.Request(url)  #set up a variable that wil get the data from the url

            opener = urllib2.build_opener()  #create a var that will represent the object that is returned

            result = opener.open(request)  #using result to get the result from the url and request the data from the API

            jsondoc = json.load(result)  #i am parsing my json doc here

            #now I am going to get back specific pieces of data


            source = jsondoc['title']

            source_link = jsondoc['href']

            version = jsondoc['version']


            img = jsondoc['results'][0]['thumbnail']

            name_list = "The name of this recipe is: " + jsondoc['results'][0]['title']

            ingredients = jsondoc['results'][0]['ingredients']

            link = jsondoc['results'][0]['href']

            self.ingr_list = '' #create var that will hold the value for my items in the array of ingredients

            for item in ingredients: #loop through the items in the array of ingredients
                self.ingr_list += item  #add each item to the page





















# I am going to create my page class

class Page(object):
    def __init__(self):

        self.css = 'css/styles.css'
        self._head = '''
  <link href="{self.css}" rel="stylesheet" type="text/css" />
  <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic' rel='stylesheet' type='text/css'>
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

        self.home = ''
#created function to print out my page
    def print_out(self):

        self.home = self._head + self._body + self._close
        self.home = self.home.format(**locals())
        # return self.home


        # return self._head + self._body + self._close


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
        new_form = self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close
        new_form = new_form.format(**locals())
        return new_form























app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
