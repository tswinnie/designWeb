'''
Tyrone Swinnie
Design for Web Programming
9/18/14
POC Assignment
'''


import webapp2
import urllib2  #imported libray to help get data
from xml.dom import minidom   #library used to pars xml

class MainHandler(webapp2.RequestHandler):
    def get(self):

        url = "http://maps.google.com/maps/api/geocode/xml?address=florida&sensor=false" # set up the url to get data, also passing in Florida so that google map returns data on florida

        request = urllib2.Request(url)  #set up a variable that wil get the data from the url

        opener = urllib2.build_opener()  #create a var that will represent the object that is returned

        result = opener.open(request)  #using result to get the result from the url and request the data from the API

        xmldoc = minidom.parse(result) #I am going to parse the xml data

        new_data = xmldoc.getElementsByTagName("long_name")[0].firstChild.nodeValue  #getting a specific set back from xml

        new_data_two = xmldoc.getElementsByTagName("short_name")[0].firstChild.nodeValue  #testing to see if I can get some data back

        latt = xmldoc.getElementsByTagName("lat")[0].firstChild.nodeValue  #testing to see if I can get some data back getting back lattitude


        long = xmldoc.getElementsByTagName("lng")[0].firstChild.nodeValue  #testing to see if I can get some data back getting back longitude

        self.response.write("The data that is returned from Google Maps API:  " + " <br/> " + new_data + " <br/> " + new_data_two + " <br/> " + latt + " <br/> " + long)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
