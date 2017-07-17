"""Generated API Documentation for Server API using server_doc_gen.py."""

doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
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
        "method": "hydra:method",
        "possibleStatus": "hydra:possibleStatus",
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
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "statusCode": "hydra:statusCode",
        "statusCodes": "hydra:statusCodes",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "http://hydrus.com/serverapi/vocab#",
        "writeonly": "hydra:writeonly"
    },
    "@id": "http://hydrus.com/serverapi/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the server side system",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "http://hydrus.com/Status",
            "@type": "hydra:Class",
            "description": "Class for drone status objects",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readonly": true,
                    "required": false,
                    "title": "Speed",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readonly": true,
                    "required": false,
                    "title": "Position",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/fuelCapacity",
                    "readonly": true,
                    "required": false,
                    "title": "Battery",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readonly": true,
                    "required": false,
                    "title": "SensorStatus",
                    "writeonly": false
                }
            ],
            "title": "Status"
        },
        {
            "@id": "http://hydrus.com/Area",
            "@type": "hydra:Class",
            "description": "Class for Area of Interest of the server",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "expects": "vocab:Area",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "Area of interest changed",
                            "statusCode": 200
                        }
                    ],
                    "returns": null,
                    "title": "UpdateArea"
                },
                {
                    "@type": "hydra:Operation",
                    "expects": null,
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Area of not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Area of returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Area",
                    "title": "GetArea"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readonly": true,
                    "required": true,
                    "title": "TopLeft",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readonly": true,
                    "required": true,
                    "title": "BottomRight",
                    "writeonly": true
                }
            ],
            "title": "Area"
        },
        {
            "@id": "http://hydrus.com/Drone",
            "@type": "hydra:Class",
            "description": "Class for a drone",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "expects": "vocab:Status",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "Drone Status updated",
                            "statusCode": 200
                        }
                    ],
                    "returns": null,
                    "title": "SubmitStatus"
                },
                {
                    "@type": "hydra:Operation",
                    "expects": null,
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Drone Returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Drone",
                    "title": "GetDrone"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Status",
                    "readonly": true,
                    "required": false,
                    "title": "DroneStatus",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/name",
                    "readonly": true,
                    "required": false,
                    "title": "name",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/model",
                    "readonly": true,
                    "required": false,
                    "title": "model",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readonly": true,
                    "required": false,
                    "title": "MaxSpeed",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/device",
                    "readonly": true,
                    "required": false,
                    "title": "Sensor",
                    "writeonly": true
                }
            ],
            "title": "Drone"
        },
        {
            "@id": "http://hydrus.com/Command",
            "@type": "hydra:Class",
            "description": "Class for drone commands",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/UpdateAction",
                    "readonly": false,
                    "required": false,
                    "title": "Update",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Status",
                    "readonly": false,
                    "required": false,
                    "title": "Status",
                    "writeonly": false
                }
            ],
            "title": "Command"
        },
        {
            "@id": "http://hydrus.com/LogEntry",
            "@type": "hydra:Class",
            "description": "Class for a log entry",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "expects": null,
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Log entry not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Log entry returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "voab:LogEntry",
                    "title": "GetLog"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readonly": true,
                    "required": false,
                    "title": "DroneID",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/UpdateAction",
                    "readonly": false,
                    "required": false,
                    "title": "Update",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/ReplyAction",
                    "readonly": false,
                    "required": false,
                    "title": "Get",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/SendAction",
                    "readonly": false,
                    "required": false,
                    "title": "Send",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Status",
                    "readonly": false,
                    "required": false,
                    "title": "Status",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Data",
                    "readonly": false,
                    "required": false,
                    "title": "Data",
                    "writeonly": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Command",
                    "readonly": false,
                    "required": false,
                    "title": "Command",
                    "writeonly": true
                }
            ],
            "title": "LogEntry"
        },
        {
            "@id": "http://hydrus.com/Message",
            "@type": "hydra:Class",
            "description": "Class for messages received by the GUI interface",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Text",
                    "readonly": true,
                    "required": false,
                    "title": "MessageString",
                    "writeonly": true
                }
            ],
            "title": "Message"
        },
        {
            "@id": "http://hydrus.com/Data",
            "@type": "hydra:Class",
            "description": "Class for a data entry",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "expects": null,
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Data not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Data returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Data",
                    "title": "ReadData"
                },
                {
                    "@type": "hydra:Operation",
                    "expects": "vocab:Data",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "Data added",
                            "statusCode": 201
                        }
                    ],
                    "returns": null,
                    "title": "SubmitData"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/QuantitativeValue",
                    "readonly": true,
                    "required": false,
                    "title": "Temperature",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readonly": true,
                    "required": false,
                    "title": "DroneID",
                    "writeonly": false
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readonly": true,
                    "required": false,
                    "title": "Position",
                    "writeonly": false
                }
            ],
            "title": "Data"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": null,
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": null,
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": false,
                    "required": null,
                    "title": "members",
                    "writeonly": false
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
                    "expects": "http://hydrus.com/Drone",
                    "label": "Create new Drone entitity",
                    "method": "POST",
                    "returns": "http://hydrus.com/Drone",
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
                    "description": null,
                    "expects": null,
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
                    "readonly": false,
                    "required": null,
                    "writeonly": false
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
                    "expects": "http://hydrus.com/Data",
                    "label": "Create new Data entitity",
                    "method": "POST",
                    "returns": "http://hydrus.com/Data",
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
                    "description": null,
                    "expects": null,
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
                    "readonly": false,
                    "required": null,
                    "writeonly": false
                }
            ]
        },
        {
            "@id": "vocab:MessageCollection",
            "@type": "hydra:Class",
            "description": "A collection of message",
            "label": "MessageCollection",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:message_create",
                    "@type": "http://schema.org/AddAction",
                    "expects": "http://hydrus.com/Message",
                    "label": "Create new Message entitity",
                    "method": "POST",
                    "returns": "http://hydrus.com/Message",
                    "statusCodes": [
                        {
                            "code": 201,
                            "description": "If the Message entity was created successfully."
                        }
                    ]
                },
                {
                    "@id": "_:message_collection_retrieve",
                    "@type": "hydra:Operation",
                    "description": null,
                    "expects": null,
                    "label": "Retrieves all Message entities",
                    "method": "GET",
                    "returns": "vocab:MessageCollection",
                    "statusCodes": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The message",
                    "hydra:title": "members",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": false,
                    "required": null,
                    "writeonly": false
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
                    "expects": "http://hydrus.com/LogEntry",
                    "label": "Create new LogEntry entitity",
                    "method": "POST",
                    "returns": "http://hydrus.com/LogEntry",
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
                    "description": null,
                    "expects": null,
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
                    "readonly": false,
                    "required": null,
                    "writeonly": false
                }
            ]
        },
        {
            "@id": "vocab:StatusCollection",
            "@type": "hydra:Class",
            "description": "A collection of status",
            "label": "StatusCollection",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:status_create",
                    "@type": "http://schema.org/AddAction",
                    "expects": "http://hydrus.com/Status",
                    "label": "Create new Status entitity",
                    "method": "POST",
                    "returns": "http://hydrus.com/Status",
                    "statusCodes": [
                        {
                            "code": 201,
                            "description": "If the Status entity was created successfully."
                        }
                    ]
                },
                {
                    "@id": "_:status_collection_retrieve",
                    "@type": "hydra:Operation",
                    "description": null,
                    "expects": null,
                    "label": "Retrieves all Status entities",
                    "method": "GET",
                    "returns": "vocab:StatusCollection",
                    "statusCodes": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The status",
                    "hydra:title": "members",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": false,
                    "required": null,
                    "writeonly": false
                }
            ]
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "hydra:Operation",
                    "description": null,
                    "expects": null,
                    "label": "The APIs main entry point.",
                    "method": "GET",
                    "returns": "vocab:EntryPoint",
                    "statusCodes": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The Area Class",
                    "hydra:title": "area",
                    "property": {
                        "@id": "vocab:EntryPoint/Area",
                        "@type": "hydra:Link",
                        "description": "Class for Area of Interest of the server",
                        "domain": "vocab:EntryPoint",
                        "label": "Area",
                        "range": "vocab:Area",
                        "supportedOperation": [
                            {
                                "@id": "_:updatearea",
                                "@type": "hydra:Operation",
                                "description": null,
                                "expects": "vocab:Area",
                                "label": "UpdateArea",
                                "method": "PUT",
                                "returns": null,
                                "statusCodes": [
                                    {
                                        "description": "Area of interest changed",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "_:getarea",
                                "@type": "hydra:Operation",
                                "description": null,
                                "expects": null,
                                "label": "GetArea",
                                "method": "GET",
                                "returns": "vocab:Area",
                                "statusCodes": [
                                    {
                                        "description": "Area of not found",
                                        "statusCode": 404
                                    },
                                    {
                                        "description": "Area of returned",
                                        "statusCode": 200
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": true,
                    "required": null,
                    "writeonly": false
                },
                {
                    "hydra:description": "The DroneCollection collection",
                    "hydra:title": "dronecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DroneCollection",
                        "@type": "hydra:Link",
                        "description": "The DroneCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "DroneCollection",
                        "range": "vocab:DroneCollection"
                    },
                    "readonly": true,
                    "required": null,
                    "writeonly": false
                },
                {
                    "hydra:description": "The DataCollection collection",
                    "hydra:title": "datacollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DataCollection",
                        "@type": "hydra:Link",
                        "description": "The DataCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "DataCollection",
                        "range": "vocab:DataCollection"
                    },
                    "readonly": true,
                    "required": null,
                    "writeonly": false
                },
                {
                    "hydra:description": "The MessageCollection collection",
                    "hydra:title": "messagecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/MessageCollection",
                        "@type": "hydra:Link",
                        "description": "The MessageCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "MessageCollection",
                        "range": "vocab:MessageCollection"
                    },
                    "readonly": true,
                    "required": null,
                    "writeonly": false
                },
                {
                    "hydra:description": "The LogEntryCollection collection",
                    "hydra:title": "logentrycollection",
                    "property": {
                        "@id": "vocab:EntryPoint/LogEntryCollection",
                        "@type": "hydra:Link",
                        "description": "The LogEntryCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "LogEntryCollection",
                        "range": "vocab:LogEntryCollection"
                    },
                    "readonly": true,
                    "required": null,
                    "writeonly": false
                },
                {
                    "hydra:description": "The StatusCollection collection",
                    "hydra:title": "statuscollection",
                    "property": {
                        "@id": "vocab:EntryPoint/StatusCollection",
                        "@type": "hydra:Link",
                        "description": "The StatusCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "StatusCollection",
                        "range": "vocab:StatusCollection"
                    },
                    "readonly": true,
                    "required": null,
                    "writeonly": false
                }
            ],
            "title": "EntryPoint"
        }
    ]
}
