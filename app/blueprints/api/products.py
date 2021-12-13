from stripe.api_resources import product
from .import bp as api
from flask import jsonify, current_app as app, request, redirect, url_for
import stripe
from flask_cors import cross_origin

@api.route('/products', methods=['GET'])
@cross_origin()
def get_products():
    """
    [GET] /api/products
    """
    stripe.api_key = app.config.get('STRIPE_TEST_SK')
    productData = []
    for p in stripe.Product.list()['data']:
        product_info = {
            'id': p.id,
            'image': p.images[0],
            'name': p.name,
            'price_id': p['metadata']['price_id'],
            'price_value': float(stripe.Price.retrieve(p['metadata']['price_id'])['unit_amount']) / 100,
            'description': p.description,
        }
        productData.append(product_info)
    return jsonify([i for i in productData])