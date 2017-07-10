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
            "@context": "http://hydrus.com/context/Status.jsonld",
            "@id": "http://hydrus.com/serverapi/vocab#Status",
            "@type": "Class",
            "description": "Class for drone status objects",
            "subClassOf": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readable": "true",
                    "required": "false",
                    "title": "Speed",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "true",
                    "required": "false",
                    "title": "Position",
                    "writeable": "false"
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
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/model",
                    "readable": "true",
                    "required": "false",
                    "title": "Model",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readable": "true",
                    "required": "false",
                    "title": "SensorStatus",
                    "writeable": "false"
                }
            ],
            "title": "Status"
        },
        {
            "@context": "http://hydrus.com/context/Drone.jsonld",
            "@id": "http://hydrus.com/serverapi/vocab#Drone",
            "@type": "Class",
            "description": "Class for a drone",
            "subClassOf": "null",
            "supportedOperation": [
                {
                    "@id": "/serverapi/issue_order",
                    "@type": "Operation",
                    "expects": "vocab: Status",
                    "method": "POST",
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
                    "@id": "/serverapi/get_status",
                    "@type": "Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Status Returned"
                        }
                    ],
                    "returns": "vocab: Status",
                    "title": "GetStatus"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Status",
                    "readable": "true",
                    "required": "false",
                    "title": "DroneStatus",
                    "writeable": "false"
                }
            ],
            "title": "Drone"
        },
        {
            "@context": "http://hydrus.com/context/LogEntry.jsonld",
            "@id": "http://hydrus.com/serverapi/vocab#LogEntry",
            "@type": "Class",
            "description": "Class for a log entry",
            "subClassOf": "null",
            "supportedOperation": [
                {
                    "@id": "/serverapi/get_latest_log",
                    "@type": "Operation",
                    "expects": "vocab:LogEntry",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Log returned"
                        }
                    ],
                    "returns": "null",
                    "title": "GetLogEntries"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Drone",
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
                    "property": "vocab:Status",
                    "readable": "true",
                    "required": "true",
                    "title": "Status",
                    "writeable": "true"
                }
            ],
            "title": "LogEntry"
        },
        {
            "@context": "http://hydrus.com/context/Area.jsonld",
            "@id": "http://hydrus.com/serverapi/vocab#Area",
            "@type": "Class",
            "description": "Class for Area of Interest of the server",
            "subClassOf": "null",
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
