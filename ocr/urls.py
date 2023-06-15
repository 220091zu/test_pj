from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("ocr/", views.ListOcrView.as_view(), name="list-ocr"),
    path("ocr/<int:pk>/detail/", views.DetailOcrView.as_view(), name="detail-ocr"),
    path("ocr/create/", views.CreateOcrView.as_view(), name="create-ocr"),
    path("ocr/<int:pk>/delete/", views.DeleteOcrView.as_view(), name="delete-ocr"),
    path("ocr/<int:pk>/update/", views.UpdateOcrView.as_view(), name="update-ocr"),
]