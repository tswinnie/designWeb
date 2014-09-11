'''
Tyrone Swinnie
Design for Web Programming
9/10/14
Simple Form Assignment
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # Create the page so that I can create a form
        # create the form inside the html code like I normally would in an HTML document

        page_head = '''<!DOCTYPE HTML>
<html>
<head>
<title>Welcome to my landing page</title>
<link href='http://fonts.googleapis.com/css?family=Lato:300,400,300italic,400italic' rel='stylesheet' type='text/css'>
<style type="text/css">


</style>
'''
        page_body = '''
<body>
<div class="container">
<form method ="GET" action="">
<h2 id="titleText">We are Coming Soon!</h2>
<label>First Name:</label><input type="text" name="first" /><br>
<label>Last Name:</label><input type="text" name="last" /><br>
<label>Email:</label><input type="text" name="email" /><br>



<label>How Did You Hear About Us?:</label><select name="aboutus">
  <option  value="Online" >Online</option>
    <option  value="Friend" >Friend</option>
        <option  value="Other" >Other</option>
</select>
<br>
<label>How Excited Are About This Site?:</label><select name="excited">
  <option  value="not really" > Not Really</option>
    <option  value="a little" >A Little</option>
        <option  value="very excited" >Very Excited</option>
</select>
<label>Send Me Email Updates:</label><input type="checkbox" name= "updates" value="send updates" /><br>

<br>
<input id="submit" type="submit" value="submit" />
<h3 id="confirmation">Your Confirmation</h3>




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
            self.response.write(page_head + page_body + first_name + ' ' + last_name + ' ' + email + ' ' + about_us + ' ' + excited + ' ' + updates + page_close)
        else:
            # if the user does not input any values then do this
            self.response.write(page_head + page_body + page_close)

















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
