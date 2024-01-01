from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import SEOReport, SEOReportDetail


@login_required()
def analytics(request):
    return render(request, "statistics_and_analytics/analytics.html")
