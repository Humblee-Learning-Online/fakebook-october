from stripe.api_resources import product
from .import bp as api
from flask import jsonify, current_app as app
import stripe

@api.route('/products', methods=['GET'])
def get_products():
    """
    [GET] /api/products
    """
    stripe.api_key = app.config.get('STRIPE_TEST_SK')
    productData = [p for p in stripe.Product.list()['data']]
    for i in productData:
        i['price'] = float(stripe.Price.retrieve(i['metadata']['price_id'])['unit_amount']) / 100
    return jsonify([i for i in productData])