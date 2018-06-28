from django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
from ..read_count.utils import get_seven_days_read_data

def home(request):
    blog_content_type = ContentType.objects.get_for_model()
    read_nums = get_seven_days_read_data()
    context = {}
    context['read_nums'] = read_nums
    return render_to_response('../templates/home.html0', context)