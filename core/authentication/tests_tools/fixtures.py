import factory
from pytest_factoryboy import register
from faker import Factory as FakerFactory
from core.authentication.models import User

faker = FakerFactory.create()

@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    email = factory.LazyAttribute(lambda _: faker.email())
    username = factory.LazyAttribute(lambda _: faker.name())
    is_staff = False
    is_active = True
    is_superuser = False
    password = factory.PostGenerationMethodCall('set_password', 'password')
    

    @classmethod
    def create_user(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

    @classmethod
    def create_superuser(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_superuser(*args, **kwargs)
