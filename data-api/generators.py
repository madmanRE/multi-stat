import schemas
import random

# -----------------SEO--------------------


def yandex_seo():
    impress = random.randint(1500, 2500) * random.randint(500, 1000)
    ctr = round((random.randint(1, 6) * 0.01), 3)
    convert = random.randint(1, 2) * 0.001
    report = schemas.YandexSEO(
        title="yandex",
        visits=int(impress * ctr),
        impressions=impress,
        ctr=ctr,
        avg_position=random.randint(10, 20),
        convert=round(convert, 5),
        transactions=int(impress * ctr * convert),
    )
    return report


def google_seo():
    impress = random.randint(1500, 2500) * random.randint(500, 1000)
    ctr = round((random.randint(1, 6) * 0.01), 3)
    convert = random.randint(1, 2) * 0.001
    report = schemas.GoogleSEO(
        title="google",
        visits=int(impress * ctr),
        impressions=impress,
        ctr=ctr,
        avg_position=random.randint(10, 20),
        convert=round(convert, 5),
        transactions=int(impress * ctr * convert),
    )
    return report


def direct_seo():
    visits = random.randint(800, 1500)
    convert = random.randint(6, 12) * 0.001
    report = schemas.DirectSEO(
        title="direct",
        visits=visits,
        convert=round(convert, 5),
        transactions=int(visits * convert),
    )
    return report


def referrals_seo():
    visits = random.randint(850, 1350)
    convert = random.randint(4, 8) * 0.001
    report = schemas.ReferralsSEO(
        title="referrals",
        visits=visits,
        convert=round(convert, 5),
        transactions=int(visits * convert),
    )
    return report


def gen_seo_report():
    yandex = yandex_seo()
    google = google_seo()
    direct = direct_seo()
    referrals = referrals_seo()
    sum_transactions = yandex.transactions
    +google.transactions
    +direct.transactions
    +referrals.transactions
    visits = yandex.visits + google.visits + direct.visits + referrals.visits
    seo_report = schemas.SEO(
        title="SEO",
        visits=visits,
        all_expense=random.randint(180000, 250000),
        sum_transactions=sum_transactions,
        avg_check=4000,
        income=sum_transactions * 4000,
        yandex=yandex,
        google=google,
        direct=direct,
        referrals=referrals,
    )
    return seo_report


# -----------------Ads--------------------


def gen_ads_report():
    trans = random.randint(100, 120)
    visits = random.randint(1000, 1500)
    cta = random.randint(150, 330)
    exp = visits * cta
    ads_report = schemas.Ads(
        average_check=4000,
        views=(random.randint(1500, 2500) * 500),
        visits=visits,
        ctr=round((random.randint(1, 6) * 0.1), 3),
        cta=cta,
        transactions=trans,
        all_expense=exp,
        income=trans * 4000,
    )
    return ads_report


# -----------------Others--------------------


def gen_other_report():
    other_channels = schemas.Channel(
        visits=random.randint(300, 800),
        transactions=random.randint(2, 10),
        convert=(random.randint(4, 10) * 0.01),
        all_expense=random.randint(20000, 50000),
        income=(random.randint(10, 50) * random.randint(180, 280)) * 10,
    )
    return other_channels
