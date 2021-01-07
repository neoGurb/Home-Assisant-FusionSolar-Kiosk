"""
Custom integration to integrate FusionSolar Kiosk with Home Assistant.
"""
import logging

from homeassistant import core
from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    ENERGY_KILO_WATT_HOUR,
    POWER_KILO_WATT,
)
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import (
    ATTR_SUCCESS, 
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the FusionSolar Kiosk component."""
    _LOGGER.debug("Set up the  Solar Kiosk component")

    return True


class FusionSolarKioskEnergyEntity(CoordinatorEntity, Entity):
    """Base class for all FusionSolarKioskEnergy entities."""
    def __init__(
        self,
        coordinator,
        kioskId,
        kioskName,
        idSuffix,
        nameSuffix,
        attribute,
    ):
        """Initialize the entity"""
        super().__init__(coordinator)
        self._kioskId = kioskId
        self._kioskName = kioskName
        self._idSuffix = idSuffix
        self._nameSuffix = nameSuffix
        self._attribute = attribute

    @property
    def device_class(self):
        return DEVICE_CLASS_ENERGY

    @property
    def name(self):
        return f'{self._kioskName} ({self._kioskId}) - {self._nameSuffix}'

    @property
    def state(self):
        return self.coordinator.data[self._kioskId][self._attribute] if self.coordinator.data[self._kioskId][ATTR_SUCCESS] else None

    @property
    def unique_id(self) -> str:
        return f'{DOMAIN}-{self._kioskId}-{self._idSuffix}'

    @property
    def unit_of_measurement(self):
        return ENERGY_KILO_WATT_HOUR


class FusionSolarKioskPowerEntity(CoordinatorEntity, Entity):
    """Base class for all FusionSolarKioskEnergy entities."""
    def __init__(
        self,
        coordinator,
        kioskId,
        kioskName,
        idSuffix,
        nameSuffix,
        attribute,
    ):
        """Initialize the entity"""
        super().__init__(coordinator)
        self._kioskId = kioskId
        self._kioskName = kioskName
        self._idSuffix = idSuffix
        self._nameSuffix = nameSuffix
        self._attribute = attribute

    @property
    def device_class(self):
        return DEVICE_CLASS_POWER

    @property
    def name(self):
        return f'{self._kioskName} ({self._kioskId}) - {self._nameSuffix}'

    @property
    def state(self):
        return self.coordinator.data[self._kioskId][self._attribute] if self.coordinator.data[self._kioskId][ATTR_SUCCESS] else None

    @property
    def unique_id(self) -> str:
        return f'{DOMAIN}-{self._kioskId}-{self._idSuffix}'

    @property
    def unit_of_measurement(self):
        return POWER_KILO_WATT