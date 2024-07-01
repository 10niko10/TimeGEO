from flask import render_template, redirect, flash, request, session
from os import path
from forms import RegisterForm, AuthorizeForm, ProductForm
from ext import app, db
from models import Product, Watch, User
from flask_login import login_user, logout_user, current_user, login_required

profiles = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/saati/<int:watch_id>")
def watch(watch_id):
    watch = Watch.query.get_or_404(watch_id)
    return render_template('watch_details.html', watch=watch)


@app.route('/search')
def search():
    query = request.args.get('query')
    watches = Watch.query.filter(Watch.name == query).all()
    return render_template('result.html', watches=watches)

@app.route('/registration', methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("ეს იუზერნეიმი უკვე გამოყენებულია, გთხოვთ შეცვალეთ")
        else:
            new_user = User(username=form.username.data, password=form.password.data)
            new_user.create()
            return redirect('/authorization')
    return render_template('registration.html', form=form)
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/authorization', methods=["GET", "POST"])
def authorization():
    form = AuthorizeForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.name.data).first()
        if user:
            login_user(user)
            return redirect('/')
    return render_template('authorization.html', form=form)


@app.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template('products.html', products=products, role=current_user.role)

@app.route('/products/<int:product_id>')
@login_required
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_details.html', product=product)

@app.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    product = Product.query.get(product_id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/products')


@app.route("/saati")
def saati():
    watches = Watch.query.all()
    return render_template('saati.html', watches=watches)

@app.route("/create_product", methods=["GET", "POST"])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
            new_product = Product(name = form.product_name.data, price = form.product_price.data)

            image = form.img.data
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)

            new_product.img = image.filename

            db.session.add(new_product)
            db.session.commit()
            return redirect('/products')
            

    return render_template("create_products.html", form=form)


@app.route('/add_to_cart/<int:watch_id>', methods=["POST"])
def add_to_cart(watch_id):
    watch = Watch.query.get_or_404(watch_id)
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append({
        'id': watch.id,
        'title': watch.title,
        'name': watch.name,
        'price': watch.price,
        'img': watch.img
    })
    session.modified = True
    return redirect('/saati')

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@app.route('/remove_from_cart/<int:watch_id>', methods=["POST"])
def remove_from_cart(watch_id):
    if 'cart' in session:
        cart = session['cart']
        cart = [item for item in cart if item['id'] != watch_id]
        session['cart'] = cart
        session.modified = True

    return redirect('/cart')

@app.route("/edit_product/<int:product_id>", methods=["POST", "GET"] )
@login_required
def edit_product(product_id):
    product= Product.query.get(product_id)
    form= ProductForm(name=product.name, price=product.price)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.save()
        return redirect("/products")
    return render_template("create_products.html", form=form)

@app.route('/delete_watch/<int:watch_id>')
@login_required
def delete_watch(watch_id):
    watch = Watch.query.get_or_404(watch_id)

    db.session.delete(watch)
    db.session.commit()

    return redirect('/saati')

@app.route('/brands')
def brands():
    watches = Watch.query.all()
    return render_template('brands.html', watches=watches)


