import tornado.ioloop
import tornado.web

class indexHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello,Qz Data Graph ...")

class qzHandler(tornado.web.RequestHandler):
  def get(self,rps):
    self.write("spi@date0@date1@01: "+rps)

class qz2Handler(tornado.web.RequestHandler):
  def get(self,rps):
    self.write("get data from redis to draw:"+rps)

application=tornado.web.Application([
(r"/",indexHandler),
(r"/qz/([0-9]{5}-[0-9]-[0-9]{4}@20[0|1][0-9]-[0-9]{,2}-[0-9]{,2}@20[0-1][0-9]-[0-9]{,2}-[0-9]{,2}@01)",qzHandler),
(r"/qz2/(.+)",qz2Handler),
])

if __name__=="__main__":
  print "launch web 8081 ..."
  application.listen(8081)
  tornado.ioloop.IOLoop.instance().start()


