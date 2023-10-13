import pytest
import structlog
from django.contrib.auth import authenticate

logger = structlog.get_logger("test")


@pytest.mark.django_db
def test_user_factory(user_factory):
    user = user_factory.create()
    assert user.email
    assert user.username
    assert user.password
    assert user.is_active
    logger.debug("test_user_factory", user=user.email)


@pytest.mark.django_db
def test_user_authentication(user_factory):
    email = "red@email.com"
    pwd = "password"
    username = "red"
    user_factory.create(email=email, password=pwd, username=username)
    user = authenticate(username=email, password=pwd)
    logger.debug(
        "test_user_authentication",
        is_authenticated=user.is_authenticated,
        user=user.email,
    )
    assert user
    assert user.email == email
    # authenticate with username
    user = authenticate(username=username, password=pwd)
    assert user
    assert user.email == email  