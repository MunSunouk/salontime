from django.apps import AppConfig
import shuup.apps


class ShopsConfig(shuup.apps.AppConfig):
    name = 'shops'
    label = "shops"
    provides = {
        "api_populator": [
            "shuup_rest_api.api.populate_api"
        ]
    }
