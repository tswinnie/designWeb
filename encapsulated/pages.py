__author__ = 'tyroneswinnie'

# I am going to create a class that will hold the HTML for my application

class Page(object):
    def __init__(self):
        self.title = "Welcome Tyrone"
        self.css = "css/styles.css"
        self.head = """
<!DOCTYPE HTML>

<html>
    <head>
        <title>{self.title}</title>
    </head>
    <link href="{self.css}" rel="stylesheet" type="text/css" />


    <body>
        """
        self.body = """
        <p> test</p>



        """
        self.close = """

    </body>

</html>



        """

        self.user_page =""

    def update(self):
        self.user_page = self.head + self.body + self.close  #here i am going to set user_page = to all the elements from my class.
        self.user_page = self.user_page.format(**locals())  #I am going to use the locals() here so that I can use self.title in html.


#I am going to make the attributes title and css able to be called and edited from my main.py file
    # using getter and setters



    @property
    def title(self):
        return self.__title  #this is returning the value of title

    @title.setter
    def title(self, new_title):
        self.__title = new_title  #this is setting the value of title to the value of the new title

    @property
    def css(self):
        return self.__css  #this is returning the value of css

    @css.setter
    def css(self, new_css):
        self.__css = new_css  #this is setting the old value of css to the new value of css







