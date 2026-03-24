from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from detections.models import Detections

class HistoryListView(LoginRequiredMixin, ListView):
    model = Detections
    template_name = 'history/list.html'
    context_object_name = 'scans'
    paginate_by = 10

    def get_queryset(self):
        return Detections.objects.filter(user=self.request.user).order_by('-created_at')


@login_required
@require_http_methods(["POST"])
def delete_scan(request, scan_id):
    try:
        scan = Detections.objects.get(id=scan_id, user=request.user)
        scan.delete()
        return JsonResponse({'status': 'success', 'message': 'Scan deleted successfully'})
    except Detections.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Scan not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)