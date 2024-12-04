from django.contrib import admin
from .models import Portfolio, SecaoDescritiva, SecaoCarrosel, SecaoVideo, FAQ, Feedback

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'created_at', 'is_tenant')
    search_fields = ('title', 'user__username')
    list_filter = ('is_tenant',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs

class SecaoDescritivaAdmin(admin.ModelAdmin):
    list_display = ('title', 'portfolio', 'order', 'created_at')
    search_fields = ('title', 'portfolio__title')
    list_filter = ('portfolio',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(portfolio__user=request.user)
        return qs

class SecaoCarroselAdmin(admin.ModelAdmin):
    list_display = ('title', 'portfolio', 'order', 'created_at')
    search_fields = ('title', 'portfolio__title')
    list_filter = ('portfolio',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(portfolio__user=request.user)
        return qs

class SecaoVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'portfolio', 'order', 'created_at')
    search_fields = ('title', 'portfolio__title')
    list_filter = ('portfolio',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(portfolio__user=request.user)
        return qs


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'portfolio', 'created_at')
    search_fields = ('question', 'answer')
    list_filter = ('portfolio',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(portfolio__user=request.user)
        return qs

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'portfolio', 'rating', 'date')
    search_fields = ('name', 'comment', 'portfolio__title')
    list_filter = ('portfolio', 'rating')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(portfolio__user=request.user)
        return qs

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(SecaoDescritiva, SecaoDescritivaAdmin)
admin.site.register(SecaoCarrosel, SecaoCarroselAdmin)
admin.site.register(SecaoVideo, SecaoVideoAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Feedback, FeedbackAdmin)
