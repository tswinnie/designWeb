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
        self.body = "Welcome Tyrone TO My SIte"
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
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css):
        self.__css = new_css



