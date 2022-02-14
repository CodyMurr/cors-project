from django.core.management.base import BaseCommand
from ...models import Category
import requests


BASE_URL = "https://sephora.p.rapidapi.com/categories/list/"

HEADERS = {
    'x-rapidapi-host': "sephora.p.rapidapi.com",
    'x-rapidapi-key': "a458fc8e21msh8965fedee115759p1a7861jsn77b90d60b5d0"
}

def get_categories():
    querystring = {"categoryId": "cat150006"}
    response = requests.get(BASE_URL, headers=HEADERS, params=querystring).json()
    categories = response["childCategories"]
    return categories

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in get_categories():
            print(i["displayName"], i["categoryId"])
        self.stdout.write(self.style.SUCCESS("Complete"))
        