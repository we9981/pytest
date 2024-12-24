import tornado.ioloop #导入 Tornado 框架中的相关模块
import tornado.web #导入 Tornado 框架中的相关模块
#定义子类 MainHandler
class MainHandler(tornado.web.RequestHandler):
  def get(self): #定义请求业务函数get()
    self.write("这是第一个 Tornado 程序") #输出文本
def make_app(): #定义应用配置函数
  return tornado.web.Application([
    (r"/", MainHandler), #定义 URL 映射列表
  ])
if __name__ == "__main__":
  app = make_app() #调用配置函数
  app.listen(8888) #设置监听服务器 8888 端口
  tornado.ioloop.IOLoop.current().start() #使用方法 start()启动服务器

# 访问，http://localhost:8888