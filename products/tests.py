from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class ProductAPITest(APITestCase):

    def test_create_product(self):

        data = {
            "name": "Laptop",
            "description": "Dell Laptop",
            "price": "55000.00"
        }

        response = self.client.post(
            '/api/products/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_products(self):

        response = self.client.get('/api/products/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )