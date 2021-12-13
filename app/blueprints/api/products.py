from stripe.api_resources import product
from .import bp as api
from flask import json, jsonify, current_app as app, request
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

@api.route('/product/<id>', methods=['GET'])
def get_product(id):
    """
    [GET] /api/product/<id>
    """
    print(id)
    # Send API call to stripe to retrieve the product's information
    product = stripe.Product.retrieve(id)

    # Add a price key and the value is another Stripe API request to get the product's price information (object)
    product['price'] = float(stripe.Price.retrieve(product['metadata']['price_id'])['unit_amount']) / 100

    # Sending that product data back to our React frontend as "data" 
    return jsonify(product)

@api.route('/shop/checkout', methods=['POST'])
def create_checkout():
    stripe.api_key = app.config.get('STRIPE_TEST_SK')

    # grab the list of cart data from the React frontend
    cart_data = request.get_json()['cartData']
    # print(cart_data)
    
    # build line items
    line_items = [dict(price=i['metadata']['price_id'], quantity=i['quantity']) for i in cart_data]

    # create the checkout session
    checkout = stripe.checkout.Session.create(
        success_url='http://localhost:3000/shop/products',
        cancel_url='http://localhost:3000/shop/products',
        line_items=line_items,
        mode="payment"
    )
    return jsonify({ 'checkout_session': checkout['url'] })