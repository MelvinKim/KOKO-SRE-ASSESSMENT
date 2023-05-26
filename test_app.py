import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_homepage(self):
        response = self.app.get("/home")
        # assert that response status code = 200
        self.assertEqual(response.status_code, 200)
        # assert that the response body contains the content we expect
        self.assertEqual(response.data.decode('utf-8'), 'My name is Melvin Kimathi and I love Backend and Site Reliability Engineering.')
        
if  __name__ == '__main__':
    unittest.main()