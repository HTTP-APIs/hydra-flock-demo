"""Parsed Classes templates generator for hydrus. Here parsed_classes refers
to the classes being parsed from RDF/OWL vocabulary. If you user don't have
a RDF/OWL vocab defined the he can use this script to generate parsed_classes.
Parsed Classes is just a set of hydra Classes that hydrus needs to generate
the ApiDocumentation."""


class ParsedClasses():
    """Create a parsed_classes list for hydrus vocab_generator."""

    def __init__(self):
        """Initialize the ParsedClasses."""
        self.parsed_classes = []

    def add_supported_class(self, class_):
        """Add a new supportedClass."""
        self.parsed_classes.append(class_)

    def get(self):
        """Get the parsed_classes as a python list."""
        return self.parsed_classes


class HydraClass():
    """Template for a new class."""

    def __init__(self, id_, title, desc, entrypoint, base_url, sub_classof=None):
        """Initialize the Hydra_Class."""
        self.class_ = {
            "@id": id_,
            "@type": "Class",
            "subClassOf": None,
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

## NOTE: we don't need this as we'll be keeping everything in Python Dict format.
## The python dicts are converted to json in App.py, this makes using generated
## things in other scripts easy.

    # def to_json(self):
    #     """Return the Hydra JSON for the class."""
    #     import json
    #     return json.dumps(self.class_, indent=4, sort_keys=True)
    #

    def get(self):
        """Get the Hydra class as a python dict."""
        return self.class_


class HydraProp():
    """Template for a new property."""

    def __init__(self, prop, title, desc, read, write, required):
        """Initialize the Hydra_Prop."""
        self.prop = {
          "@type": "SupportedProperty",
          "title": title,
          "property": prop,
          "description": desc,
          "required": required,
          "readable": read,
          "writeable": write
        }
    #
    # def to_json(self):
    #     """Return the Hydra JSON for the prop."""
    #     import json
    #     return j\son.dumps(self.prop, indent=4, sort_keys=True)
    #
    def get(self):
        """Get the Hydra prop as a python dict."""
        return self.prop


class HydraOp():
    """Template for a new Operation."""

    def __init__(self, id_, label, desc, method, expects, returns, status):
        """Initialize the Hydra_Prop."""
        self.op = {
                "@type": "hydra:Operation",
                "@id": id_,
                "label": label,
                "description": desc,
                "method": method,
                "expects": expects,
                "returns": returns,
                "statusCodes": status
            }
    #
    # def to_json(self):
    #     """Return the Hydra JSON for the op."""
    #     import json
    #     return json.dumps(self.op, indent=4, sort_keys=True)
    #
    def get(self):
        """Get the Hydra op as a python dict."""
        return self.op
