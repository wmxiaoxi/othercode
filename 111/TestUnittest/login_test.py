import unittest

from Test_data.login_data import *
from framework.login_action import *


class TestLogin(unittest.TestCase):

    def test_success(self):
        test_login(usevalue[0],passvalue[0],message[0],mesele[0],mesele[1])
        #method.quit_browser()
    def test_failname(self):
        test_login(usevalue[1],passvalue[0],message[1],mesele1[0],mesele1[1])

    def test_failpass(self):
        test_login(usevalue[0], passvalue[1], message[1], mesele1[0], mesele1[1])

    def test_nameempty(self):
        test_login('', passvalue[0], message[2], mesele2[0], mesele2[1])

    def test_passempty(self):
        test_login(usevalue[0], '', message[3], mesele3[0], mesele3[1])

if __name__ == "__main__":
    unittest.main()


