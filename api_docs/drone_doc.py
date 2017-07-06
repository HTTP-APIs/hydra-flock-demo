"""Generated API Documentation for Drone API using drone_doc_gen.py."""

drone_doc = {
    "@context": "http://hydrus.com/contexts/droneapi.jsonld",
    "@id": "http://hydrus.com/droneapi/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the drone side system",
    "entrypoint": "/droneapi/",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@context": "http://hydrus.com/context/Drone.jsonld",
            "@id": "http://hydrus.com/droneapi/vocab/Drone",
            "@type": "Class",
            "description": "Class for a drone",
            "supportedOperation": [
                {
                    "@id": ":change_speed",
                    "@type": "Operation",
                    "expects": "http://auto.schema.org/speed",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Speed Changed"
                        }
                    ],
                    "returns": "null",
                    "title": "ChangeSpeed"
                },
                {
                    "@id": ":change_position",
                    "@type": "Operation",
                    "expects": "http://schema.org/geo",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Position Changed"
                        }
                    ],
                    "returns": "null",
                    "title": "ChangePosition"
                },
                {
                    "@id": ":change_status",
                    "@type": "Operation",
                    "expects": "http://schema.org/status",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Status Changed"
                        }
                    ],
                    "returns": "null",
                    "title": "ChangeStatus"
                },
                {
                    "@id": ":get_speed",
                    "@type": "Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Speed returned"
                        }
                    ],
                    "returns": "http://auto.schema.org/speed",
                    "title": "GetSpeed"
                },
                {
                    "@id": ":get_position",
                    "@type": "Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Position returned"
                        }
                    ],
                    "returns": "http://schema.org/geo",
                    "title": "GetPosition"
                },
                {
                    "@id": ":get_battery_status",
                    "@type": "Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Battery status returned"
                        }
                    ],
                    "returns": "http://schema.org/fuelCapacity",
                    "title": "GetBatteryStatus"
                },
                {
                    "@id": ":get_model",
                    "@type": "Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Model returned"
                        }
                    ],
                    "returns": "http://schema.org/model",
                    "title": "GetModel"
                },
                {
                    "@id": ":get_status",
                    "@type": "Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Status returned"
                        }
                    ],
                    "returns": "http://schema.org/status",
                    "title": "GetStatus"
                },
                {
                    "@id": ":get_temperature",
                    "@type": "Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Temperature returned"
                        }
                    ],
                    "returns": "http://schema.org/Float",
                    "title": "GetTemperature"
                },
                {
                    "@id": ":recharge",
                    "@type": "Operation",
                    "expects": "http://schema.org/Action",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Successfully charged"
                        }
                    ],
                    "returns": "http://schema.org/fuelCapacity",
                    "title": "GetTemperature"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readable": "true",
                    "required": "true",
                    "title": "Speed",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "true",
                    "required": "true",
                    "title": "Position",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/fuelCapacity",
                    "readable": "true",
                    "required": "true",
                    "title": "Battery",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/device",
                    "readable": "true",
                    "required": "true",
                    "title": "Sensor",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/model",
                    "readable": "true",
                    "required": "true",
                    "title": "Model",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readable": "true",
                    "required": "true",
                    "title": "Status",
                    "writeable": "true"
                }
            ],
            "title": "Drone"
        }
    ],
    "title": "API Doc for the drone side API"
}
