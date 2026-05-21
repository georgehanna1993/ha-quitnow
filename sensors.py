import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_TOKEN

from .api import QuitNowApi
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

CONF_NICK = "nick"


async def async_setup_entry(hass, entry, async_add_entities):
    nick = entry.data[CONF_NICK]
    token = entry.data[CONF_TOKEN]

    api = QuitNowApi(nick=nick, token=token)

    sensors = [
        QuitNowSensor(
            api,
            entry,
            "Days Smoke Free",
            "days_smoke_free",
            "d",
            "mdi:calendar-check",
        ),
        QuitNowSensor(
            api,
            entry,
            "Cigarettes Avoided",
            "cigarettes_avoided",
            None,
            "mdi:smoking-off",
        ),
        QuitNowSensor(
            api,
            entry,
            "Money Saved",
            "money_saved",
            "₪",
            "mdi:cash",
        ),
        QuitNowSensor(
            api,
            entry,
            "Days Won Back",
            "days_won_back",
            "d",
            "mdi:clock-plus-outline",
        ),
    ]

    async_add_entities(sensors, True)


class QuitNowSensor(SensorEntity):
    def __init__(self, api, entry, name, stat_key, unit, icon):
        self._api = api
        self._entry = entry
        self._stat_key = stat_key

        self._attr_name = name
        self._attr_native_unit_of_measurement = unit
        self._attr_icon = icon
        self._attr_unique_id = f"{entry.entry_id}_{stat_key}"
        self._attr_native_value = None

    @property
    def device_info(self):
        nick = self._entry.data[CONF_NICK]

        return {
            "identifiers": {(DOMAIN, self._entry.entry_id)},
            "name": f"QuitNow ({nick})",
            "manufacturer": "QuitNow",
            "model": "QuitNow Account",
            "entry_type": "service",
        }

    @property
    def suggested_display_precision(self):
        if self._stat_key == "money_saved":
            return 1

        return 0

    def update(self):
        try:
            stats = self._api.get_stats()
            self._attr_native_value = stats[self._stat_key]
        except Exception as error:
            _LOGGER.error("Failed to update QuitNow sensor: %s", error)
