from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Овощи', 'category_title': 'Свежие'},
            {'category_name': 'Фрукты', 'category_title': 'Вкусные'},
            {'category_name': 'Хлебобулочные изделия', 'category_title': 'Не ломаются об стол'},
            {'category_name': '	Замороженные продукты', 'category_title': 'Были когда-то не замороженными'},
            {'category_name': '	Кисломолочный продукт', 'category_title': 'Продукты от парнокопытных'},
        ]

        # for product in category_list:
        #     Category.objects.create(**product)

        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))
        Category.objects.bulk_create(category_for_create)