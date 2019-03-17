import tornado.ioloop
import tornado.web

class indexHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello,Qz Data Graph ...")

class qzHandler(tornado.web.RequestHandler):
  def get(self,rps):
    self.write("spi@date0@date1@01",rps)

application=tornado.web.Application([
(r"/",indexHandler),
(r"/qz/([0-9]+)",qzHandler),
])

if __name__=="__main__":
  application.listen(8081)
  tornado.ioloop.IOLoop.instance().start()


