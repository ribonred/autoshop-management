from django import template
import locale

register = template.Library()


@register.filter(name="currency")
def currency(value):
    locale.setlocale(locale.LC_ALL, "id_ID.UTF-8")
    formatted_currency = locale.currency(value, grouping=True)
    return formatted_currency.replace("Rp", "Rp ")
