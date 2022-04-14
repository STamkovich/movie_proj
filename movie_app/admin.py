from django.contrib import admin
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Actor)


# admin.site.register(DressingRoom)

@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['actor', 'floor', 'number']


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', ' Низкий'),
            ('от 40 до 79', 'Средний'),
            ('>=80', 'Высокий'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 79':
            return queryset.filter(rating__gte=40).filter(rating__lte=79)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating'] - добавление в базу данных только с этими указанными полями
    # exclude = ['slug']  # исключение полей в бд
    # readonly_fields = ['year'] - запрещать изменять поля при добавлении записей в бд
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'year', 'director', 'budget', 'currency', 'slug', 'rating_status']
    list_editable = ['rating', 'year', 'budget', 'slug', 'currency', 'director', ]
    filter_horizontal = ['actors']
    ordering = ['-rating', 'name']
    actions = ['set_dollars', 'set_rubles', 'set_euro']
    search_fields = ['name__startswith']
    list_filter = ['name', 'currency', RatingFilter]

    # list_per_page = сколько должно отображаться объектов на страничке

    # @admin.display(ordering='rating', description='Статус') - для сортировки поля rating_status, и изменении его имени
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
