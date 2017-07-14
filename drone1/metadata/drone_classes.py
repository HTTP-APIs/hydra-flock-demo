classes_ = [
    {
        "@id": "http://schema.org/Order",
        "@type": "hydra:Class",
        "title": "order",
        "description": "Handle orders from the central server.",
        "supportedOperation": [
            {
                 "statusCodes": [
                     {
                         "code": 200,
                         "description": "Order successfully recieved."
                     }
                 ],
                "@type": "http://schema.org/UpdateAction",
                "returns": "http://schema.org/Order",
                "label": "Create new order.",
                "method": "POST",
                "@id": "_:Order_create",
                "description": None,
                "expects": "http://schema.org/Order"
            },
            {
                "statusCodes": [
                    {
                        "code": 404,
                        "description": "If no orders were found."
                    }
                ],
                "@type": "hydra:Operation",
                "returns": "http://schema.org/Order",
                "label": "Retrieves a order.",
                "method": "GET",
                "@id": "_:Order_retrieve",
                "description": None,
                "expects": None
            }
        ],
        "supportedProperty": [

            {"@type": "SupportedProperty",
             "property": "http://schema.org/geo",
             "title": "Destination",
             "hydra:description": "Coordinates of the new destination",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
            {"@type": "SupportedProperty",
             "property": "http://auto.schema.org/speed",
             "title": "Speed",
             "hydra:description": "Speed of Drone in Km/h",
             "required": True,
             "readonly": False,
             "writeonly": False
             },

            {"@type": "SupportedProperty",
             "property": "http://schema.org/identifier",
             "title": "Identifier",
             "hydra:description": "Id with which the drone is stored at the central server ( Initially None).",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
        ]
    },
    # 1. Drone Class
    {
        "@id": "http://hydrus.com/info",
        "@type": "hydra:Class",
        "title": "info",
        "description": "Contains specifications related to the drone itself.",
        "supportedOperation": [
            {
                "statusCodes": [],
                "@type": "hydra:Operation",
                "returns": "http://hydrus.com/info",
                "label": "Retrieves all drone details.",
                "method": "GET",
                "@id": "_:info_retrieve",
                "description": None,
                "expects": None
            }
        ],
        "supportedProperty": [
            {"@type": "SupportedProperty",
             "property": "http://schema.org/identifier",
             "title": "Identifier",
             "hydra:description": "Id with which the drone is stored at the central server ( Initially None).",
             "required": True,
             "readonly": False,
             "writeonly": False
             },

            {
                "@type": "SupportedProperty",
                "property": "http://auto.schema.org/speed",
                "hydra:description":"Current speed of the drone",
                "readable": True,
                "required": True,
                "title": "Speed",
                "writeable": True
            },
            {
                "@type": "SupportedProperty",
                "property": "http://schema.org/geo",
                "readable": True,
                "required": True,
                "hydra:description":"Current coordinates of the drone",
                "title": "Position",
                "writeable": True
            },
            {"@type": "SupportedProperty",
             "property": "http://schema.org/geo",
             "title": "Destination",
             "hydra:description": "Coordinates of the new destination",
             "required": True,
             "readonly": False,
             "writeonly": False
             },
            {
                "@type": "SupportedProperty",
                "property": "http://schema.org/fuelCapacity",
                "readable": True,
                "required": True,
                "hydra:description": "Battery status of the drone.",
                "title": "Battery",
                "writeable": True
            },
            {
                "@type": "SupportedProperty",
                "property": "http://schema.org/device",
                "readable": True,
                "required": True,
                "title": "Sensor",
                "hydra:description": "Sensors available in the drone.",
                "writeable": False
            },
            {
                "@type": "SupportedProperty",
                "property": "http://schema.org/name",
                "readable": True,
                "required": True,
                "title": "Name",
                "hydra:description":"Name of the drone ( will be used as the network alias)",
                "writeable": False
            },
            {
                "@type": "SupportedProperty",
                "property": "https://schema.org/status",
                "readable": True,
                "required": True,
                "title": "Status",
                "hydra:description":"Current status of the drone.",
                "writeable": True
            }
        ]
    },

]


## Classes that need to be a collection
collection_classes = ["order"]

## Classes that need to be shown at Entrypoint
entrypoint_classes = ["order", "info"]
