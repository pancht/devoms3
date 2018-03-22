from random import choice
from selenium.webdriver.common.keys import Keys

class Variables:
    def AddProject(self):
        longitud = 4
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        p = ""
        self.p = p.join([choice(valores) for i in range(longitud)])