'''
Tyrone Swinnie
Design for Web
Final Project: Application with API
9/22/14
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')
        p = Page()
        self.response.write(p.print_out())

# I am going to create my page class

class Page(object):
    def __init__(self):

        self._head = '''

<!DOCTYPE HTML>

<html>

    <head>

        <title></title>

    </head>
    <body> '''

        self._body = ''
        self._close = '''

    </body>

</html>

        '''

    def print_out(self):
        return self._head + self._body + self._close







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
