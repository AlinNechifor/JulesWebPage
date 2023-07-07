from browser import Browser
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage
from pages.forgot_password_page import ForgotPassword


def before_all(context):
    context.browser = Browser() # initializam pagina browser
    context.login_page = LoginPage() # initializam pagina login_page
    context.sign_up_page = SignUpPage() #initializam pagina sign_up_page
    context.forgot_password_page = ForgotPassword()


# - De fiecare data cand adaugam cate o pagian noua in Fisierul pages, o sa trebuiasca sa-l adaugam si aici in Environment.

def after_all(context):
    context.browser.close()