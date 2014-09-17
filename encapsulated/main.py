'''
Tyrone Swinnie
9/16/14
Design for Web
Encapsulated Calculator
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Tyrone')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
