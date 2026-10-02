
import unittest

from api.app import app


class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertTrue(data["model_loaded"])

    def test_missing_image(self):
        response = self.client.post("/predict")

        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()