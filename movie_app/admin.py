from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'currency', 'slug', 'rating_status']
    list_editable = ['rating', 'year', 'budget', 'slug', 'currency']
    ordering = ['name', 'rating']
    actions = ['set_dollars', 'set_rubles', 'set_euro']

    # list_per_page = сколько должно отображаться объектов на страничке

    @staticmethod
    def rating_status(mov: Movie):
        if mov.rating < 50:
            return "Зачем это смотреть"
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 88:
            return 'Зачёт'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей'
        )

    @admin.action(description='Установить валюту в рублях')
    def set_rubles(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.RUB)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей',
        )

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей'
        )
