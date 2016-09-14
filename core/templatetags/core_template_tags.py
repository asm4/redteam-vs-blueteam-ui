from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def current_path(context):
    return context['request'].path


@register.simple_tag(takes_context=True)
def is_logged_in(context):
    request = context['request']
    return request.user.is_authenticated()
