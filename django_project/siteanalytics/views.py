# from django.shortcuts import render
from django.shortcuts import render
from .models import Visitor


def site_analytics_view(request):
    return render(
        request, "siteanalytics/site_analytics.html", {"visitors": Visitor.objects.all()}
    )
