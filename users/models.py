from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    is_tenant = models.BooleanField(default=False)
    tenant_name = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        permissions = [
            ("can_edit_own_portfolio", "Can edit own portfolio"),
        ]

    def __str__(self):
        return self.username

    def has_edit_permission_for_portfolio(self):
        return self.has_perm('users.can_edit_own_portfolio')



def assign_permissions_to_user(user):
    content_type = ContentType.objects.get_for_model(CustomUser)
    permission = Permission.objects.get(codename='can_edit_own_portfolio', content_type=content_type)
    user.user_permissions.add(permission)
    user.save()

