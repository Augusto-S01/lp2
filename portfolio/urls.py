
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
    path('portfolio/<int:portfolio_id>/contato/', views.portfolio_contato, name='portfolio_contato'),
    path('portfolio/<int:portfolio_id>/agenda/' , views.portfolio_agenda, name='portfolio_agenda'),
    path('portfolio/<int:portfolio_id>/faq/', views.portifolio_faq, name='portfolio_faq'),
    path('portfolio/<int:portfolio_id>/feedback/', views.portfolio_feedback, name='portfolio_feedback'),
]
