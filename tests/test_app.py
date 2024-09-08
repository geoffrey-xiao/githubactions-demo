# tests/test_app.py
import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_index_template(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Hello, World!</h1>', response.data)

    def test_404(self):
        response = self.app.get('/non-existent-page')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
