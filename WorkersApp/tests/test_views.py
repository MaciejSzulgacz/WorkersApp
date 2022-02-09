from django.test import TestCase
from django.urls import reverse

from ..models import Worker


class TestViews(TestCase):
    def setUp(self):
        Worker.objects.create(name="John", surname="Smith", age=28, profession="seller", picture="seller.jpg",)
        Worker.objects.create(name="Joe", surname="Bridge", age=25, profession="mechanic", picture="mechanic.jpg",)

    def test_home(self):
        # when
        response = self.client.get(reverse("home"))

        # then
        self.assertEquals(200, response.status_code)

    def test_worker_list(self):
        # when
        response = self.client.get(reverse("worker-list"))

        # then
        self.assertEquals(200, response.status_code)
        self.assertEquals(2, len(response.context["object_list"]))

    def test_worker_details(self):
        # given
        name = "John"
        worker = Worker.objects.get(name=name)

        # when
        response = self.client.get(reverse("worker-detail", kwargs={"pk": worker.id}))

        # then
        self.assertEquals(200, response.status_code)
        self.assertEquals(name, response.context["object"].name)

    def test_worker_create(self):
        # when
        response = self.client.get(reverse("worker-create"))

        # then
        self.assertEquals(200, response.status_code)

    def test_worker_update(self):
        # given
        worker = Worker.objects.get(name="John")

        # when
        response = self.client.get(reverse("worker-update", kwargs={"pk": worker.id}))

        # then
        self.assertEquals(200, response.status_code)
