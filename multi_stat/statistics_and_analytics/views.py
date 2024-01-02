from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

    context = {
        "data": res_dict[page],
        "pages": ind,
    }
    return render(request, "statistics_and_analytics/analytics.html", context)
