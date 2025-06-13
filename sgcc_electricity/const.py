DOMAIN = "sgcc_electricity"

SENSORS = [
    {
        "name": "最近一天用电量",
        "key": "last_electricity_usage_xxxx",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "measurement",
    },
    {
        "name": "预付费电费余额",
        "key": "electricity_charge_balance_xxxx",
        "unit": "CNY",
        "device_class": "monetary",
        "state_class": "total",
    },
    {
        "name": "今年总用电量",
        "key": "yearly_electricity_usage_xxxx",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
    },
    {
        "name": "今年总用电费",
        "key": "yearly_electricity_charge_xxxx",
        "unit": "CNY",
        "device_class": "monetary",
        "state_class": "total_increasing",
    },
    {
        "name": "最近一个月用电量",
        "key": "month_electricity_usage_xxxx",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "measurement",
    },
    {
        "name": "上月总用电费",
        "key": "month_electricity_charge_xxxx",
        "unit": "CNY",
        "device_class": "monetary",
        "state_class": "measurement",
    },
]
