from django.contrib import admin
from .models import (
    SEOReport,
    YandexSEOReport,
    GoogleSEOReport,
    DirectSEOReport,
    ReferralsSEOReport,
    YandexDirect,
    GoogleAds,
    VKAds,
    FacebookAds,
    InstagramAds,
    MyTarget,
    TelegramAds,
    EmailTracking,
    CallTracking,
)


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


@admin.register(GoogleSEOReport)
class GoogleSEOReportAdmin(admin.ModelAdmin):
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


@admin.register(YandexSEOReport)
class YandexSEOReportAdmin(admin.ModelAdmin):
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


@admin.register(DirectSEOReport)
class DirectSEOReportAdmin(admin.ModelAdmin):
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


@admin.register(ReferralsSEOReport)
class ReferralsSEOReportAdmin(admin.ModelAdmin):
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


@admin.register(YandexDirect)
class YandexDirectAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "views",
        "visits",
        "average_check",
        "ctr",
        "cta",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(GoogleAds)
class GoogleAdsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "views",
        "visits",
        "average_check",
        "ctr",
        "cta",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(VKAds)
class VKAdsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "views",
        "visits",
        "average_check",
        "ctr",
        "cta",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(FacebookAds)
class FacebookAdsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "views",
        "visits",
        "average_check",
        "ctr",
        "cta",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(InstagramAds)
class InstagramAdsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "views",
        "visits",
        "average_check",
        "ctr",
        "cta",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(MyTarget)
class MyTargetAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "views",
        "visits",
        "average_check",
        "ctr",
        "cta",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(TelegramAds)
class TelegramAdsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "visits",
        "convert",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(EmailTracking)
class EmailTrackingAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "visits",
        "convert",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]


@admin.register(CallTracking)
class CallTrackingAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "visits",
        "convert",
        "transactions",
        "all_expense",
        "income",
        "created",
    ]
    list_filter = ["all_expense", "income"]
