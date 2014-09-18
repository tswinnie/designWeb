__author__ = 'tyroneswinnie'

# I am going to create a class that will hold the HTML for my application

class hello(object):
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
    <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic' rel='stylesheet' type='text/css'>
    <link href="https://fontastic.s3.amazonaws.com/EX5vThHnfUWWhKCXqQANtS/icons.css" rel="stylesheet">

    <body>
        """
        self.body = """

        <div class="topBar"></div>
        <p class="title"> Monitor Your Storage Usage</p>
        <div class="container">


<div class="moveBox"></div>

  <div class="box" style="margin-right: -295px; width: 322px; margin-top: -13px; margin-left: -27px;">
            <div class="icon-user"" style="position: relative; top: 25px; "></div>
            </div>



        </div>



        """
        self.close = """

    </body>

</html>



        """

        self.user_page_update =""

    def update_this(self):
        self.user_page_update = self.head + self.body + self.close  #here i am going to set user_page = to all the elements from my class.
        self.user_page_update = self.user_page_update.format(**locals())  #I am going to use the locals() here so that I can use self.title in html.


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







