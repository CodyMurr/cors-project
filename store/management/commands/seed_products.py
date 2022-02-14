from django.core.management.base import BaseCommand
from ...models import Product
import requests

BASE_URL = "https://sephora.p.rapidapi.com/products/"

HEADERS = {
    'x-rapidapi-host': "sephora.p.rapidapi.com",
    'x-rapidapi-key': "a458fc8e21msh8965fedee115759p1a7861jsn77b90d60b5d0"
}   

def get_products():
    querystring = {"categoryId":"cat150006","pageSize":"60","currentPage":"1"}
    response = requests.get(f'{BASE_URL}list', headers=HEADERS, params=querystring).json()
    products = response["products"]
    return products

def product_detail(pId, skuId):
    querystring = {"productId":pId,"preferedSku":skuId}
    response = requests.get(f'{BASE_URL}detail', headers=HEADERS, params=querystring).json()
    return response

class Command(BaseCommand):
    def handle(self, *args, **options):
        # for i in get_products():
        #     detail = product_detail(i["productId"], i["currentSku"]["skuId"])
        #     product = Product(
        #         category = detail["parentCategory"]["parentCategory"]["displayName"],
        #         product_name = detail["brand"]["displayName"],
        #         slug = detail["brand"]["displayName"],
        #         description = detail["quickLookDescription"],
        #         price = float(detail["currentSku"]["listPrice"][1:]),
        #         product_images = detail["currentSku"]["skuImages"]["image135"],
        #         stock = 100
        #     )
        #     product.save()
            
        self.stdout.write(self.style.SUCCESS("Complete"))
