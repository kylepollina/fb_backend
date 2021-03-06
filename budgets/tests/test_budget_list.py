# budgets/test_budget_list.py

import pytest
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from budgets.api.views import BudgetViewSet

@pytest.mark.django_db
class TestBudgetList(TestCase):
    """ Budget List test
        -------------------- 
        test_budget_list
    """
    
    def setUp(self):
        self.client = APIClient()

        # register users for use in login tests
        register_url = reverse('register')
        user_1 = {
            'email': 'test@gmail.com',
            'phone': '1',
            'password': 'test_pass',
            'first_name': 'first',
            'last_name': 'last'
        }
        response = self.client.post(register_url, user_1, format='json')
        access_token = response.data['tokens']['access token']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)


    def test_budget_list(self):
        # this is how to obtain the url of an action from a viewset
        view = BudgetViewSet()
        view.basename = 'budgets'
        view.request = None
        budget_list_url = view.reverse_action('list')

        response = self.client.get(budget_list_url)
        assert response.status_code == HTTP_200_OK












    # def test_budget_create(self):
    #     budget_create_url = reverse('budgets:budgets-create')

    #     valid_data = {
    #         'name': 'new budget',
    #         'limit': 20.50
    #     }
    
    #     self.client.post(budget_create_url, data, format='json')
    #     assert response.status_code == HTTP_201_CREATED
    #     assert response.data['name'] == 'new budget'
    #     assert response.data['limit'] == 20.50
