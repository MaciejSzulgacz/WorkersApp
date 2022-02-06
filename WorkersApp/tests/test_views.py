from django.test import TestCase
from django.urls import reverse
from ..models import Worker


class TestViews(TestCase):
    def setUp(self):
        Worker.objects.create(name="John", surname="Smith", age=25, profession="mechanic", picture="mechanic.jpg")
        Worker.objects.create(name="Jack", surname="Bridge", age=30, profession="seller", picture="seller.jpg")

    def test_home(self):
        # when
        response = self.client.get(reverse('home'))

        # then
        self.assertEqual(200, response.status_code)

    def test_worker_list(self):
        # when
        response = self.client.get(reverse('worker-list'))

        # then
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.context['object_list']))

    def test_worker_details(self):
        # given
        name = 'John'
        worker = Worker.objects.get(name=name)

        # when
        response = self.client.get(reverse('worker-detail', kwargs={'pk': worker.id}))

        # then
        self.assertEqual(200, response.status_code)
        self.assertEqual(name, response.context['object'].name)

    def test_worker_create(self):
        # when
        response = self.client.get(reverse('worker-create'))

        # then
        self.assertEqual(200, response.status_code)

    def test_worker_update(self):
        # given
        worker = Worker.objects.get(name='John')

        # when
        response = self.client.get(reverse('worker-update', kwargs={'pk': worker.id}))

        # then
        self.assertEqual(200, response.status_code)

    def test_worker_delete(self):
        # given
        worker = Worker.objects.get(name='Jack')

        # when
        response = self.client.get(reverse('worker-delete', kwargs={'pk': worker.id}))

        # then
        self.assertEqual(200, response.status_code)
