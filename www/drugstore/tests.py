from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from drugstore.models import Drug


# Create your tests here.
class BaseToken(APITestCase):

    def get_token(self):
        """
        Test token creation
        :return:
        """
        url = reverse('token_obtain')
        token = self.client.get(url, format='json')
        return token.data['token']


class DrugTests(BaseToken):

    def test_get_drugs(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('drugs_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class VaccinationTests(BaseToken):

    @classmethod
    def setUpTestData(cls):
        """
        Create a default drug for test foreign vaccination
        :return:
        """
        cls.drugs = Drug.objects.create(name='drug_test', code='ASDFGHJ', description='desc_drug_test')

    def test_success_post_vaccination(self):
        """
        Test POST a success new vaccination
        """
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('vaccination_list')
        data = {
            "rut": "11111111-1",
            "dose": 0.5,
            "date": "2020-08-10",
            "drug": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_error_drug_post_vaccination(self):
        """
        Test POST a error on fk drug new vaccination
        """
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('vaccination_list')
        data = {
            "rut": "12345678-0",
            "dose": "1",
            "date": "2020-08-10",
            "drug": 4
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_rut_post_vaccination(self):
        """
        Test POST a error on rut new vaccination
        """
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('vaccination_list')
        data = {
            "rut": "12345678-Ñ",
            "dose": 1,
            "date": "2020-08-10",
            "drug": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_dose_vaccination(self):
        """
        Test POST a error on dose new vaccination
        """
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('vaccination_list')
        data = {
            "rut": "11111111-1",
            "dose": 0.14,
            "date": "2020-08-10",
            "drug": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_date_post_vaccination(self):
        """
        Test POST a error on date new vaccination
        """
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('vaccination_list')
        data = {
            "rut": "11111111-1",
            "dose": 1,
            "date": "2020-13-10",
            "drug": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenTests(APITestCase):
    def test_create_token(self):
        """
        Test token creation
        """
        url = reverse('token_obtain')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
