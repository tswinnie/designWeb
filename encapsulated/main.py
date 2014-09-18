'''
Tyrone Swinnie
9/16/14
Design for Web
Encapsulated Calculator
'''


import webapp2
from pages import Page  #importing the page class
from users import Storage  #importing the storage class



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
        m = Storage()
        m.pictures = 5
        m.videos = 10
        m.documents = 1
        m.music = 3
        m.apps = 4
        #write the values to the page
        self.response.write("this is the result " + str(m.final_storage)) #writing the user_page which has has all the html for my application












app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
