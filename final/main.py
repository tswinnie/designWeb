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

        p = UserInput()
        p.inputs = [['recipe', 'text', 'Enter Your Favorite Dish'], ['Submit', 'submit']]
        self.response.write("<div style='margin: 0 auto; width: 195px; display:block; margin-top: 25%;'>" + p.print_out() + "</div>")

        if self.request.GET:
            #get info from api
            rd = RecipeModel()
            rd.recipe = self.request.GET['recipe']
            rd.callAPI()

            rv = RecipeView() # calling my view class
            rv.title = "<div style='margin: 0 auto; width: 195px; display:block; float: left; position: absolute; bottom: 62px; z-index: 999;'>" + "<b>Name of the recipe is:</b>  " + "<br/>" + rd.array_dos[0] + "</div>"  #setting the var I created in my views class equal to the index value of object being returned in array_dos
            rv.ingredients = "<div style='margin: 0 auto; width: 195px; display:block; float: left; position: absolute; bottom: 33px; z-index: 999; margin-left: 315px;'>" + "<b>Ingredients:</b> " + rd.array_dos[1] + "</div>" #setting the var I created in my views class equal to the index value of object being returned in array_dos
            rv.link = "<div style='margin: 0 auto; width: 195px; display:block; float: left; position: absolute; bottom: 31px; z-index: 999; margin-left: 615px;'>" + "<b>Link to the recipe:</b> " + rd.array_dos[2] + "</div>" #setting the var I created in my views class equal to the index value of object being returned in array_dos
            rv.source = "<div style='margin: 0 auto; width: 195px; display:block; float: left; position: absolute; bottom:106px; z-index: 999; margin-left: 963px;'>" + "<b>Name of the source is:</b> " + rd.array_dos[3] + "</div>" #setting the var I created in my views class equal to the index value of object being returned in array_dos
            rv.recipe_link = "<div style='margin: 0 auto; width: 195px; display:block; float: left; position: absolute; bottom:66px; z-index: 999; margin-left: 963px; '>" + "<b>Link to the source:</b> " + rd.array_dos[4] + "</div>" #setting the var I created in my views class equal to the index value of object being returned in array_dos
            rv.version_num = "<div style='margin: 0 auto; width: 195px; display:block; float: left; position: absolute; bottom:36px; z-index: 999; margin-left: 963px;'>" + "<b>The version number is:</b> " + str(rd.array_dos[5]) + "</div>" #setting the var I created in my views class equal to the index value of object being returned in array_dos

            #write the returned data to the page
            self.response.write(rv.title + rv.ingredients + rv.link + rv.source + rv.recipe_link + str(rv.version_num))




#now I am going to create my recipe view class
class RecipeView(object):
    ''' This class controls how the views are displayed to the user'''
    def __init__(self):
    #now create an array to hold objects
        self.__new_array_dos = []
        self.title = ''
        self.ingredients = ''
        self.link = ''
        self.source = ''
        self.recipe_link = ''
        self.version_num = ''


    @property
    def new_array_dos(self):
        pass

    @new_array_dos.setter
    def new_array_dos(self, arr):
        self.__new_array_dos = arr



#now I am going to create my model class
class RecipeModel(object):
    ''' This class is responsible for fetching, sorting and parsing my data'''
    def __init__(self):
        self.__url = "http://www.recipepuppy.com/api/?&q="
        self.__recipe = ''
        self.__jsondoc = ''


#now I am going to make a property that handles the API
    def callAPI(self):
        #now I am going to make the request to the api

        request = urllib2.Request(self.__url + self.__recipe)  #set up a variable that wil get the data from the url

        opener = urllib2.build_opener()  #create a var that will represent the object that is returned

        result = opener.open(request)  #using result to get the result from the url and request the data from the API

        self.__jsondoc = json.load(result)  #i am parsing my json doc here


        #now I am going to assgin the data returned from the json object to my recipe data object
        self._array_do = []
        #call my recipe data object method
        array_object = RecipeData()
        #now assign the corresponding values returned from json object to objects in recipe object
        array_object.title = self.__jsondoc['results'][0]['title']
        array_object.ingredients = self.__jsondoc['results'][0]['ingredients']
        array_object.link = self.__jsondoc['results'][0]['href']
        array_object.source = self.__jsondoc['href']
        array_object.link_source = self.__jsondoc['href']
        array_object.version_number = self.__jsondoc['version']
        #now I am going to add these objects to my array
        # self._array_do.append(array_object)
        self._array_do.append(array_object.title)
        self._array_do.append(array_object.ingredients)
        self._array_do.append(array_object.link)
        self._array_do.append(array_object.source)
        self._array_do.append(array_object.link_source)
        self._array_do.append(array_object.version_number)

    @property
    def array_dos(self):
        return self._array_do

    @property
    def recipe(self):
        pass

    @recipe.setter
    def recipe(self, r):
        self.__recipe = r







# now I am going to create a recipe data object
class RecipeData(object):
    ''' This data object holds the data that is returned from the API '''
    def __init__(self):
        self.title = ' '
        self.ingredients = ' '
        self.link = ' '
        self.source = ' '
        self.link_source = ' '
        self.version_number = ' '





# I am going to create my page class

class Page(object):  #MY PAGE CLASS IS MY ABSTRACT Class
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

        self._body = '''
<div class="form-search">
<h1>Let us help you choose the perfect meal today.</h1>
</div>
<div class="bottomPage"></div>


        '''

        self._close = '''

    </body>

</html>

        '''

        self.home = ''
#created function to print out my page
    def print_out(self):

        self.home = self._head + self._body + self._close
        self.home = self.home.format(**locals())




#I am going to create my form class that will hold the user input value

class UserInput(Page):  #MY USERINPUT CLASS IS MY INHERITANCE
    def __init__(self):
        #run the constructor function for my Page class
        super(UserInput, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''


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



#now I am going to create a function that will print out my form
    def print_out(self): #POLYMORPHISM ALERT WHICH IS OVERRIDING THE PRINT OUT AOVE
        new_form = self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close

        new_form = new_form.format(**locals())
        return new_form





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
