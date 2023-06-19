from django import template
from django.utils import timezone

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter
def get_posted_at_display(posted_at):
    seconds_ago = (timezone.now() - posted_at).total_seconds()
    if seconds_ago <= HOUR:
        return "Publié il y a un instant."
    elif seconds_ago <= DAY:
        return f"Publié il y a {int(seconds_ago // HOUR)} heures."
    return f'Publié le {posted_at.strftime("%d %b %y à %Hh%M")}'


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context["user"]:
        return "Vous avez"
    return f"{user.username} a"


@register.filter(name="times")
def times(number):
    return range(number)
