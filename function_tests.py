import unittest
from selenium import webdriver

#browser = webdriver.Chrome('/Users/Leey/chromedriver')
#browser.implicitly_wait(3)
#browser.get('http://localhost:8000')

#assert '일정관리' in browser.title, "Browser title was" + browser.title

#browser.quit()


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/Leey/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('일정관리',self.browser.title)
        self.self.fail('테스트종료')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
