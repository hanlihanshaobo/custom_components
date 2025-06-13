from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import STATE_UNKNOWN
from .const import DOMAIN, SENSORS

async def async_setup_entry(hass, config_entry, async_add_entities):
    # 可扩展：适配配置流程
    pass

async def async_setup(hass, config, async_add_entities, discovery_info=None):
    entities = [SGCCSensor(sensor) for sensor in SENSORS]
    async_add_entities(entities)

class SGCCSensor(SensorEntity):
    def __init__(self, sensor_def):
        self._attr_name = sensor_def["name"]
        self._attr_unique_id = sensor_def["key"]
        self._key = sensor_def["key"]
        self._attr_native_unit_of_measurement = sensor_def["unit"]
        self._attr_device_class = sensor_def["device_class"]
        self._attr_state_class = sensor_def["state_class"]
        self._attr_native_value = STATE_UNKNOWN

    @property
    def native_value(self):
        return self._attr_native_value

    def update_value(self, value):
        self._attr_native_value = value
        self.async_write_ha_state()
