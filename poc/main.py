'''
Tyrone Swinnie
Design for Web Programming
9/18/14
POC Assignment
'''


import webapp2
import urllib2
from xml.dom import minidom   #library used to pars xml

class MainHandler(webapp2.RequestHandler):
    def get(self):

        url = "http://maps.google.com/maps/api/geocode/xml?address=florida&sensor=false" # set up the url to get data, also passing in Florida so that google map returns data on florida

        request = urllib2.Request(url)  #set up a variable that wil get the data from the url

        opener = urllib2.build_opener()  #create a var that will represent the object that is returned

        result = opener.open(request)  #using result to get the result from the url and request the data from the API

        xmldoc = minidom.parse(result) #I am going to parse the xml data

        new_data = xmldoc.getElementsByTagName("long_name")[0].firstChild.nodeValue  #testing to see if I can get some data back

        new_data_two = xmldoc.getElementsByTagName("short_name")[0].firstChild.nodeValue  #testing to see if I can get some data back

        latt = xmldoc.getElementsByTagName("lat")[0].firstChild.nodeValue  #testing to see if I can get some data back getting back lattitude


        long = xmldoc.getElementsByTagName("lng")[0].firstChild.nodeValue  #testing to see if I can get some data back getting back longitude

        self.response.write("The data that is returned from Google Maps API:  " + " <br/> " + new_data + " <br/> " + new_data_two + " <br/> " + latt + " <br/> " + long)




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




        '''
        page_close = '''
</body>
</html>
        '''



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
