from django.contrib import admin
from .models import SEOReport, SEOReportDetail


@admin.register(SEOReport)
class SEOReportAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "visits",
        "all_expense",
        "sum_transactions",
        "avg_check",
        "income",
        "created",
    ]


@admin.register(SEOReportDetail)
class SEOReportDetailAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "visits",
        "impressions",
        "ctr",
        "avg_position",
        "convert",
        "transactions",
        "created",
        "category",
    ]
