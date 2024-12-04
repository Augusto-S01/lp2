from django.db import models
from users.models import CustomUser
from django.utils import timezone

class Portfolio(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_tenant = models.BooleanField(default=False)

    professional_name = models.CharField(max_length=100, blank=True)  # Novo campo para o nome do profissional

    instagram_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question


class Feedback(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='feedbacks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.portfolio.title} by {self.name}"

class Secao(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['order']

class SecaoDescritiva(Secao):
    content = models.TextField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='secoes_descritivas')

    class Meta:
        verbose_name = "Seção Descritiva"
        verbose_name_plural = "Seções Descritivas"

class SecaoCarrosel(Secao):
    images = models.JSONField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='secoes_carrosel')

    class Meta:
        verbose_name = "Seção Carrosel"
        verbose_name_plural = "Seções Carrosel"

class SecaoVideo(Secao):
    video_url = models.URLField()
    description = models.TextField(blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='secoes_video')

    class Meta:
        verbose_name = "Seção de Vídeo"
        verbose_name_plural = "Seções de Vídeo"
