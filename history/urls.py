from django.urls import path
from .views import HistoryListView, delete_scan

urlpatterns = [
    path('', HistoryListView.as_view(), name='history_list'),
    path('delete/<uuid:scan_id>/', delete_scan, name='delete_scan'),
]