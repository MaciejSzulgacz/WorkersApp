import pytest

from ..models import Worker


@pytest.mark.django_db
def test_worker_create():
    Worker.objects.create(name="John", surname="Smith", age=28, profession="seller", picture="seller.jpg")
    assert Worker.objects.count() == 1
