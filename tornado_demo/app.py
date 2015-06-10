# coding:utf-8
import os
import tornado.ioloop
import tornado.web
import tornado.gen
import sdk.geetestmsg as geetestmsg


BASE_URL = "api.geetest.com/get.php?gt="

captcha_id = "a40fd3b0d712165c5d13e6f747e948d4"
private_key = "0f1a37e33c9ed10dd2e133fe2ae9c459"
product = "embed"


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("static/login.html")

    def post(self, *args, **kwargs):
        phone = self.get_argument("phone")
        challenge = self.get_argument("geetest_challenge")
        validate = self.get_argument("geetest_validate")
        seccode = self.get_argument("geetest_seccode")
        gt = geetestmsg.geetest(captcha_id, private_key)
        res = gt.send_request(challenge, validate, seccode, phone)
        self.write(str(res))


if __name__ == "__main__":
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }
    app = tornado.web.Application([
                                      (r"(.+)", MainHandler),
                                  ], debug=True, **settings)

    app.listen(8008)
    tornado.ioloop.IOLoop.instance().start()
