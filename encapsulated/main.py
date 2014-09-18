'''
Tyrone Swinnie
9/16/14
Design for Web
Encapsulated Calculator
'''


import webapp2
from pages import Page  #importing the page class


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        p.title = "My New Page"
        p.css = "css/styles.css"
        p.body = "This is a test of the text"
        p.update() #referencing my update class from pages
        self.response.write(p.user_page) #writing the user_page which has has all the html for my application

        # I will create an application that calculates the remaining storage for different users

        #I am going to set up my class that will hold my 5 data objects

        #each user will have a total storage limit of 50GB


class Michele(object):
    def __init__(self):
        self.pictures = 0  #the number of pictures in GB
        self.videos = 0  #the number of videos in GB
        self.documents = 0  #the number of documents in GB
        self.music = 0  #the number of music in GB
        self.apps = 0  #the number of all files stored in GB
        self.__remaining = 0  #total storage remaining


class Jack(object):
    def __init__(self):
        self.pictures = 0  #the number of pictures in GB
        self.videos = 0  #the number of videos in GB
        self.documents = 0  #the number of documents in GB
        self.music = 0  #the number of music in GB
        self.apps = 0  #the number of all files stored in GB
        self.__remaining = 0  #total storage remaining


class Henry(object):
    def __init__(self):
        self.pictures = 0  #the number of pictures in GB
        self.videos = 0  #the number of videos in GB
        self.documents = 0  #the number of documents in GB
        self.music = 0  #the number of music in GB
        self.total = 0  #the number of all files stored in GB
        self.__remaining = 0  #total storage remaining


class Tiffany(object):
    def __init__(self):
        self.pictures = 0  #the number of pictures in GB
        self.videos = 0  #the number of videos in GB
        self.documents = 0  #the number of documents in GB
        self.music = 0  #the number of music in GB
        self.apps = 0  #the number of all files stored in GB
        self.__remaining = 0  #total storage remaining


class Jason(object):
    def __init__(self):
        self.pictures = 0  #the number of pictures in GB
        self.videos = 0  #the number of videos in GB
        self.documents = 0  #the number of documents in GB
        self.music = 0  #the number of music in GB
        self.apps = 0  #the number of all files stored in GB
        self.__remaining = 0  #total storage remaining

        #now I am going to use a getter to do the calculations for me

        @property
        def final_storage(self):
            self.__remaining = 50 - (self.pictures + self.videos + self.documents + self.music + self.apps)  #do the math for the remaining storage
            return self.final_storage










app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
