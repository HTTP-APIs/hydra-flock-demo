"""API Doc templates generator."""


class HydraDoc():
    """Template for a new API Doc."""

    def __init__(self, API, title, desc, entrypoint, base_url):
        """Initialize the Hydra_APIDoc."""
        self.API = API
        self.base = base_url
        self.context = Context()
        self.parsed_classes = list()
        self.other_classes = list()
        self.collections = list()
        self.status = list()
        self.entrypoint = HydraEntryPoint()
        # self.doc = {
        #     "@context": self.context.get(),
        #     "@id": base_url + API + "/vocab",
        #     "@type": "ApiDocumentation",
        #     "title": title,
        #     "description": desc,
        #     "entrypoint": entrypoint,
        #     "supportedClass": [
        #     ],
        #     "possibleStatus": [
        #     ]
        # }

    def add_supported_class(self, class_, collection=False):
        """Add a new supportedClass."""
        # self.doc["supportedClass"].append(class_.get())
        self.parsed_classes.append(class_)
        if collection:
            collection = HydraCollection(class_)
            self.collections.append(collection)
            # self.doc["supportedClass"].append(collection.get())

    def add_possible_status(self, status):
        """Add a new possibleStatus."""
        self.status.append(status)

    def generate(self):
        """Get the Hydra API Doc as a python dict."""
        return self.doc

    def add_baseCollection(self):
        """Add Collection class to the API Doc."""
        collection = HydraClass("http://www.w3.org/ns/hydra/core#Collection", "Collection", None)
        member = HydraProp("http://www.w3.org/ns/hydra/core#member", "members", False, False, None)
        collection.add_supported_prop(member)
        self.other_classes.append(collection)

    def add_baseResource(self):
        """Add Resource class to the API Doc."""
        resource = HydraClass("http://www.w3.org/ns/hydra/core#Resource", "Resource", None)
        self.other_classes.append(resource)

    def add_to_context(self, key, value):
        """Add entries to the vocabs context."""
        self.context.add(key, value)



    def gen_Collections(self):
        """Create collections for all Collections in parsed_classes."""
        for class_ in self.collections:
            collection = gen_item_collection(class_)
            self.doc["supportedClass"].append(collection)


class HydraClass():
    """Template for a new class."""

    def __init__(self, id_, title, desc, sub_classof=None,):
        """Initialize the Hydra_Class."""
        self.id_ = id_
        self.title = title
        self.desc = desc
        self.parents = None
        self.supportedProperty = list()
        self.supportedOperation = list()
        if sub_classof is not None:
            self.parents = sub_classof

    def add_supported_prop(self, prop):
        """Add a new supportedProperty."""
        self.supportedProperty.append(prop)

    def add_supported_op(self, op):
        """Add a new supportedOperation."""
        self.supportedOperation.append(op)

    def generate(self):
        """Get the Hydra class as a python dict."""
        class_ = {
            "@id": self.id_,
            "@type": "hydra:Class",
            "subClassOf": self.parents,
            "title": self.title,
            "description": self.desc,
            "supportedProperty": [x.generate() for x in self.supportedProperty],
            "supportedOperation": [x.generate() for x in self.supportedOperation],
        }
        return class_


class HydraProp():
    """Template for a new property."""

    def __init__(self, prop, title, read, write, required):
        """Initialize the Hydra_Prop."""
        self.prop = prop
        self.title = title
        self.read = read
        self.write = write
        self.required = required

    def generate(self):
        """Get the Hydra prop as a python dict."""
        prop = {
          "@type": "SupportedProperty",
          "title": self.title,
          "property": self.prop,
          "required": self.required,
          "readable": self.read,
          "writeable": self.write
        }
        return prop


class HydraEntryPoint():
    """Template for a new entrypoint."""

    def __init__(self):
        """Initialize the Entrypoint."""
        self.entrypoint = HydraClass("vocab:EntryPoint", "EntryPoint", "The main entry point or homepage of the API.")
        self.entrypoint = {
                "@id": "vocab:EntryPoint",
                "@type": "hydra:Class",
                "subClassOf": None,
                "label": "EntryPoint",
                "description": "The main entry point or homepage of the API.",
                "supportedOperation": [
                    {
                        "@id": "_:entry_point",
                        "@type": "hydra:Operation",
                        "method": "GET",
                        "label": "The APIs main entry point.",
                        "description": None,
                        "expects": None,
                        "returns": "vocab:EntryPoint",
                        "statusCodes": [
                        ]
                    }
                ],
                "supportedProperty": []
        }

    def get(self):
        """Get the Hydra prop as a python dict."""
        return self.prop

    def add_supported_prop(self, prop):
        """Add supportedProperty to the EntryPoint."""
        self.entrypoint["supportedProperty"].append(prop)


class HydraClassOp():
    """Template for a new supportedOperation."""

    def __init__(self, title, method, expects, returns, status):
        """Initialize the Hydra_Prop."""
        self.op = {
                "@type": "hydra:Operation",
                "title": title,
                "method": method,
                "expects": expects,
                "returns": returns,
                "possibleStatus": status
            }

    def get(self):
        """Get the Hydra op as a python dict."""
        return self.op


class Context():
    """Class for JSON-LD context."""

    def __init__(self, id_, adders={}):
        """Initialize context."""
        # NOTE: adders is a dictionary containing additional context elements to the base Hydra context
        self.context = {
            "hydra": "http://www.w3.org/ns/hydra/core#",
            "property": {
                "@type": "@id",
                "@id": "hydra:property"
            },
            "supportedClass": "hydra:supportedClass",
            "supportedProperty": "hydra:supportedProperty",
            "supportedOperation": "hydra:supportedOperation",
            "code": "hydra:statusCode",
            "label": "rdfs:label",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "vocab": id_,
            # "vocab": "localhost/api/vocab#",
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
            }
        }

    def generate(self):
        """Get as a python dict."""
        return self.context

    def add(self, key, value):
        """Add entry to context."""
        self.context[key] = value


class HydraCollection():
    """Class for Hydra Collection."""

    def __init__(self, class_):
        """Generate Collection for a given class."""
        self.class_ = class_
        self.name = class_["title"]

        self.collection = {
            "@id": "vocab:%sCollection" % (self.name,),
            "@type": "hydra:Class",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "label": "%sCollection" % (self.name),
            "description": "A collection of %s" % (self.name.lower()),
            "supportedOperation": [
                {
                    "@id": "_:%s_create" % (self.name.lower()),
                    "@type": "http://schema.org/AddAction",
                    "method": "POST",
                    "description": None,
                    "expects": self.name,
                    "returns": self.name,
                    "statusCodes": [
                        {
                            "code": 201,
                            "description": "If the %s entity was created successfully." % (self.name,)
                        }
                    ]
                },
                {
                    "@id": "_:%s_collection_retrieve" % (self.name.lower(),),
                    "@type": "hydra:Operation",
                    "method": "GET",
                    "label": "Retrieves all %s entities" % (self.name,),
                    "description": None,
                    "expects": None,
                    "returns": "vocab:%sCollection" % (self.name),
                    "statusCodes": [
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "hydra:title": "members",
                    "hydra:description": "The %s" % (self.name.lower(),),
                    "required": None,
                    "readonly": False,
                    "writeonly": False

                }
            ]
        }

        def get(self):
            """Get as a python dict."""
            return self.collection


class EntryPointCollectionObject():
    """Class for a Collection Entry to the EntryPoint object."""

    def __init__(self, class_):
        """Create method."""
        self.name = class_["title"]
        self.object_ = {
            "property": {
                "@id": "vocab:EntryPoint/" + self.name,
                "@type": "hydra:Link",
                "label": self.name,
                "description": "The %s collection" % (self.name,),
                "domain": "vocab:EntryPoint",
                "range": "vocab:%sCollection" % (self.name,),
                "supportedOperation": [
                    {
                        "@id": "_:%s_collection_retrieve" % (self.name.lower(),),
                        "@type": "hydra:Operation",
                        "method": "GET",
                        "label": "Retrieves all %s entities" % (self.name,),
                        "description": None,
                        "expects": None,
                        "returns": "vocab:%sCollection" % (self.name,),
                        "statusCodes": [
                        ]
                    }
                ]
            },
            "hydra:title": self.name.lower(),
            "hydra:description": "The %s collection" % (self.name,),
            "required": None,
            "readonly": True,
            "writeonly": False
        }

    def get(self):
        """Get as a python dict."""
        return self.collection


class EntryPointOpObject():
    """Class for a Operation Entry to the EntryPoint object."""

    def __init__(self, name, description, method, expects, returns):
        """Create method."""
        self.object_ = {
            "property": {
                "@id": "vocab:EntryPoint/" + name,
                "@type": "hydra:Link",
                "label": name,
                "description": description,
                "domain": "vocab:EntryPoint",
                "range": "vocab:%sCollection" % (name,),
                "supportedOperation": [
                    {
                        "@id": "_:" + name.lower(),
                        "@type": "hydra:Operation",
                        "method": method,
                        "label": name,
                        "description": None,
                        "expects": expects,
                        "returns": returns,
                        "statusCodes": [
                        ]
                    }
                ]
            },
            "hydra:title": name.lower(),
            "hydra:description": "The %s collection" % (name,),
            "required": None,
            "readonly": True,
            "writeonly": False
        }
