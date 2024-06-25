from ext import app

if __name__ == '__main__':
    from routes import index, registration, authorization, saati,  watch, products, delete_product, create_product, logout, search, add_to_cart, cart, remove_from_cart, edit_product, delete_watch, brands
    app.run(debug=True)