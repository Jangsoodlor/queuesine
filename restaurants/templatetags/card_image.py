from django import template
from django.templatetags.static import static

register = template.Library()


def _get_card_image_context(default_path: str, image, alt="", aspect_ratio="1 / 1"):
    return {
        "image": image,
        "alt": alt,
        "default_image": static(default_path),
        "aspect_ratio": aspect_ratio,
    }


@register.inclusion_tag("restaurants/includes/card_image.html")
def restaurant_card_image(image, alt=""):
    return _get_card_image_context("images/restaurant.jpg", image, f"{alt} Restaurant")


@register.inclusion_tag("restaurants/includes/card_image.html")
def menu_card_image(image, alt=""):
    return _get_card_image_context("images/food.jpg", image, alt, "16/9")
