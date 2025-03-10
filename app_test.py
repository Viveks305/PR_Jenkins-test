from app import app

import unittest
import json

class CitiesTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/cities.json', content_type='application/json')
    self.assertEqual(response.status_code, 200)
    #print(response.data.decode('unicode_escape'))
    self.assertEqual(response.data.decode('unicode_escape'), json.dumps(['Amsterdam', 'San Franci', 'Berlin', 'New York']))

if __name__ == '__main__':
    unittest.main()
