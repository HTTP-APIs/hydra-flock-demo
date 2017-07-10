"""API Doc templates generator."""


class HydraDoc():
    """Template for a new API Doc."""

    def __init__(self, API, title, desc, entrypoint, base_url):
        """Initialize the Hydra_APIDoc."""
        self.doc = {
            "@context": base_url + "contexts/" + API + ".jsonld",
            "@id": base_url + API + "/vocab",
            "@type": "ApiDocumentation",
            "title": title,
            "description": desc,
            "entrypoint": entrypoint,
            "supportedClass": [
            ],
            "possibleStatus": [
            ]
        }

    def add_supported_class(self, class_):
        """Add a new supportedClass."""
        self.doc["supportedClass"].append(class_)

    def add_possible_status(self, status):
        """Add a new possibleStatus."""
        self.doc["possibleStatus"].append(status)

    def to_json(self):
        """Return the Hydra JSON for the API Doc."""
        import json
        return json.dumps(self.doc, indent=4, sort_keys=True)

    def get(self):
        """Get the Hydra API Doc as a python dict."""
        return self.doc


class HydraClass():
    """Template for a new class."""

    def __init__(self, class_, title, desc, entrypoint, base_url, sub_classof=None):
        """Initialize the Hydra_Class."""
        self.class_ = {
            "@context": base_url + "context/" + class_ + ".jsonld",
            "@id": base_url + entrypoint + "/vocab#" + class_,
            "@type": "Class",
            "subClassOf": "null",
            "title": title,
            "description": desc,
            "supportedProperty": [

            ],
            "supportedOperation": [

            ]
        }
        if sub_classof is not None:
            self.class_["subClassOf"] = sub_classof

    def add_supported_prop(self, prop):
        """Add a new supportedProperty."""
        self.class_["supportedProperty"].append(prop)

    def add_supported_op(self, op):
        """Add a new supportedOperation."""
        self.class_["supportedOperation"].append(op)

    def to_json(self):
        """Return the Hydra JSON for the class."""
        import json
        return json.dumps(self.class_, indent=4, sort_keys=True)

    def get(self):
        """Get the Hydra class as a python dict."""
        return self.class_


class HydraProp():
    """Template for a new property."""

    def __init__(self, prop, title, read, write, required):
        """Initialize the Hydra_Prop."""
        self.prop = {
          "@type": "SupportedProperty",
          "title": title,
          "property": prop,
          "required": required,
          "readable": read,
          "writeable": write
        }

    def to_json(self):
        """Return the Hydra JSON for the prop."""
        import json
        return json.dumps(self.prop, indent=4, sort_keys=True)

    def get(self):
        """Get the Hydra prop as a python dict."""
        return self.prop


class HydraOp():
    """Template for a new Operation."""

    def __init__(self, id_, title, method, expects, returns, status):
        """Initialize the Hydra_Prop."""
        self.op = {
                "@type": "Operation",
                "@id": id_,
                "title": title,
                "method": method,
                "expects": expects,
                "returns": returns,
                "possibleStatus": status
            }

    def to_json(self):
        """Return the Hydra JSON for the op."""
        import json
        return json.dumps(self.op, indent=4, sort_keys=True)

    def get(self):
        """Get the Hydra op as a python dict."""
        return self.op
