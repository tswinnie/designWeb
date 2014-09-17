__author__ = 'tyroneswinnie'

# I am going to create a class that will hold the HTML for my application

class Page(object):
    def __int__(self):
        self.__title = "Welcome"
        self.__css    = "css/styles.css"
        self.head = """


<DOCTYPE HTML>
<html>

    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />

    </head>
    <body>
        """

        self.body = "Welcome to my page"

        self.close = """

    </body>
</html>
        """

#I am going to make the attributes title and css able to be called and edited from my main.py file
    # using getter and setters

    @property
    def title(self):
        pass

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def css(self):
        pass

    @css.setter
    def css(self, new_css):
        self.__css = new_css



