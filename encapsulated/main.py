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
        self.response.write('Hello Tyrone')

        p = Page()
        p.title = "My New Page"
        p.css = "css/styles.css"
        p.body = "This is a test of the text"
        p.update()
        self.response.write(p.user_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
