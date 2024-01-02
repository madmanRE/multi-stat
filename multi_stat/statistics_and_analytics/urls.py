from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    analytics,
    seo_detail_view,
    ads_detail,
    other_detail,
    dataloading_dates,
    analytics_for_date,
)

app_name = "saa"

urlpatterns = (
    [
        path("seo-report/<int:page>/", seo_detail_view, name="seo_report"),
        path("other-ads-report/<int:page>/", other_detail, name="other_ads_report"),
        path("ads-report/<int:page>/", ads_detail, name="ads_report"),
        path("dashboard/<int:page>/", analytics, name="analytics"),
        path("dataloading-dates/", dataloading_dates, name="dates"),
        path("analytic-for-date/<str:date>/", analytics_for_date, name="a_for_dates"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
