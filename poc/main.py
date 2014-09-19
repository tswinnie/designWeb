'''
Tyrone Swinnie
Design for Web Programming
9/18/14
Simple Form Assignment
'''


import webapp2
import urllib2
from xml.dom import minidom   #library used to pars xml

class MainHandler(webapp2.RequestHandler):
    def get(self):

        url = "http://maps.google.com/maps/api/geocode/xml?address=sydney&sensor=false" # set up the url to get data

        request = urllib2.Request(url)  #set up a variable that wil get the data from the url

        opener = urllib2.build_opener()  #create a var that will represent the object that is returned

        result = opener.open(request)  #using result to get the result from the url and request the data from the API

        xmldoc = minidom.parse(result) #I am going to parse the xml data



        # Create the page so that I can create a form
        # create the form inside the html code like I normally would in an HTML document

        page_head = '''<!DOCTYPE HTML>
<html>
<head>
<title>Welcome to my landing page</title>
<link href='http://fonts.googleapis.com/css?family=Lato:300,400,300italic,400italic' rel='stylesheet' type='text/css'>
<style type="text/css">
body{
font-family: 'Lato', sans-serif;

}

html {
  background: url(images/background.png) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}

.container{

width: 650px !important;
height: 325px !important;
margin-left: auto!important;
margin-right: auto !important;
background: #fff !important;
border-radius: 2px !important;
}

.resultsCon{

width: 650px !important;
height: 325px !important;
margin-left: auto!important;
margin-right: auto !important;
background: #fff !important;
border-radius: 2px !important;

}

.topLabel {
text-align: center !important;
display: block !important;
text-transform: uppercase !important;
font-weight: bold !important;
color: #282828 !important;
padding-top: 20% !important;
padding-bottom: 2% !important;
}

.userName {
border: none !important;
background: #eaedf2 !important;
width: 215px !important;
height: 33px !important;
border-radius: 2px !important;
margin-left: 40px !important;
}

.bottomLabel {
text-align: center !important;
display: block !important;
text-transform: uppercase !important;
font-weight: bold !important;
color: #282828 !important;
padding-top: 2% !important;
padding-bottom: 2% !important;
}


.submitBTN {
border: none;
width: 150px;
height: 35px;
margin-left: 67%;
margin-top: 19px;
background: #4b93ff;
border-radius: 2px !important;
color: #fff;
box-shadow: none !important;
position: relative;
top: -319px;
}

#bg {
  position: fixed;
  top: 0;
  left: 0;
  min-width: 100%;
  min-height: 100%;
}

.topText{
text-align: center;
font-size: 1.3em;
width: 980px;
margin: 0 auto;
color: #fff;
font-weight: 200;
line-height: 1.5;
padding: 10px;

}

.titlePage{
text-align: center;
font-size: 2.5em;
color: #fff;
font-weight: 200;

}

form{
color: #fff !important;
}

</style>
'''
        page_body = '''
<body>
        <h2 class="titlePage">We are Coming Soon!</h2>

<div class="boxRight">

<p class="topText">We are bringing the latest technology to you and developers alike. We will change the world and how it thinks aboutweb development.</p>
<p class="topText">If you would like to know more about this new technology, please fill out the form and we will be in touch.</p>
</div>

<div class="container">
<form method ="GET" action="">



        '''
        page_close = '''
</form>
</div>
</body>
</html>
        '''

   # I am going to store the information that are collected from the user into a variable
        if self.request.GET:
            first_name = self.request.GET['first']  # this gets the value for the first name
            last_name = self.request.GET['last']  # this gets the last name value
            email = self.request.GET['email']  # this gets the email value from the user
            about_us = self.request.GET['aboutus']  # this gets the info for about us field
            excited = self.request.GET['excited']  # this gets the value to see if the user is excited
            updates = self.request.GET['updates']  # this gets value to see if the user wants you to send updates
            # return the values that the user put in the form after the submit button

            self.response.write(page_head + page_body + first_name + ' '  ' '+ last_name + ' ' ' ' + email + ' ' ' ' + about_us + ' '' ' + excited + ' ' ' ' + updates + ' ' ' ' + page_close)

        else:
            # if the user does not input any values then do this
            self.response.write(page_head + page_body + page_close)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
