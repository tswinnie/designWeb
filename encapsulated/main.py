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
        self.response.write("Michel has  " + str(m.final_storage) + " GB of storage remaining") #writing the user_page which has has all the html for my application

    #now I am going create the remaining users

        #now I will hard code the values for each data object
        t = Storage()
        t.pictures = 10
        t.videos = 10
        t.documents = 1
        t.music = 20
        t.apps = 7
        #write the values to the page
        self.response.write(" <br/> Todd has  " + str(t.final_storage) + " GB of storage remaining") #writing the user_page which has has all the html for my application


#now I will hard code the values for each data object
        n = Storage()
        n.pictures = 1
        n.videos = 4
        n.documents = 1
        n.music = 9
        n.apps = 7
        #write the values to the page
        self.response.write(" <br/> Nancy has  " + str(n.final_storage) + " GB of storage remaining") #writing the user_page which has has all the html for my application


#now I will hard code the values for each data object
        h = Storage()
        h.pictures = 18
        h.videos = 10
        h.documents = 1
        h.music = 6
        h.apps = 7
        #write the values to the page
        self.response.write(" <br/> Henry has  " + str(h.final_storage) + " GB of storage remaining") #writing the user_page which has has all the html for my application


#now I will hard code the values for each data object
        j = Storage()
        j.pictures = 6
        j.videos = 4
        j.documents = 1
        j.music = 7
        j.apps = 2
        #write the values to the page
        self.response.write(" <br/> Jason has  " + str(j.final_storage) + " GB of storage remaining") #writing the user_page which has has all the html for my application











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
