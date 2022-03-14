from django.template.loader import render_to_string

from myapi.models import Film

prices = {"one_cof": 4, "one_exte": 5, "card_cof": 30, "card_exte": 35}


def render_com(template_name, film: Film) -> str:
    return render_to_string(template_name, {"film": film, "prices": prices})


def bocal(film: Film) -> str:
    return render_com("bocal.tex", film)


def facebook(film: Film) -> str:
    return render_com("facebook.txt", film)


def mail(film: Film) -> str:
    return render_com("mail.html", film)
