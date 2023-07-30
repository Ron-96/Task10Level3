from django.apps import AppConfig


class onlinestoreConfig(AppConfig):
    """
    Configuration class for the 'onlinestore' Django app.

    This class is used to configure various settings and behavior specific to the
    'onlinestore' app. It inherits from the base AppConfig class provided by Django.

    :ivar default_auto_field: The default auto-generated field type to use for primary keys
                              in models. In this case, it is set to 'django.db.models.BigAutoField',
                              which means that Django will use a 64-bit integer for primary keys on models
                              created in this app.
    :vartype default_auto_field: str

    :ivar name: The name of the app. This attribute is used by Django to uniquely identify
                the app in the project and in various configurations. In this case, it is set to
                'onlinestore', which is the name of the Django app.
    :vartype name: str

    :Note:
        This class should be defined in the 'apps.py' file of the 'onlinestore' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onlinestore'
