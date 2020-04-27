import unittest
from .models import News
from .models import Source


class NewsTest(unittest.TestCase):
    '''
    Test class to test the news class
    '''

    def setUp(self):
        '''
        set up method that will run everything before every test
        '''
        self.new_news = News('flask', 'python','python is okay','http://newsapi.org/v2/top-headlines?','2001-01-02')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


class SourceTest(unittest.TestCase):
    '''
    test class for the sources class
    '''

    def setUp(self):

        self.new_source = Source('citizen','i am trying')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))



if __name__ == '__main__':
    unittest.main() 