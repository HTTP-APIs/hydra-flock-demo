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
            "@context": "http://hydrus.com/context/Status.jsonld",
            "@id": "http://hydrus.com/droneapi/vocab#Status",
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
            "@id": "http://hydrus.com/droneapi/vocab#Drone",
            "@type": "Class",
            "description": "Class for a drone",
            "subClassOf": "null",
            "supportedOperation": [
                {
                    "@id": "/droneapi/issue_order",
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
                    "@id": "/droneapi/get_status",
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
        }
    ],
    "title": "API Doc for the drone side API"
}
