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
body{
font-family: 'Lato', sans-serif;

}

html {
  background: url(images/background.png) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}

.container{

width: 300px !important;
height: 265px !important;
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


.submitBTN{

border: none;
width: 150px;
height: 35px;
margin-left: 24%;
margin-top: 19px;
background: #4b93ff;
border-radius: 2px !important;
color: #fff;
box-shadow: none !important;

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

}

</style>
'''
        page_body = '''
<body>
        <h2 id="titleText">We are Coming Soon!</h2>

<div class="boxRight">

<p class="topText">We are bringing the latest technology to you and developers alike. We will change the world and how it thinks aboutweb development.</p>
<p class="topText">If you would like to know more about this new technology, please fill out the form and we will be in touch.</p>
</div>

<div class="container">
<form method ="GET" action="">
<label class="topLabel">First Name:</label><input type="text" name="first" class= "userName" /><br>
<label class="bottomLabel">Last Name:</label><input type="text" name="last"  class= "userName"/><br>
<label class="bottomLabel">Email:</label><input type="text" name="email" class= "userName" /><br>



<label class="bottomLabel">How Did You Hear About Us?:</label><select name="aboutus" class= "userName">
  <option  value="Online" >Online</option>
    <option  value="Friend" >Friend</option>
        <option  value="Other" >Other</option>
</select>
<br>
<label class="bottomLabel">How Excited Are About This Site?:</label><select name="excited" class= "userName">
  <option  value="not really" > Not Really</option>
    <option  value="a little" >A Little</option>
        <option  value="very excited" >Very Excited</option>
</select>
<label class="bottomLabel">Send Me Email Updates:</label><input type="checkbox" name= "updates" value="send updates"  style="position: relative; left: 39px;"/><br>

<br>
<input id="submit" type="submit" value="submit" class="submitBTN" />




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






# created a class that will hold my page for me


#
#         p = Page()
#         self.response.write(p.print_out())
#
#
# class Page(object):
#     def __init__(self):
#         self.title = "Welcome Tyrone"
#         self.css = "css/styles.css"
#         self.head = """
# <!DOCTYPE HTML>
#
# <html>
#     <head>
#         <title>{self.title}</title>
#     </head>
#     <link href="{self.css}" rel="stylesheet" type="text/css" />
#     <link href='http://fonts.googleapis.com/css?family=Lato:300,400,300italic,400italic' rel='stylesheet' type='text/css'>
#
#     <body>
#         """
#         self.body = """
#         <h2 id="titleText">We are Coming Soon!</h2>
#
# <div class="boxRight">
#
# <p>We are bringing the latest technology to you and developers alike. We will change the world and how it thinks aboutweb development.</p>
# <p>If you would like to know more about this new technology, please fill out the form and we will be in touch.</p>
# </div>
#
# <div class="container">
# <form method ="GET" action="">
# <label class="topLabel">First Name:</label><input type="text" name="first" class= "userName" /><br>
# <label class="bottomLabel">Last Name:</label><input type="text" name="last"  class= "userName"/><br>
# <label class="bottomLabel">Email:</label><input type="text" name="email" class= "userName" /><br>
#
#
#
# <label class="bottomLabel">How Did You Hear About Us?:</label><select name="aboutus" class= "userName">
#   <option  value="Online" >Online</option>
#     <option  value="Friend" >Friend</option>
#         <option  value="Other" >Other</option>
# </select>
# <br>
# <label class="bottomLabel">How Excited Are About This Site?:</label><select name="excited" class= "userName">
#   <option  value="not really" > Not Really</option>
#     <option  value="a little" >A Little</option>
#         <option  value="very excited" >Very Excited</option>
# </select>
# <label class="bottomLabel">Send Me Email Updates:</label><input type="checkbox" name= "updates" value="send updates"  style="position: relative; left: 39px;"/><br>
#
# <br>
# <input id="submit" type="submit" value="submit" class="submitBTN" />
#
#
#
#
#         """
#         self.close = """
#
#     </body>
#
# </html>
#
#
#
#         """
#
# #now I am going to get the data from the user
#
#         first_name = self.request.GET['first']  # this gets the value for the first name
#         last_name = self.request.GET['last']  # this gets the last name value
#         email = self.request.GET['email']  # this gets the email value from the user
#
#
#
#
#     def print_out(self):
#         all = self.head + self.body + self.close
#         all = all.format(**locals())
#         return all
#
#
#












app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
