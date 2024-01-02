import requests
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


def get_seo_reports():
    url = "http://127.0.0.1:8000/seo/"
    response = requests.get(url)
    res_json = response.json()
    seo_report = SEOReport.objects.create(
        title=res_json["title"],
        visits=res_json["visits"],
        all_expense=res_json["all_expense"],
        transactions=res_json["sum_transactions"],
        avg_check=res_json["avg_check"],
        income=res_json["income"],
    )
    seo_report.save()
    yandex_report = YandexSEOReport.objects.create(
        title=res_json["yandex"]["title"],
        visits=res_json["yandex"]["visits"],
        impressions=res_json["yandex"]["impressions"],
        ctr=res_json["yandex"]["ctr"],
        avg_position=res_json["yandex"]["avg_position"],
        convert=res_json["yandex"]["convert"],
        transactions=res_json["yandex"]["transactions"],
        category=SEOReport.objects.filter(title="SEO")[0],
    )
    yandex_report.save()
    google_report = GoogleSEOReport.objects.create(
        title=res_json["google"]["title"],
        visits=res_json["google"]["visits"],
        impressions=res_json["google"]["impressions"],
        ctr=res_json["google"]["ctr"],
        avg_position=res_json["google"]["avg_position"],
        convert=res_json["google"]["convert"],
        transactions=res_json["google"]["transactions"],
        category=SEOReport.objects.filter(title="SEO")[0],
    )
    google_report.save()
    direct_report = DirectSEOReport.objects.create(
        title=res_json["direct"]["title"],
        visits=res_json["direct"]["visits"],
        convert=res_json["direct"]["convert"],
        transactions=res_json["direct"]["transactions"],
        category=SEOReport.objects.filter(title="SEO")[0],
    )
    direct_report.save()
    refs_report = ReferralsSEOReport.objects.create(
        title=res_json["referrals"]["title"],
        visits=res_json["referrals"]["visits"],
        convert=res_json["referrals"]["convert"],
        transactions=res_json["referrals"]["transactions"],
        category=SEOReport.objects.filter(title="SEO")[0],
    )
    refs_report.save()
    return 0


def get_yandex_direct():
    url = "http://127.0.0.1:8000/yandex_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = YandexDirect.objects.create(
        title="YandexDirect",
        views=res_json["views"],
        visits=res_json["visits"],
        average_check=res_json["average_check"],
        ctr=res_json["ctr"],
        cta=res_json["cta"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_google_ads():
    url = "http://127.0.0.1:8000/google_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = GoogleAds.objects.create(
        title="GoogleAds",
        views=res_json["views"],
        visits=res_json["visits"],
        average_check=res_json["average_check"],
        ctr=res_json["ctr"],
        cta=res_json["cta"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_vk_ads():
    url = "http://127.0.0.1:8000/vk_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = VKAds.objects.create(
        title="VKAds",
        views=res_json["views"],
        visits=res_json["visits"],
        average_check=res_json["average_check"],
        ctr=res_json["ctr"],
        cta=res_json["cta"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_mytarget():
    url = "http://127.0.0.1:8000/vk_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = MyTarget.objects.create(
        title="MyTarget",
        views=res_json["views"],
        visits=res_json["visits"],
        average_check=res_json["average_check"],
        ctr=res_json["ctr"],
        cta=res_json["cta"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_facebook_ads():
    url = "http://127.0.0.1:8000/facebook_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = FacebookAds.objects.create(
        title="FacebookAds",
        views=res_json["views"],
        visits=res_json["visits"],
        average_check=res_json["average_check"],
        ctr=res_json["ctr"],
        cta=res_json["cta"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_insta_ads():
    url = "http://127.0.0.1:8000/facebook_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = InstagramAds.objects.create(
        title="InstagramAds",
        views=res_json["views"],
        visits=res_json["visits"],
        average_check=res_json["average_check"],
        ctr=res_json["ctr"],
        cta=res_json["cta"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_ads_reports():
    get_yandex_direct()
    get_google_ads()
    get_vk_ads()
    get_mytarget()
    get_facebook_ads()
    get_insta_ads()


def get_telegram_ads():
    url = "http://127.0.0.1:8000/telegram_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = TelegramAds.objects.create(
        title="TelegramAds",
        visits=res_json["visits"],
        convert=res_json["convert"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_email_tracking():
    url = "http://127.0.0.1:8000/email_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = EmailTracking.objects.create(
        title="EmailTracking",
        visits=res_json["visits"],
        convert=res_json["convert"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_call_tracking():
    url = "http://127.0.0.1:8000/call_ads/"
    response = requests.get(url)
    res_json = response.json()
    res = CallTracking.objects.create(
        title="CallTracking",
        visits=res_json["visits"],
        convert=res_json["convert"],
        transactions=res_json["transactions"],
        all_expense=res_json["all_expense"],
        income=res_json["income"],
    )
    res.save()


def get_other_reports():
    get_telegram_ads()
    get_email_tracking()
    get_call_tracking()


def dataloader():
    try:
        get_seo_reports()
        get_ads_reports()
        get_other_reports()
        print("Данные выгружены успешно")
    except e:
        print(e)
    return 0
