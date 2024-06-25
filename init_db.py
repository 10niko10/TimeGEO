from ext import app, db
from models import Product, Watch, User

with app.app_context():

    db.drop_all()
    db.create_all()

    admin_user = User(username = "admin", password = "admingoat", role = "Admin")
    admin_user.create()

watches = [
    { "title": "Citizen", "name": "Citizen CITIZEN AUTOMATIC WATCH/NJ0150-81Z", "price":  1569, "img": "/static/images/saati1.jpg", "id": 0 },
    { "title": "Casio", "name": "CASIO EDIFICE QUARTZ WRISTWATCH MEN/EFR-S108D-2AVUDF", "price":  529, "img": "/static/images/saati2.png", "id": 1},
    { "title": "Casio", "name": "QUARTZ WRISTWATCH/LTP-V007L-7B1UDF", "price":  109, "img": "/static/images/saati3.jpg", "id": 4 },
    { "title": "Casio", "name": "CASIO GENERAL QUARTZ WATCH WOMEN/LW-205H-8ADF", "price": 155, "img": "/static/images/saati4.png", "id": 3},
    { "title": "CLUSE", "name": "Cluse Quartz Watch Women/CW11220", "price": 399, "img": "/static/images/saati5.png", "id": 11},
    { "title": "PANDORA", "name": "PANDORA Moments Bracelet / 590719-18", "price": 215, "img": "/static/images/pandora1.jpg", "id": 5},
    { "title": "Citizen", "name": "AUTOMATIC WRISTWATCH/NJ0150-81A", "price": 1549, "img": "/static/images/saati6.jpg", "id": 6},
    { "title": "D1 Milano", "name": "QUARTZ WRISTWATCH/D1-ATBJ12", "price": 2499, "img": "/static/images/saati7.png", "id": 7},
    { "title": "TOUS", "name": "Bracelet/112721533", "price": 625, "img": "/static/images/tous1.png", "id": 8},
    { "title": "EDOX", "name": "Automatic Wristwatch/80131 3NM NIB", "price": 4799, "img": "/static/images/saati9.jpg", "id": 9},
    { "title": "Casio", "name": "Quartz wristwatch/ECB-10P-1ADF", "price": 579, "img": "/static/images/saati10.jpg", "id": 10},
    { "title": "PANDORA", "name": "Ring/188421C01-60F", "price": 359, "img": "/static/images/pandora2.jpg", "id": 2},
]

with app.app_context():
    for watch in watches:
        new_watch = Watch(
            id=watch["id"],
            title=watch["title"],
            name=watch["name"],
            price=watch["price"],
            img=watch["img"]
        )
        db.session.add(new_watch)

    db.session.commit()

    
