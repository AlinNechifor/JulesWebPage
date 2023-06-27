from browser import Browser
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.sign_up_page = SignUpPage()


# - De fiecare data cand adaugam cate o pagian noua in Fisierul pages, o sa trebuiasca sa-l adaugam si aici in Environment.

def after_all(context):
    context.browser.close()