from django.db import models


class SEOReport(models.Model):
    title = models.CharField(max_length=100, default="SEO", verbose_name="Название")
    visits = models.PositiveIntegerField(default=0, verbose_name="Визиты")
    all_expense = models.PositiveIntegerField(default=0, verbose_name="Расход")
    transactions = models.PositiveIntegerField(default=0, verbose_name="Заявки")
    avg_check = models.PositiveIntegerField(default=0, verbose_name="Средний чек")
    income = models.PositiveIntegerField(default=0, verbose_name="Доход")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "SEO отчет"
        verbose_name_plural = "SEO отчеты"
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]


class SEOReportDetail(models.Model):
    title = models.CharField(max_length=100, default="-----", verbose_name="Название")
    visits = models.PositiveIntegerField(default=0, verbose_name="Визиты")
    impressions = models.PositiveIntegerField(
        default=0, blank=True, null=True, verbose_name="Показы"
    )
    ctr = models.DecimalField(
        default=0,
        verbose_name="CTR",
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=10,
    )
    avg_position = models.DecimalField(
        default=0,
        blank=True,
        null=True,
        verbose_name="Средняя позиция",
        decimal_places=2,
        max_digits=10,
    )
    convert = models.DecimalField(
        default=0,
        blank=True,
        null=True,
        verbose_name="Конверсия",
        decimal_places=3,
        max_digits=15,
    )
    transactions = models.PositiveIntegerField(default=0, verbose_name="Заявки")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "SEOReport",
        on_delete=models.CASCADE,
        related_name="report",
        verbose_name="Канал трафика",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "SEO отчет детально"
        verbose_name_plural = "SEO отчеты детально"
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]


class YandexSEOReport(SEOReportDetail):
    class Meta:
        verbose_name = "SEO Яндекс отчет"
        verbose_name_plural = "SEO Яндекс отчеты"
        ordering = ["-created"]


class GoogleSEOReport(SEOReportDetail):
    class Meta:
        verbose_name = "SEO Google отчет"
        verbose_name_plural = "SEO Google отчеты"
        ordering = ["-created"]


class DirectSEOReport(SEOReportDetail):
    class Meta:
        verbose_name = "SEO Прямые заходы отчет"
        verbose_name_plural = "SEO Прямые заходы отчеты"
        ordering = ["-created"]


class ReferralsSEOReport(SEOReportDetail):
    class Meta:
        verbose_name = "SEO Ссылочные заходы отчет"
        verbose_name_plural = "SEO Ссылочные заходы отчеты"
        ordering = ["-created"]


class Ads(models.Model):
    title = models.CharField(max_length=100, default="-----", verbose_name="Название")
    average_check = models.PositiveIntegerField(default=0, verbose_name="Средний чек")
    views = models.PositiveIntegerField(default=0, verbose_name="Показы")
    visits = models.PositiveIntegerField(default=0, verbose_name="Визиты")
    ctr = models.DecimalField(
        default=0,
        verbose_name="CTR",
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=10,
    )
    cta = models.PositiveIntegerField(default=0, verbose_name="Стоимость клика")
    transactions = models.PositiveIntegerField(default=0, verbose_name="Заявки")
    all_expense = models.PositiveIntegerField(default=0, verbose_name="Расход")
    income = models.PositiveIntegerField(default=0, verbose_name="Доход")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]


class YandexDirect(Ads):
    class Meta:
        verbose_name = "Yandex Direct отчет"
        verbose_name_plural = "Yandex Direct отчеты"


class GoogleAds(Ads):
    class Meta:
        verbose_name = "Google Ads отчет"
        verbose_name_plural = "Google Ads отчеты"


class VKAds(Ads):
    class Meta:
        verbose_name = "VK Ads отчет"
        verbose_name_plural = "VK Ads отчеты"


class FacebookAds(Ads):
    class Meta:
        verbose_name = "Facebook Ads отчет"
        verbose_name_plural = "Facebook Ads отчеты"


class InstagramAds(Ads):
    class Meta:
        verbose_name = "Instagram Ads отчет"
        verbose_name_plural = "Instagram Ads отчеты"


class MyTarget(Ads):
    class Meta:
        verbose_name = "MyTarget Ads отчет"
        verbose_name_plural = "MyTarget Ads отчеты"


class OtherAds(models.Model):
    title = models.CharField(max_length=100, default="-----", verbose_name="Название")
    visits = models.PositiveIntegerField(default=0, verbose_name="Визиты")
    transactions = models.PositiveIntegerField(default=0, verbose_name="Заявки")
    all_expense = models.PositiveIntegerField(default=0, verbose_name="Расход")
    convert = models.DecimalField(
        default=0,
        blank=True,
        null=True,
        verbose_name="Конверсия",
        decimal_places=3,
        max_digits=15,
    )
    income = models.PositiveIntegerField(default=0, verbose_name="Доход")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]


class TelegramAds(OtherAds):
    class Meta:
        verbose_name = "Telegram Ads отчет"
        verbose_name_plural = "Telegram Ads отчеты"


class EmailTracking(OtherAds):
    class Meta:
        verbose_name = "EmailTracking отчет"
        verbose_name_plural = "EmailTracking отчеты"


class CallTracking(OtherAds):
    class Meta:
        verbose_name = "CallTracking отчет"
        verbose_name_plural = "CallTracking отчеты"
