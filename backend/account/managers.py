from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy


class UserManager(BaseUserManager):
    def create_user(self, uuid, password, **info):

        if not uuid:
            raise ValueError(gettext_lazy("The uuid must be set"))
        user = self.model(uuid=uuid, **info)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, uuid, password, **info):

        info.setdefault("is_active", True)
        info.setdefault("role", "admin")

        if info.get("role") != "admin":
            raise ValueError(gettext_lazy("Superuser must have admin role"))

        return self.create_user(uuid, password, **info)
