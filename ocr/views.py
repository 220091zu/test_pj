from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Ocr

# Create your views here.
class ListOcrView(ListView):
    template_name = "ocr/ocr_list.html"
    model = Ocr

class DetailOcrView(DetailView):
    template_name = "ocr/ocr_detail.html"
    model = Ocr

class CreateOcrView(CreateView):
    template_name ="ocr/ocr_create.html"
    model = Ocr
    fields = ("company",
              "location",
              "employee",
              "sales_amount",
              "company_url",
              "listed",
              "work_time",
              "work_hours",
              "over_time",
              "basic_salary",
              "bonus_salary",
              "holiday",
              "on_site")
    success_url = reverse_lazy("list-ocr")

class DeleteOcrView(DeleteView):
    template_name = "ocr/ocr_confirm_delete.html"
    model = Ocr
    success_url = reverse_lazy("list-ocr")
    
class UpdateOcrView(UpdateView):
    model = Ocr
    fields = ("company",
              "location",
              "employee",
              "sales_amount",
              "company_url",
              "listed",
              "work_time",
              "work_hours",
              "over_time",
              "basic_salary",
              "bonus_salary",
              "holiday",
              "on_site")
    template_name = "ocr/ocr_update.html"
    success_url = reverse_lazy("list-ocr")

def index_view(request):
    object_list = Ocr.objects.all()
    return render(request, "ocr/index.html", {"object_list":object_list})