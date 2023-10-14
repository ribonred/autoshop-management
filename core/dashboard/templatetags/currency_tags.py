from django import template
import locale

register = template.Library()


@register.filter(name="currency")
def currency(value):
    locale.setlocale(locale.LC_ALL, "id_ID.UTF-8")
    formatted_currency = locale.currency(value, grouping=True)
    return formatted_currency.replace("Rp", "Rp ")


@register.filter(name="trx_type_color")
def trx_type_color(value: str):
    match value.lower():
        case "debit":
            return "#50c878"
        case "credit":
            return "#db0015 "
        case _:
            return "#b9cbc9"
