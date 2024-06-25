from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, DateField, RadioField, SelectField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class RegisterForm(FlaskForm):
    profile_img = FileField("პროფილის სურათი", validators=[FileAllowed(["jpg", "png"], message="მხოლოდ სურათების ატვირთვა შიეძლება"), FileSize(1024*1024*5)])
    username = StringField("შეიყვანეთ იუზერნეიმი", validators=[DataRequired()])
    email = EmailField("შეიყვანეთ იმეილი", validators=[DataRequired()])
    password = PasswordField("ჩაწერეთ პაროლი", validators=[DataRequired(), Length(min=8, max=25, message="პაროლი უნდა იყოს 8 - 25 ასო")])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), EqualTo("password", message="პაროლები არ ემთხვევა")])
    birthday = DateField()
    region_number = SelectField(choices=["+995", "+577", "+994"], validators=[DataRequired()])
    phone_number = IntegerField("შეიყვანეთ ტელეფონის ნომერი", validators=[DataRequired()])
    gender = RadioField("მონიშნეთ სქესი", validators=[DataRequired()], choices =["კაცი", "ქალი"])
    country = SelectField(choices=["აირჩიეთ ქვეყანა", "USA", "Georgia", "UK"], validators=[DataRequired()])
    submit = SubmitField("რეგისტრაცია")


class AuthorizeForm(FlaskForm):
    name = StringField("შეიყვანეთ იუზერნეიმი", validators=[DataRequired()])
    passcode = PasswordField("ჩაწერეთ პაროლი", validators=[DataRequired(), Length(min=8, max=25, message="პაროლი უნდა იყოს 8 - 25 ასო")])
    repeat_passcode = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), EqualTo("passcode", message="პაროლები არ ემთხვევა")])

    submit1 = SubmitField("ავტორიზაცია")
    

class ProductForm(FlaskForm):
    img = FileField()
    product_name = StringField("პროდუქტის სახელი")
    product_price = IntegerField("პროდუქტის ფასი")

    submit_product = SubmitField("პროდუქტის ატვირთვა")
