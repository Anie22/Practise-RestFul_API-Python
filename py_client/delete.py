from typing import get_args
import requests

product_id = input('which id? \n')
try:
   product_id = int(product_id)
except: 
    product_id = None   
if product_id:
    endpoint = f"http://localhost:8000/api/product/delete/{product_id}/"

get_response = requests.delete(endpoint)