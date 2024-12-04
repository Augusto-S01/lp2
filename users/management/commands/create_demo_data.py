from django.core.management.base import BaseCommand
from users.models import CustomUser
from portfolio.models import Portfolio


class Command(BaseCommand):
    help = "Cria dados de demonstração no banco de dados."

    def handle(self, *args, **kwargs):

        user = CustomUser.objects.create_user(
            username="profissional1",
            password="123456",
            is_tenant=True
        )


        user.first_name = "João"
        user.last_name = "Silva"
        user.email = "joao@exemplo.com"
        user.tenant_name = "profissional1"  #
        user.save()


        portfolio = Portfolio.objects.create(
            user=user,
            title="Portfólio de João Silva",
            description="Psicólogo com 10 anos de experiência."
        )


        portfolio.save()


        self.stdout.write(self.style.SUCCESS("Dados de demonstração criados com sucesso!"))
