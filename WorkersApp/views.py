import csv

from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import WorkerCreateForm
from .models import Worker


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


class WorkerCreateView(CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("worker-list")


class WorkerDetailView(DetailView):
    model = Worker


class WorkerListView(ListView):
    model = Worker


class WorkerUpdateView(UpdateView):
    template_name = "WorkersApp/worker_update.html"
    model = Worker
    fields = ["name", "surname", "age", "profession", "picture"]
    success_url = reverse_lazy("worker-list")


class WorkerDeleteView(DeleteView):
    model = Worker
    success_url = reverse_lazy("worker-list")


def download_report(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="worker_list.csv"'

    file_writer = csv.writer(response, delimiter=",")
    file_writer.writerow(["Profession", "Average age"])

    professions_list = Worker.objects.values_list("profession", flat=True).distinct()

    for profession in professions_list:
        profession_avg = Worker.objects.filter(profession=profession).aggregate(Avg("age"))["age__avg"]
        file_writer.writerow(([profession, profession_avg]))

    return response
