
import unittest
from run import app

class DictionaryTest(unittest.TestCase):

    dictionary = app.test_client()

    def test_1_home(self):

        result = self.dictionary.get('/', content_type='html/text')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(b'ENGLISH POCKET DICTIONARY' in result.data)
        
    def test_2_word_check(self):

        response = self.dictionary.post('/dictionary', data={'word' : 'posh'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'noun' in response.data)
        self.assertTrue(b'associated with the upper classes' in response.data)
        self.assertFalse(b'verb' in response.data)

    def test_3_word_not_found(self):

        response = self.dictionary.post('/not_found', data={'word' : 'shjkashgj'}, follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Your word cannot be found' in response.data)

if __name__ == '__main__':
    unittest.main()