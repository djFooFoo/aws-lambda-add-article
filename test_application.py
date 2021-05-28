import unittest

import application


class TestApplication(unittest.TestCase):
    def test_application_returns_message(self):
        result = application.handler(None, None)

        self.assertEqual('Hello darkness my old friend', result['body'])

    def test_application_returns_ok(self):
        result = application.handler(None, None)

        self.assertEqual(200, result['statusCode'])


if __name__ == '__main__':
    unittest.main()