from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from generators import gen_seo_report, gen_ads_report, gen_other_report

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


@app.get("/seo/")
async def get_seo_report():
    seo_report = gen_seo_report()
    return jsonable_encoder(seo_report)


@app.get("/yandex_ads/")
async def get_yandex_ads_report():
    ads_report = gen_ads_report()
    return jsonable_encoder(ads_report)


@app.get("/google_ads/")
async def get_google_ads_report():
    ads_report = gen_ads_report()
    return jsonable_encoder(ads_report)


@app.get("/vk_ads/")
async def get_vk_ads_report():
    ads_report = gen_ads_report()
    return jsonable_encoder(ads_report)


@app.get("/facebook_ads/")
async def get_facebook_ads_report():
    ads_report = gen_ads_report()
    return jsonable_encoder(ads_report)


@app.get("/telegram_ads/")
async def get_telegram_ads_report():
    ads_report = gen_other_report()
    return jsonable_encoder(ads_report)


@app.get("/email_ads/")
async def get_email_ads_report():
    ads_report = gen_other_report()
    return jsonable_encoder(ads_report)


@app.get("/call_ads/")
async def get_call_ads_report():
    ads_report = gen_other_report()
    return jsonable_encoder(ads_report)
