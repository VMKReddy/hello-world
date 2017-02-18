import webapp2

class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        
        self.response.out.write(""""
        <html>
        <head></head>
        <body>
        <h1>My Guest Book</h1>

        <form action="/greet" method="post">
            <p>
            Name: <input type="text" name="user_name" style="width:300px"> </input>
            </p>
            <p>
            Message: <textarea name="message" style ="width:300px"rows="5"></textarea>
            </p>
            <p>
            <input type= "submit" value="send">
            </p>
        </form>
        </body>
        </html>
        """)


app = webapp2.WSGIApplication([
    ('/', MainHandler),

], debug=True)

