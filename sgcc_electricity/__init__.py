from homeassistant.components.http import HomeAssistantView
from homeassistant.const import HTTP_OK

async def async_setup(hass, config):
    hass.http.register_view(SgccUpdateView)
    return True

class SgccUpdateView(HomeAssistantView):
    url = "/api/sgcc_electricity/update"
    name = "api:sgcc_electricity:update"
    requires_auth = True

    async def post(self, request):
        data = await request.json()
        key = data.get("key")
        value = data.get("value")

        # 查找对应实体
        for entity in hass.data["sgcc_electricity"]["entities"]:
            if entity.unique_id == key:
                entity.update_value(value)
                return self.json({"status": "ok"}, status_code=HTTP_OK)

        return self.json({"error": "entity not found"}, status_code=404)
