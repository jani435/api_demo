# api_demo

Module to fetch prduct data like id, name, sale price, cost, quantity from given ID.
Steps to test:

1) Install module product_rest
2) For authentication hit the URL: /api/auth
3) After authentication is completed call URL: /api/product/<id>, with product id to get the product data
4) You will get data in following format:
  {"id": 20, "name": "Flipover", "cost": 1700.0, "sale_price": 1950.0, "quanity": 0.0, "category": "Office Furniture", "reference": "FURN_9001"}
