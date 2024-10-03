# data/urls.py
from django.urls import path
from .views import upload_csv, CSVDataListView

urlpatterns = [
    path('data-excel/', upload_csv, name='upload-csv'),
    path('data-excel/list/', CSVDataListView.as_view(), name='list-csv-data'),
]
