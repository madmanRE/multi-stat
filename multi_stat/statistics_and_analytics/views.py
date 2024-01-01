from django.shortcuts import render


def analytics(request):
    return render(request, "statistics_and_analytics/analytics.html")
