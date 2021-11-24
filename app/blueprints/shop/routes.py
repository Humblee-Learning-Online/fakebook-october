from flask.templating import render_template
from werkzeug.utils import redirect
from .import bp as shop
from .models import Product
from flask import redirect, url_for, flash

@shop.route('/')
def index():

    context = {
        'products': Product.query.all()
    }
    return render_template('shop/index.html', **context)

@shop.route('/product/add/<id>')
def add_product(id):
    print(id)
    flash('Product added successfully', 'success')
    return redirect(url_for('shop.index'))