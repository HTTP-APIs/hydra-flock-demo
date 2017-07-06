"""Generated API Documentation for Server API using server_doc_gen.py."""

server_doc = {
    "@context": "http://hydrus.com/contexts/serverapi.jsonld",
    "@id": "http://hydrus.com/serverapi/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the server side system",
    "entrypoint": "/serverapi/",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@context": "http://hydrus.com/context/Drone.jsonld",
            "@id": "http://hydrus.com/serverapi/vocab/Drone",
            "@type": "Class",
            "description": "Class for a drone",
            "supportedOperation": [
                {
                    "@id": "/serverapi/change_speed",
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
                    "@id": "/serverapi/change_position",
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
                    "@id": "/serverapi/change_status",
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
                    "@id": "/serverapi/get_speed",
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
                    "@id": "/serverapi/get_position",
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
                    "@id": "/serverapi/get_battery_status",
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
                    "@id": "/serverapi/get_model",
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
                    "@id": "/serverapi/get_status",
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
                    "@id": "/serverapi/get_temperature",
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
                    "@id": "/serverapi/recharge",
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
        },
        {
            "@context": "http://hydrus.com/context/LogEntry.jsonld",
            "@id": "http://hydrus.com/serverapi/vocab/LogEntry",
            "@type": "Class",
            "description": "Class for a log entry",
            "supportedOperation": [
                {
                    "@id": "/serverapi/log_entry",
                    "@type": "Operation",
                    "expects": "http://hydrus.com/LogEntry",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Log entered"
                        }
                    ],
                    "returns": "null",
                    "title": "CreateEntry"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://hydrus.com/serverapi/vocab/Drone",
                    "readable": "true",
                    "required": "true",
                    "title": "Drone",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/UpdateAction",
                    "readable": "true",
                    "required": "false",
                    "title": "Update",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/ReplyAction",
                    "readable": "true",
                    "required": "false",
                    "title": "Get",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readable": "true",
                    "required": "false",
                    "title": "Speed",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "true",
                    "required": "false",
                    "title": "Position",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/fuelCapacity",
                    "readable": "true",
                    "required": "false",
                    "title": "Battery",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/device",
                    "readable": "true",
                    "required": "false",
                    "title": "Sensor",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/model",
                    "readable": "true",
                    "required": "false",
                    "title": "Model",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readable": "true",
                    "required": "false",
                    "title": "Status",
                    "writeable": "true"
                }
            ],
            "title": "LogEntry"
        },
        {
            "@context": "http://hydrus.com/context/Area.jsonld",
            "@id": "http://hydrus.com/serverapi/vocab/Area",
            "@type": "Class",
            "description": "Class for Area of Interest of the server",
            "supportedOperation": [
                {
                    "@id": "/serverapi/update_area",
                    "@type": "Operation",
                    "expects": "http://hydrus.com/Area",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Area of interest changed"
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateArea"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "true",
                    "required": "true",
                    "title": "TopLeft",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "true",
                    "required": "true",
                    "title": "BottomRight",
                    "writeable": "true"
                }
            ],
            "title": "Area"
        }
    ],
    "title": "API Doc for the server side API"
}
