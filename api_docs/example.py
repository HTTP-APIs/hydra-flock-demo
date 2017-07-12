vocab = {
    "@type": "ApiDocumentation",
    "@context": {
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "property": {
            "@type": "@id",
            "@id": "hydra:property"
        },
        "drone": "http://drone.com",
        "supportedClass": "hydra:supportedClass",
        "supportedProperty": "hydra:supportedProperty",
        "supportedOperation": "hydra:supportedOperation",
        "code": "hydra:statusCode",
        "label": "rdfs:label",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "vocab": "localhost/api/vocab#",
        "domain": {
            "@type": "@id",
            "@id": "rdfs:domain"
        },
        "ApiDocumentation": "hydra:ApiDocumentation",
        "range": {
            "@type": "@id",
            "@id": "rdfs:range"
        },
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "title": "hydra:title",
        "readonly": "hydra:readonly",
        "expects": {
            "@type": "@id",
            "@id": "hydra:expects"
        },
        "owl": "http://www.w3.org/2002/07/owl#",
        "writeonly": "hydra:writeonly",
        "returns": {
            "@type": "@id",
            "@id": "hydra:returns"
        },
        "subClassOf": {
            "@type": "@id",
            "@id": "rdfs:subClassOf"
        },
        "description": "rdfs:comment",
        "method": "hydra:method",
        "statusCodes": "hydra:statusCodes"
    },
    "@id": "localhost/api/vocab",
    "supportedClass": [
        {
            "hydra:description": "null",
            "@type": "hydra:Class",
            "hydra:title": "Collection",
            "supportedProperty": [
                {
                    "hydra:description": "The members of this collection.",
                    "required": "null",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "hydra:title": "members",
                    "writeonly": "false"
                }
            ],
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": []
        },
        {
            "hydra:description": "null",
            "@type": "hydra:Class",
            "hydra:title": "Resource",
            "supportedProperty": [],
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "supportedOperation": []
        },
        {
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "subClassOf": "null",
            "supportedProperty": [
                {
                    "hydra:description": "The drone collection",
                    "required": "null",
                    "property": {
                        "@type": "hydra:Link",
                        "domain": "vocab:EntryPoint",
                        "range": "vocab:droneCollection",
                        "@id": "vocab:EntryPoint/drone",
                        "label": "drone",
                        "supportedOperation": [
                            {
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "returns": "vocab:droneCollection",
                                "@id": "_:drone_collection_retrieve",
                                "statusCodes": [],
                                "method": "GET",
                                "label": "Retrieves all drone entities"
                            }
                        ],
                        "description": "The drone collection"
                    },
                    "readonly": "true",
                    "hydra:title": "drone",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The logs collection",
                    "required": "null",
                    "property": {
                        "@type": "hydra:Link",
                        "domain": "vocab:EntryPoint",
                        "range": "vocab:logsCollection",
                        "@id": "vocab:EntryPoint/logs",
                        "label": "logs",
                        "supportedOperation": [
                            {
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "returns": "vocab:logsCollection",
                                "@id": "_:logs_collection_retrieve",
                                "statusCodes": [],
                                "method": "GET",
                                "label": "Retrieves all logs entities"
                            }
                        ],
                        "description": "The logs collection"
                    },
                    "readonly": "true",
                    "hydra:title": "logs",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The message collection",
                    "required": "null",
                    "property": {
                        "@type": "hydra:Link",
                        "domain": "vocab:EntryPoint",
                        "range": "vocab:messageCollection",
                        "@id": "vocab:EntryPoint/message",
                        "label": "message",
                        "supportedOperation": [
                            {
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "returns": "vocab:messageCollection",
                                "@id": "_:message_collection_retrieve",
                                "statusCodes": [],
                                "method": "GET",
                                "label": "Retrieves all message entities"
                            }
                        ],
                        "description": "The message collection"
                    },
                    "readonly": "true",
                    "hydra:title": "message",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The order collection",
                    "required": "null",
                    "property": {
                        "@type": "hydra:Link",
                        "domain": "vocab:EntryPoint",
                        "range": "vocab:orderCollection",
                        "@id": "vocab:EntryPoint/order",
                        "label": "order",
                        "supportedOperation": [
                            {
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "returns": "vocab:orderCollection",
                                "@id": "_:order_collection_retrieve",
                                "statusCodes": [],
                                "method": "GET",
                                "label": "Retrieves all order entities"
                            }
                        ],
                        "description": "The order collection"
                    },
                    "readonly": "true",
                    "hydra:title": "order",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The status collection",
                    "required": "null",
                    "property": {
                        "@type": "hydra:Link",
                        "domain": "vocab:EntryPoint",
                        "range": "vocab:statusCollection",
                        "@id": "vocab:EntryPoint/status",
                        "label": "status",
                        "supportedOperation": [
                            {
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "returns": "vocab:statusCollection",
                                "@id": "_:status_collection_retrieve",
                                "statusCodes": [],
                                "method": "GET",
                                "label": "Retrieves all status entities"
                            }
                        ],
                        "description": "The status collection"
                    },
                    "readonly": "true",
                    "hydra:title": "status",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The datastream collection",
                    "required": "null",
                    "property": {
                        "@type": "hydra:Link",
                        "domain": "vocab:EntryPoint",
                        "range": "vocab:datastreamCollection",
                        "@id": "vocab:EntryPoint/datastream",
                        "label": "datastream",
                        "supportedOperation": [
                            {
                                "@type": "hydra:Operation",
                                "description": "null",
                                "expects": "null",
                                "returns": "vocab:datastreamCollection",
                                "@id": "_:datastream_collection_retrieve",
                                "statusCodes": [],
                                "method": "GET",
                                "label": "Retrieves all datastream entities"
                            }
                        ],
                        "description": "The datastream collection"
                    },
                    "readonly": "true",
                    "hydra:title": "datastream",
                    "writeonly": "false"
                }
            ],
            "@id": "vocab:EntryPoint",
            "label": "EntryPoint",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "returns": "vocab:EntryPoint",
                    "@id": "_:entry_point",
                    "statusCodes": [],
                    "method": "GET",
                    "label": "The APIs main entry point."
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "Contains specifications related to each drone.",
            "title": "drone",
            "supportedProperty": [
                {
                    "hydra:description": "Identifier for drone to check if the recieved order was for the same drone.",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/identifier",
                    "title": "Identifier",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://auto.schema.org/speed",
                    "title": "Speed",
                    "writeable": "true",
                    "required": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://schema.org/geo",
                    "title": "Position",
                    "writeable": "true",
                    "required": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://schema.org/fuelCapacity",
                    "title": "Battery",
                    "writeable": "true",
                    "required": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://schema.org/device",
                    "title": "Sensor",
                    "writeable": "false",
                    "required": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://schema.org/model",
                    "title": "Model",
                    "writeable": "false",
                    "required": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "https://schema.org/status",
                    "title": "Status",
                    "writeable": "true",
                    "required": "true"
                }
            ],
            "@id": "http://hydrus.com/drone",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "@id": "_:drone_create",
                    "description": "null",
                    "label": "Add a new drone to the Central Server",
                    "expects": "http://hydrus.com/drone",
                    "method": "POST",
                    "returns": "http://hydrus.com/drone",
                    "statusCodes": [
                        {
                            "description": "New drone successfully created.",
                            "code": 201
                        }
                    ]
                },
                {
                    "@type": "hydra:Operation",
                    "@id": "_:drone_retrieve",
                    "description": "null",
                    "label": "Retrieves all drones from the central server.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "http://hydrus.com/drone",
                    "statusCodes": [
                        {
                            "description": "If no orders were found.",
                            "code": 404
                        }
                    ]
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "Handle logs from the central server.",
            "title": "logs",
            "supportedProperty": [],
            "@id": "http://hydrus.com/logs",
            "supportedOperation": [
                {
                    "@type": "hydra:Operation",
                    "@id": "_:logs_retrieve",
                    "description": "null",
                    "label": "Retrieves all logs from the central server.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "http://hydrus.com/logs",
                    "statusCodes": [
                        {
                            "description": "If no logs were found.",
                            "code": 404
                        }
                    ]
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "Commands in NLP format issued by the user.",
            "title": "message",
            "supportedProperty": [
                {
                    "hydra:description": "Message in NLP format submitted from GUI client.",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/message",
                    "title": "message",
                    "readonly": "false",
                    "writeonly": "false"
                }
            ],
            "@id": "http://hydrus.com/message",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "@id": "_:message_create",
                    "description": "null",
                    "label": "Recieve command in NLP format from the GUI client.",
                    "expects": "http://hydrus.com/message",
                    "method": "POST",
                    "returns": "http://hydrus.com/message",
                    "statusCodes": [
                        {
                            "description": "message successfully submitted.",
                            "code": 200
                        }
                    ]
                },
                {
                    "@type": "hydra:Operation",
                    "@id": "_:message_retrieve",
                    "description": "null",
                    "label": "Retrieves all messages submitted to the central server.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "http://hydrus.com/message",
                    "statusCodes": [
                        {
                            "description": "If no messages were found.",
                            "code": 404
                        }
                    ]
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "Handle orders from the central server.",
            "title": "order",
            "supportedProperty": [
                {
                    "hydra:description": "Coordinates of the new destination",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/geo",
                    "title": "Destination",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "Speed of drone in Km/h",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://auto.schema.org/speed",
                    "title": "Speed",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "Identifier for drone to check if the recieved order was for the same drone.",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/identifier",
                    "title": "Identifier",
                    "readonly": "false",
                    "writeonly": "false"
                }
            ],
            "@id": "http://schema.org/order",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "@id": "_:order_create",
                    "description": "null",
                    "label": "Recieves orders from the Central Server",
                    "expects": "http://schema.org/order",
                    "method": "POST",
                    "returns": "http://schema.org/order",
                    "statusCodes": [
                        {
                            "description": "order successfully recieved.",
                            "code": 200
                        }
                    ]
                },
                {
                    "@type": "hydra:Operation",
                    "@id": "_:order_retrieve",
                    "description": "null",
                    "label": "Retrieves all orders from the central server.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "http://schema.org/order",
                    "statusCodes": [
                        {
                            "description": "If no orders were found.",
                            "code": 404
                        }
                    ]
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "Handle status requests from different drones.",
            "title": "status",
            "supportedProperty": [
                {
                    "hydra:description": "Identifier for server to check if the drone is associated with the server.",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/identifier",
                    "title": "Identifier",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "Coordinates of the new destination",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/geo",
                    "title": "Destination",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "Speed of Drone in Km/h",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://auto.schema.org/speed",
                    "title": "Speed",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://schema.org/geo",
                    "title": "Position",
                    "writeable": "true",
                    "required": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://schema.org/fuelCapacity",
                    "title": "Battery",
                    "writeable": "true",
                    "required": "true"
                },
                {
                    "hydra:description": "Current status of the drone can be [ Charging| Moving| Reached Destination| Analysing ]",
                    "@type": "SupportedProperty",
                    "readable": "true",
                    "property": "http://schema.org/OrderStatus",
                    "title": "Progress",
                    "writeable": "true",
                    "required": "true"
                }
            ],
            "@id": "http://hydrus.com/status",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "@id": "_:status_create",
                    "description": "null",
                    "label": "Recieves status updates from different drones.",
                    "expects": "http://hydrus.com/status",
                    "method": "POST",
                    "returns": "http://hydrus.com/status",
                    "statusCodes": [
                        {
                            "description": "Status successfully submitted.",
                            "code": 200
                        }
                    ]
                },
                {
                    "@type": "hydra:Operation",
                    "@id": "_:status_retrieve",
                    "description": "null",
                    "label": "Retrieves all status objects submitted by differnt drones.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "http://hydrus.com/status",
                    "statusCodes": [
                        {
                            "description": "If no status objects were found.",
                            "code": 404
                        }
                    ]
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "Handle sensor datastreams submitted by different drones.",
            "title": "datastream",
            "supportedProperty": [
                {
                    "hydra:description": "Coordinates of the current location",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/geo",
                    "title": "Position",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "Temperature of area can be [ Normal | Abnormal | Critical]",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "schema.org/QuantitativeValue",
                    "title": "Temperature",
                    "readonly": "false",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "Identifier for drone to check if the recieved datastream was for the same drone.",
                    "@type": "SupportedProperty",
                    "required": "true",
                    "property": "http://schema.org/identifier",
                    "title": "Drone Identifier",
                    "readonly": "false",
                    "writeonly": "false"
                }
            ],
            "@id": "http://hydrus.com/datastream",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "@id": "_:datastream_create",
                    "description": "null",
                    "label": "Recieves datastreams from differnet drones.",
                    "expects": "http://hydrus.com/datastream",
                    "method": "POST",
                    "returns": "http://hydrus.com/datastream",
                    "statusCodes": [
                        {
                            "description": "Datastream successfully recieved.",
                            "code": 200
                        }
                    ]
                },
                {
                    "@type": "hydra:Operation",
                    "@id": "_:datastream_retrieve",
                    "description": "null",
                    "label": "Retrieves all datastream objects from the central server.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "http://hydrus.com/datastream",
                    "statusCodes": [
                        {
                            "description": "No datastream objects were found.",
                            "code": 404
                        }
                    ]
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "A collection of drone",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedProperty": [
                {
                    "hydra:description": "The drone",
                    "required": "null",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "hydra:title": "members",
                    "writeonly": "false"
                }
            ],
            "@id": "vocab:droneCollection",
            "label": "droneCollection",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "http://hydrus.com/drone",
                    "@id": "_:drone_create",
                    "statusCodes": [
                        {
                            "description": "If the drone entity was created successfully.",
                            "code": 201
                        }
                    ],
                    "method": "POST",
                    "returns": "http://hydrus.com/drone"
                },
                {
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "returns": "vocab:droneCollection",
                    "@id": "_:drone_collection_retrieve",
                    "statusCodes": [],
                    "method": "GET",
                    "label": "Retrieves all drone entities"
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "A collection of logs",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedProperty": [
                {
                    "hydra:description": "The logs",
                    "required": "null",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "hydra:title": "members",
                    "writeonly": "false"
                }
            ],
            "@id": "vocab:logsCollection",
            "label": "logsCollection",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "null",
                    "@id": "_:logs_create",
                    "statusCodes": [
                        {
                            "description": "If the logs entity was created successfully.",
                            "code": 201
                        }
                    ],
                    "method": "POST",
                    "returns": "http://hydrus.com/logs"
                },
                {
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "returns": "vocab:logsCollection",
                    "@id": "_:logs_collection_retrieve",
                    "statusCodes": [],
                    "method": "GET",
                    "label": "Retrieves all logs entities"
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "A collection of message",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedProperty": [
                {
                    "hydra:description": "The message",
                    "required": "null",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "hydra:title": "members",
                    "writeonly": "false"
                }
            ],
            "@id": "vocab:messageCollection",
            "label": "messageCollection",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "http://hydrus.com/message",
                    "@id": "_:message_create",
                    "statusCodes": [
                        {
                            "description": "If the message entity was created successfully.",
                            "code": 201
                        }
                    ],
                    "method": "POST",
                    "returns": "http://hydrus.com/message"
                },
                {
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "returns": "vocab:messageCollection",
                    "@id": "_:message_collection_retrieve",
                    "statusCodes": [],
                    "method": "GET",
                    "label": "Retrieves all message entities"
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "A collection of order",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedProperty": [
                {
                    "hydra:description": "The order",
                    "required": "null",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "hydra:title": "members",
                    "writeonly": "false"
                }
            ],
            "@id": "vocab:orderCollection",
            "label": "orderCollection",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "http://schema.org/order",
                    "@id": "_:order_create",
                    "statusCodes": [
                        {
                            "description": "If the order entity was created successfully.",
                            "code": 201
                        }
                    ],
                    "method": "POST",
                    "returns": "http://schema.org/order"
                },
                {
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "returns": "vocab:orderCollection",
                    "@id": "_:order_collection_retrieve",
                    "statusCodes": [],
                    "method": "GET",
                    "label": "Retrieves all order entities"
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "A collection of status",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedProperty": [
                {
                    "hydra:description": "The status",
                    "required": "null",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "hydra:title": "members",
                    "writeonly": "false"
                }
            ],
            "@id": "vocab:statusCollection",
            "label": "statusCollection",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "http://hydrus.com/status",
                    "@id": "_:status_create",
                    "statusCodes": [
                        {
                            "description": "If the status entity was created successfully.",
                            "code": 201
                        }
                    ],
                    "method": "POST",
                    "returns": "http://hydrus.com/status"
                },
                {
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "returns": "vocab:statusCollection",
                    "@id": "_:status_collection_retrieve",
                    "statusCodes": [],
                    "method": "GET",
                    "label": "Retrieves all status entities"
                }
            ]
        },
        {
            "@type": "hydra:Class",
            "description": "A collection of datastream",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedProperty": [
                {
                    "hydra:description": "The datastream",
                    "required": "null",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "hydra:title": "members",
                    "writeonly": "false"
                }
            ],
            "@id": "vocab:datastreamCollection",
            "label": "datastreamCollection",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/AddAction",
                    "description": "null",
                    "expects": "http://hydrus.com/datastream",
                    "@id": "_:datastream_create",
                    "statusCodes": [
                        {
                            "description": "If the datastream entity was created successfully.",
                            "code": 201
                        }
                    ],
                    "method": "POST",
                    "returns": "http://hydrus.com/datastream"
                },
                {
                    "@type": "hydra:Operation",
                    "description": "null",
                    "expects": "null",
                    "returns": "vocab:datastreamCollection",
                    "@id": "_:datastream_collection_retrieve",
                    "statusCodes": [],
                    "method": "GET",
                    "label": "Retrieves all datastream entities"
                }
            ]
        }
    ]
}
