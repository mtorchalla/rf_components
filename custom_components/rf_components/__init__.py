"""
This component provides support for virtual components.

"""

import logging

from homeassistant.exceptions import HomeAssistantError

__version__ = '0.4'

_LOGGER = logging.getLogger(__name__)

COMPONENT_DOMAIN = 'rf_components'
COMPONENT_SERVICES = 'rf_components-services'


def add_new_switch_to_yaml(call):
    """Handle the service call."""
    name = call.data.get("name", "test")
    _LOGGER.debug("RF_COMPONENTS: Got from service call: {}".format(name))


def setup(hass, _config):
    """Set up a rf component."""

    hass.data[COMPONENT_SERVICES] = {}
    _LOGGER.debug('setup')
    hass.services.register(COMPONENT_DOMAIN, "add_new_switch_to_yaml", add_new_switch_to_yaml)
    return True


def get_entity_from_domain(hass, domain, entity_id):
    component = hass.data.get(domain)
    if component is None:
        raise HomeAssistantError("{} component not set up".format(domain))

    entity = component.get_entity(entity_id)
    if entity is None:
        raise HomeAssistantError("{} not found".format(entity_id))

    return entity
