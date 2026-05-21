import voluptuous as vol

from homeassistant import config_entries

from .api import QuitNowApi
from .const import DOMAIN

CONF_NICK = "nick"
CONF_TOKEN = "token"


class QuitNowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            nick = user_input[CONF_NICK]
            token = user_input[CONF_TOKEN]

            try:
                api = QuitNowApi(nick=nick, token=token)

                await self.hass.async_add_executor_job(api.get_stats)

                await self.async_set_unique_id(nick)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=f"QuitNow ({nick})",
                    data=user_input,
                )

            except Exception:
                errors["base"] = "cannot_connect"

        schema = vol.Schema(
            {
                vol.Required(CONF_NICK): str,
                vol.Required(CONF_TOKEN): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
