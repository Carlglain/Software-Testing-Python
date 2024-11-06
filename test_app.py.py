# import unittest
# from app import app

# class FlaskAppTestCase(unittest.TestCase):
#     def setUp(self):
#         # Create a test client
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_home(self):
#         # Send a GET request to the home page
#         response = self.app.get('/')
        
#         # Check if the status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)
        
#         # Check if the response data is as expected
#         self.assertEqual(response.json, {"message": "Hello level 400 FET, Quality Assurance!"})

# if __name__ == '__main__':
#     unittest.main()

# lecturers version
# test_app.py
import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello level 400 FET, Quality Assurance!"})


if __name__ == '__main__':
    unittest.main()