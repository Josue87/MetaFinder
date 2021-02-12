class GoogleCaptcha(Exception):
    def __init__(self, *args):
        self.data = "Google Captcha detected"
        if args:
            self.data = args[0]
    def  __str__(self):
        return "GoogleCaptcha, {0}".format(self.data)

class BaiduDetection(Exception):
    def __init__(self, *args):
        self.data = "Baidu detected"
        if args:
            self.data = args[0]
    def  __str__(self):
        return "BaiduDetection, {0}".format(self.data)