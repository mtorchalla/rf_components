"""
This component provides support for a RF switch.

"""

import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.config_validation import (PLATFORM_SCHEMA)

from homeassistant.const import (
    CONF_UNIQUE_ID,
)

_LOGGER = logging.getLogger(__name__)

CONF_NAME = "name"
CONF_INITIAL_VALUE = "initial_value"
# CONF_UNIQUE_ID = "unique_id"
CONF_ON_VAL = "on_val"
CONF_OFF_VAL = "off_val"
CONF_PULSE_LEN = "pulse_len"

DEFAULT_INITIAL_VALUE = "off"
DEFAULT_ON_VAL = "0"
DEFAULT_ON_VAL = "0"
DEFAULT_PULSE_LEN = "230"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Optional(CONF_INITIAL_VALUE, default=DEFAULT_INITIAL_VALUE): cv.string,
    vol.Required(CONF_ON_VAL): cv.string,
    vol.Required(CONF_OFF_VAL): cv.string,
    vol.Required(CONF_PULSE_LEN): cv.string,
    vol.Optional(CONF_UNIQUE_ID): cv.string,
})


async def async_setup_platform(_hass, config, async_add_entities, _discovery_info=None):
    switches = [RfSwitch(config)]
    async_add_entities(switches, True)


class RfSwitch(SwitchEntity):
    """Representation of a RF switch."""

    def __init__(self, config):
        """Initialize the RF switch device."""
        self._name = config.get(CONF_NAME)
        self._state = config.get(CONF_INITIAL_VALUE)
        self._on_val = config.get(CONF_ON_VAL)
        self._off_val = config.get(CONF_OFF_VAL)
        self._pulse_len = config.get(CONF_PULSE_LEN)
        unique_id = config.get(CONF_UNIQUE_ID)
        if not unique_id:
            self._unique_id = self._name.lower().replace(' ', '_')
        else:
            self._unique_id = unique_id
        _LOGGER.info('RfSwitch: {} created'.format(self._name))

    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._unique_id

    @property
    def state(self):
        """Return the state of the switch."""
        return self._state

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self.state == "on"

    @property
    def is_off(self):
        """Return true if switch is on."""
        return not self.is_on

    def turn_on(self, **kwargs):
        self._state = 'on'

    def turn_off(self, **kwargs):
        self._state = 'off'

    @property
    def device_state_attributes(self):
        """Return the device state attributes."""
        attrs = {
            'friendly_name': self._name,
            'unique_id': self._unique_id,
            'on_val': self._on_val,
            'off_val': self._off_val,
            'pulse_len': self._pulse_len
        }
        return attrs
