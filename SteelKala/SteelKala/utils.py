import string
import random


def generate_random_digits(k, char=False):
    if char:
        return ''.join(random.choices(string.digits + string.ascii_lowercase, k=k))
    return ''.join(random.choices(string.digits, k=k))


def unique_slug_generator(model, slug):
    if model.objects.filter(slug=slug).exists():
        new_slug = slug + '-' + 'وبسایت-اسپیدوس' + '-' + generate_random_digits(5)
        return new_slug
    return slug


def slugify(char):
    if char:
        char = char.replace(' ', '-')
        char = char.replace(',', '')
        char = char.replace('?', '')
        char = char.replace('/', '')
        char = char.replace(':', '')
        char = char.replace('(', '')
        char = char.replace(')', '')
        return char.lower()


def convert_to_int(char):
    if char is not None:
        char = char.replace(",", "")
        return int(char)
    return 0


def convert_to_comma(char):
    if char is not None: 
        char = "{:,}".format(char)
        return char
    return 0