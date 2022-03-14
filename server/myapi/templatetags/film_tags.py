from datetime import timedelta
from django import template
from typing import List
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def color_display(in_color: bool) -> str:
    res = "Couleur" if in_color else "Noir & Blanc"
    return mark_safe(res)


@register.simple_tag
def list_actors(actors: List[str]) -> str:
    res = ", ".join(actors[:3])
    if len(actors) > 3:
        res += "..."
    return res


@register.filter
def movie_duration(value: timedelta) -> str:
    s = value.total_seconds()
    str_duration = f"{int(s // 3600):01d}h{int(s % 3600 // 60):02d}"
    return mark_safe(str_duration)
