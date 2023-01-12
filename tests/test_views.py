from django.test import TestCase
from django.urls import reverse
from restaurant.views import MenuItemsView
from restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        # Create 10 menu items for tests
        menu_items = []
        for i in range(10):
            menu_items.append(
                MenuItem.objects.create(
                    title=f"menu item # {i}", price=(1 + i) * 10, inventory=(1 + i) * 10
                )
            )

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)