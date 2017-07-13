"""Generated API Documentation for Server API using server_doc_gen.py."""

server_doc = {
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
        "vocab": "http://hydrus.com/serverapi/vocab#"
    },
    "@id": "http://hydrus.com/serverapi/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the server side system",
    "entrypoint": "serverapi",
    "possibleStatus": [],
    "supportedClass": [
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
            "@id": "Data",
            "@type": "hydra:Class",
            "description": "Class for a data entry",
            "subClassOf": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/QuantitativeValue",
                    "readable": "true",
                    "required": "false",
                    "title": "Temperature",
                    "writeable": "true"
                }
            ],
            "title": "Data"
        },
        {
            "@id": "LogEntry",
            "@type": "hydra:Class",
            "description": "Class for a log entry",
            "subClassOf": "null",
            "supportedOperation": [],
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
            "@id": "Area",
            "@type": "hydra:Class",
            "description": "Class for Area of Interest of the server",
            "subClassOf": "null",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "expects": "http://hydrus.com/Area",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "code": 200,
                            "description": "Area of interest changed"
                        }
                    ],
                    "returns": ""null"",
                    "title": "UpdateArea"
                },
                {
                    "@type": "hydra:Operation",
                    "expects": ""null"",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "code": 404,
                            "description": "Area of not found"
                        }
                    ],
                    "returns": "http://hydrus.com/Area",
                    "title": "GetArea"
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
            "@id": "vocab:DroneCollection",
            "@type": "hydra:Class",
            "description": "A collection of drone",
            "label": "DroneCollection",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:drone_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "Drone",
                    "method": "POST",
                    "returns": "Drone",
                    "statusCodes": [
                        {
                            "code": 201,
                            "description": "If the Drone entity was created successfully."
                        }
                    ]
                },
                {
                    "@id": "_:drone_collection_retrieve",
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "label": "Retrieves all Drone entities",
                    "method": "GET",
                    "returns": "vocab:DroneCollection",
                    "statusCodes": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The drone",
                    "hydra:title": "members",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "null",
                    "writeonly": "false"
                }
            ]
        },
        {
            "@id": "vocab:DataCollection",
            "@type": "hydra:Class",
            "description": "A collection of data",
            "label": "DataCollection",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:data_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "Data",
                    "method": "POST",
                    "returns": "Data",
                    "statusCodes": [
                        {
                            "code": 201,
                            "description": "If the Data entity was created successfully."
                        }
                    ]
                },
                {
                    "@id": "_:data_collection_retrieve",
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "label": "Retrieves all Data entities",
                    "method": "GET",
                    "returns": "vocab:DataCollection",
                    "statusCodes": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The data",
                    "hydra:title": "members",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "null",
                    "writeonly": "false"
                }
            ]
        },
        {
            "@id": "vocab:LogEntryCollection",
            "@type": "hydra:Class",
            "description": "A collection of logentry",
            "label": "LogEntryCollection",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:logentry_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "LogEntry",
                    "method": "POST",
                    "returns": "LogEntry",
                    "statusCodes": [
                        {
                            "code": 201,
                            "description": "If the LogEntry entity was created successfully."
                        }
                    ]
                },
                {
                    "@id": "_:logentry_collection_retrieve",
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "label": "Retrieves all LogEntry entities",
                    "method": "GET",
                    "returns": "vocab:LogEntryCollection",
                    "statusCodes": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The logentry",
                    "hydra:title": "members",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "null",
                    "writeonly": "false"
                }
            ]
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
                },
                {
                    "hydra:description": "The Area Class",
                    "hydra:title": "area",
                    "property": {
                        "@id": "vocab:EntryPoint/Area",
                        "@type": "hydra:Link",
                        "description": "Class for Area of Interest of the server",
                        "domain": "vocab:EntryPoint",
                        "label": "Area",
                        "range": "vocab:AreaCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:updatearea",
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "http://hydrus.com/Area",
                                "label": "UpdateArea",
                                "method": "PUT",
                                "returns": ""null"",
                                "statusCodes": [
                                    {
                                        "code": 200,
                                        "description": "Area of interest changed"
                                    }
                                ]
                            },
                            {
                                "@id": "_:getarea",
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": ""null"",
                                "label": "GetArea",
                                "method": "GET",
                                "returns": "http://hydrus.com/Area",
                                "statusCodes": [
                                    {
                                        "code": 404,
                                        "description": "Area of not found"
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The Drone collection",
                    "hydra:title": "drone",
                    "property": {
                        "@id": "vocab:EntryPoint/Drone",
                        "@type": "hydra:Link",
                        "description": "The Drone collection",
                        "domain": "vocab:EntryPoint",
                        "label": "Drone",
                        "range": "vocab:DroneCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:drone_collection_retrieve",
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "label": "Retrieves all Drone entities",
                                "method": "GET",
                                "returns": "vocab:DroneCollection",
                                "statusCodes": []
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The Data collection",
                    "hydra:title": "data",
                    "property": {
                        "@id": "vocab:EntryPoint/Data",
                        "@type": "hydra:Link",
                        "description": "The Data collection",
                        "domain": "vocab:EntryPoint",
                        "label": "Data",
                        "range": "vocab:DataCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:data_collection_retrieve",
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "label": "Retrieves all Data entities",
                                "method": "GET",
                                "returns": "vocab:DataCollection",
                                "statusCodes": []
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The LogEntry collection",
                    "hydra:title": "logentry",
                    "property": {
                        "@id": "vocab:EntryPoint/LogEntry",
                        "@type": "hydra:Link",
                        "description": "The LogEntry collection",
                        "domain": "vocab:EntryPoint",
                        "label": "LogEntry",
                        "range": "vocab:LogEntryCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:logentry_collection_retrieve",
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "label": "Retrieves all LogEntry entities",
                                "method": "GET",
                                "returns": "vocab:LogEntryCollection",
                                "statusCodes": []
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
    "title": "API Doc for the server side API"
}
