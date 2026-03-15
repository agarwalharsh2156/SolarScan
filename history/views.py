from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from detections.models import Detections

class HistoryListView(LoginRequiredMixin, ListView):
    model = Detections
    template_name = 'history/list.html'
    context_object_name = 'scans'
    paginate_by = 10

    def get_queryset(self):
        return Detections.objects.filter(user=self.request.user).order_by('-created_at')