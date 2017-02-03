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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.write_form()
        
    def post(self):
        
        correct = userval(self.request.get('username'))
        alsocorrect = passval((self.request.get('passwd')),(self.request.get('verify')))
        thirdlycorrect = userval(self.request.get('passwd'))
        if correct and alsocorrect and thirdlycorrect:
#            self.response.out.write(yes)
            self.redirect("/wel")
        if not correct:
            uvalfail = "That's not a valid username."
        else:
            uvalfail = ""
        if not alsocorrect:
            matchfail = "Your password entries do not match."
        else:
            matchfail = ""
        if not thirdlycorrect:
            passwval = "That's not a valid password"
        else:
            passwval = ""
        self.write_form(uvalfail, passwval, matchfail)    
#        if correct and alsocorrect and thirdlycorrect:
#            self.response.out.write(yes)
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
        

import re
user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def userval(username):
    return user_re.match(username)
    
def passval(passwd,verpass):
    return passwd == verpass

#def write_form(self, error=""):
#    self.response.out.write(SignupForm % {"ivuser": error})
        
  
       
SignupForm = """
<h3>Signup</h3>
<form method="post" action='/wel'>
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
