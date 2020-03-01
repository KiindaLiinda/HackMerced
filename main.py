import json
import jinja2
import os
import webapp2

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#Homepage Handler
class HomepageHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("/index.html")
        self.response.write(start_template.render())
class SignupHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("/SignUp.html")
        self.response.write(start_template.render())
class AboutusHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("/aboutus.html")
        self.response.write(start_template.render())

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomepageHandler), #this maps the root url to the Main Page Handler
    ('/signup', SignupHandler),
    ('/aboutus', AboutusHandler)
], debug=True)
