#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.write_form()
        
    def post(self):
        
        uservalidated = userval(self.request.get('username'))
        passwordmatch = passval((self.request.get('passwd')),(self.request.get('verify')))
        passwordvalidated = userval(self.request.get('passwd'))
        if uservalidated and passwordmatch and passwordvalidated:
#            self.response.out.write(yes)
            self.redirect("/wel")
        if not uservalidated:
            uvalfail = "That's not a valid username."
        else:
            uvalfail = ""
        if not passwordmatch:
            matchfail = "Your password entries do not match."
        else:
            matchfail = ""
        if not passwordvalidated:
            passwval = "That's not a valid password"
        else:
            passwval = ""
        self.write_form(uvalfail, passwval, matchfail)    


    def write_form(self, uval="", pval="", mval =""):
        UN = self.request.get('username')
        self.response.out.write(SignupForm % {"ivuser": uval, "ivpass": pval, "nomatch": mval, "uname": UN})

class wpage(webapp2.RequestHandler):
    def post(self):
        UN = self.request.get('username')
        message = "Welcome, %s" % UN
        self.response.out.write(message)
    
yes = "all good"
no = "no"
#class FormVerify(webapp2.RequestHandler):
#    def post(self):
#        uver = self.request.get("username")
#        self.response.out.write(uver)
        



def userval(username):
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(username)
    
def passval(passwd,verpass):
    return passwd == verpass

#def write_form(self, error=""):
#    self.response.out.write(SignupForm % {"ivuser": error})
        
  
       
SignupForm = """
<h3>Signup</h3>
<form method="post" action='/'>
    <label>
        Username
        <input name="username" value = "%(uname)s">
        
    </label> <div style="color: red">%(ivuser)s</div>
    
    <label>
        Password
        <input type="password" name="passwd">
        
    </label> <div style="color: red">%(ivpass)s</div>
    
    <label>
        Verify Password
        <input type="password" name="verify">
        
    </label> <div style="color: red">%(nomatch)s</div>
    
    <label>
        Email (Optional)
        <input name="email">
    </label><br>
    
    <input type="submit">
</form>    
"""

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/wel', wpage)
], debug=True)
