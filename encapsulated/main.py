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

        #now I will hard code the values for each data object
        m = Michele()
        m.pictures = 5
        m.videos = 10
        m.documents = 1
        m.music = 3
        m.apps = 4
        #write the values to the page
        self.response.write("this is the result " + str(m.final_storage)) #writing the user_page which has has all the html for my application


class Michele(object):
    def __init__(self):
        self.pictures = 0  #the number of pictures in GB
        self.videos = 0  #the number of videos in GB
        self.documents = 0  #the number of documents in GB
        self.music = 0  #the number of music in GB
        self.apps = 0  #the number of all files stored in GB
        self.__remaining = 0  #total storage remaining




    @property
    def final_storage(self):
            self.__remaining = 50 - (self.pictures + self.videos + self.documents + self.music + self.apps)  #do the math for the remaining storage
            return self.__remaining

        #now I will set up my setter

    @final_storage.setter
    def final_storage(self, new_final_storage):
            pass  # not using my setter right now











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
