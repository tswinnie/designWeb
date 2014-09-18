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

      <h3>Hello</h3>


        </div>



        """
        self.close = """

    </body>

</html>



        """


