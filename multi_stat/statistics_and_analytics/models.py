from django.db import models


class SEOReport(models.Model):
    title = models.CharField(max_length=100, default="SEO", verbose_name="Название")
    visits = models.PositiveIntegerField(default=0, verbose_name="Визиты")
    all_expense = models.PositiveIntegerField(default=0, verbose_name="Расход")
    sum_transactions = models.PositiveIntegerField(default=0, verbose_name="Заявки")
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
        verbose_name="Средняя позиция",
        decimal_places=5,
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
