import webapp2

class Mainpage(webapp2.requestHandler);
	def get(self);
	self.response.headers('Content-Type') - 'text/plain'
	self.response.out.write('Hello, Udacity!')

app = webpapp2.WSGIApplication([('/',MainPage)]),
								debug = True)