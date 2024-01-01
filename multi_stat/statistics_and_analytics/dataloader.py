import requests
from .models import SEOReport, SEOReportDetail


def get_seo_reports():
    url = "http://127.0.0.1:8000/seo/"
    response = requests.get(url)
    res_json = response.json()
    return 0


def get_ads_reports():
    pass


def get_other_reports():
    pass


def dataloader():
    try:
        get_seo_reports()
        get_ads_reports()
        get_other_reports()
    except e:
        print(e)
    return 0
