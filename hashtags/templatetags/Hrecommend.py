from django import template
from hashtags import models

register = template.Library()



@register.inclusion_tag("snippets/Hrecommend.html")

def Hrecommend(limit_to=10):
	tags = models.HashTag.objects.all().order_by("?")[:limit_to]
	return {"tags": tags}