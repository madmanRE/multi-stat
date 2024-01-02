from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
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


@login_required()
@cache_page(60 * 60)
def analytics(request, page):
    seo = SEOReport.objects.all()[:10]
    ya_d = YandexDirect.objects.all()[:10]
    go_a = GoogleAds.objects.all()[:10]
    vk_a = VKAds.objects.all()[:10]
    fb_a = FacebookAds.objects.all()[:10]
    in_a = InstagramAds.objects.all()[:10]
    my_t = MyTarget.objects.all()[:10]
    tg_a = TelegramAds.objects.all()[:10]
    em_t = EmailTracking.objects.all()[:10]
    ca_t = CallTracking.objects.all()[:10]
    ind = [i for i in range(1, len(seo) + 1)]
    dates = list(map(lambda d: d.strftime("%Y-%m-%d"), [s.created for s in seo]))
    data = list(
        zip(
            seo,
            ya_d,
            go_a,
            vk_a,
            fb_a,
            in_a,
            my_t,
            tg_a,
            em_t,
            ca_t,
        )
    )
    res_dict = {}
    for i in range(len(seo)):
        res_dict.update({ind[i]: data[i]})

    context = {"data": res_dict[page], "pages": list(zip(ind, dates))}
    return render(request, "statistics_and_analytics/analytics.html", context)


@login_required()
@cache_page(60 * 60)
def seo_detail_view(request, page):
    ya = YandexSEOReport.objects.all()[:10]
    go = GoogleSEOReport.objects.all()[:10]
    dr = DirectSEOReport.objects.all()[:10]
    rf = ReferralsSEOReport.objects.all()[:10]

    ind = [i for i in range(1, len(ya) + 1)]
    dates = list(map(lambda d: d.strftime("%Y-%m-%d"), [s.created for s in ya]))

    data = list(zip(ya, go, dr, rf))

    res_dict = {}

    for i in range(len(ya)):
        res_dict.update({ind[i]: data[i]})

    context = {"data": res_dict[page], "pages": list(zip(ind, dates))}
    return render(request, "statistics_and_analytics/seo-detail.html", context)


@login_required
@cache_page(60 * 60)
def ads_detail(request, page):
    ya_d = YandexDirect.objects.all()[:10]
    go_a = GoogleAds.objects.all()[:10]
    vk_a = VKAds.objects.all()[:10]
    fb_a = FacebookAds.objects.all()[:10]
    in_a = InstagramAds.objects.all()[:10]
    my_t = MyTarget.objects.all()[:10]
    ind = [i for i in range(1, len(ya_d) + 1)]
    dates = list(map(lambda d: d.strftime("%Y-%m-%d"), [s.created for s in ya_d]))

    data = list(
        zip(
            ya_d,
            go_a,
            vk_a,
            fb_a,
            in_a,
            my_t,
        )
    )

    res_dict = {}
    for i in range(len(ya_d)):
        res_dict.update({ind[i]: data[i]})

    context = {"data": res_dict[page], "pages": list(zip(ind, dates))}
    return render(request, "statistics_and_analytics/ads-report.html", context)


@login_required
@cache_page(60 * 60)
def other_detail(request, page):
    tg_a = TelegramAds.objects.all()[:10]
    em_t = EmailTracking.objects.all()[:10]
    ca_t = CallTracking.objects.all()[:10]
    ind = [i for i in range(1, len(tg_a) + 1)]
    dates = list(map(lambda d: d.strftime("%Y-%m-%d"), [s.created for s in tg_a]))

    data = list(
        zip(
            tg_a,
            em_t,
            ca_t,
        )
    )

    res_dict = {}
    for i in range(len(tg_a)):
        res_dict.update({ind[i]: data[i]})

    context = {"data": res_dict[page], "pages": list(zip(ind, dates))}
    return render(request, "statistics_and_analytics/other-ads-report.html", context)


@login_required
@cache_page(60 * 60)
def dataloading_dates(request):
    seo = SEOReport.objects.all()
    ya_d = YandexDirect.objects.all()
    go_a = GoogleAds.objects.all()
    vk_a = VKAds.objects.all()
    fb_a = FacebookAds.objects.all()
    in_a = InstagramAds.objects.all()
    my_t = MyTarget.objects.all()
    tg_a = TelegramAds.objects.all()
    em_t = EmailTracking.objects.all()
    ca_t = CallTracking.objects.all()

    data = list(
        zip(
            seo,
            ya_d,
            go_a,
            vk_a,
            fb_a,
            in_a,
            my_t,
            tg_a,
            em_t,
            ca_t,
        )
    )

    dates = [d.created for d in tg_a]
    res_dict = {}

    for i in range(len(dates)):
        current_data = data[i]
        current_data_res = [(x.income - x.all_expense) for x in current_data]
        res_dict.update({str(dates[i]): sum(current_data_res)})

    context = {"data": res_dict.items()}
    return render(request, "statistics_and_analytics/all-dates.html", context)


@login_required()
@cache_page(60 * 60)
def analytics_for_date(request, date):
    res_date = date.split(".")[0]
    seo = SEOReport.objects.filter(created__contains=res_date).first()
    ya_d = YandexDirect.objects.filter(created__contains=res_date).first()
    go_a = GoogleAds.objects.filter(created__contains=res_date).first()
    vk_a = VKAds.objects.filter(created__contains=res_date).first()
    fb_a = FacebookAds.objects.filter(created__contains=res_date).first()
    in_a = InstagramAds.objects.filter(created__contains=res_date).first()
    my_t = MyTarget.objects.filter(created__contains=res_date).first()
    tg_a = TelegramAds.objects.filter(created__contains=res_date).first()
    em_t = EmailTracking.objects.filter(created__contains=res_date).first()
    ca_t = CallTracking.objects.filter(created__contains=res_date).first()

    data = [
        seo,
        ya_d,
        go_a,
        vk_a,
        fb_a,
        in_a,
        my_t,
        tg_a,
        em_t,
        ca_t,
    ]

    context = {"data": data}
    return render(request, "statistics_and_analytics/analytics.html", context)
