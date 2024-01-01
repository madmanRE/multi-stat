from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


# -----------------SEO--------------------


class ChanelSEOTraffic(BaseModel):
    title: str
    visits: int
    impressions: Optional[int] = None
    ctr: Optional[float] = None
    avg_position: Optional[float] = None
    convert: float
    transactions: int


class YandexSEO(ChanelSEOTraffic):
    pass


class GoogleSEO(ChanelSEOTraffic):
    pass


class DirectSEO(ChanelSEOTraffic):
    pass


class ReferralsSEO(ChanelSEOTraffic):
    pass


class SEO(BaseModel):
    title: str
    visits: int
    all_expense: int
    sum_transactions: int
    avg_check: int
    income: int
    yandex: YandexSEO
    google: GoogleSEO
    direct: DirectSEO
    referrals: ReferralsSEO


# -----------------Yandex Direct / Google Ads--------------------


class Ads(BaseModel):
    average_check: int
    views: int
    visits: int
    ctr: float
    cta: int
    transactions: int
    all_expense: int
    income: int


class YandexDirect(Ads):
    pass


class GoogleAds(Ads):
    pass


class VKAds(Ads):
    pass


class FacebookAds(Ads):
    pass


# -----------------Other Channels--------------------


class Channel(BaseModel):
    visits: int
    transactions: int
    convert: float
    all_expense: int
    income: int


class TelegramAds(Channel):
    pass


class EmailTracking(Channel):
    pass


class CallTracking(Channel):
    pass
