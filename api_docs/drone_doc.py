"""Generated API Documentation for Drone API using drone_doc_gen.py."""

drone_doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "code": "hydra:statusCode",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readonly": "hydra:readonly",
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "http://hydrus.com/droneapi/vocab#"
    },
    "@id": "http://hydrus.com/droneapi/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the drone side system",
    "entrypoint": "droneapi",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "Status",
            "@type": "hydra:Class",
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
            "@id": "Drone",
            "@type": "hydra:Class",
            "description": "Class for a drone",
            "subClassOf": "null",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "expects": "vocab:Status",
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
                    "@type": "hydra:Operation",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Status Returned"
                        }
                    ],
                    "returns": "vocab:Status",
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
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "subClassOf": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "null",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "subClassOf": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "subClassOf": "null",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "label": "The APIs main entry point.",
                    "method": "GET",
                    "returns": "vocab:EntryPoint",
                    "statusCodes": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The Status Class",
                    "hydra:title": "status",
                    "property": {
                        "@id": "vocab:EntryPoint/Status",
                        "@type": "hydra:Link",
                        "description": "Class for drone status objects",
                        "domain": "vocab:EntryPoint",
                        "label": "Status",
                        "range": "vocab:StatusCollection",
                        "supportedOperation": []
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The Drone Class",
                    "hydra:title": "drone",
                    "property": {
                        "@id": "vocab:EntryPoint/Drone",
                        "@type": "hydra:Link",
                        "description": "Class for a drone",
                        "domain": "vocab:EntryPoint",
                        "label": "Drone",
                        "range": "vocab:DroneCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:changestatus",
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "vocab:Status",
                                "label": "ChangeStatus",
                                "method": "POST",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "code": 200,
                                        "description": "Status Changed"
                                    }
                                ]
                            },
                            {
                                "@id": "_:getstatus",
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "label": "GetStatus",
                                "method": "GET",
                                "returns": "vocab:Status",
                                "statusCodes": [
                                    {
                                        "code": 200,
                                        "description": "Status Returned"
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "API Doc for the drone side API"
}
