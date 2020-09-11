#Basic custom controller without any custom app

import json
from odoo import http, exceptions
from odoo.http import request

#Function to create product data dict from recordset
def get_product_dict(product):
    res = {
        "id": product.id,
        "name": product.name,
        "cost": product.standard_price,
        "sale_price": product.list_price,
        "quanity": product.qty_available,
        "category": product.categ_id.name,
        "reference": product.default_code,
    }
    return res

class Product(http.Controller):
    #Authentication process
    @http.route('/api/auth', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, db, login, password):
        if db and login and password:
            request.session.authenticate(db, login, password)
            return json.dumps(request.env['ir.http'].session_info())
        return json.dumps({'error': 'Invalid Credentials or DB name'})
    
    #Browse record based on id parameter and return json
    @http.route('/api/product/<id>', type="http", auth='user')
    def get_product(self, id=None, **kw):
        if id:
            try:
                product = request.env['product.template'].browse(int(id))
                if product:
                    res = get_product_dict(product)
                    return json.dumps(res)
            except Exception as e:
                return json.dumps({'error': 'Product ID not found'})

