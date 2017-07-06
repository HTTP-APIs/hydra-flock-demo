"""API Doc templates generator."""


def hydra_doc(API, title, desc, entrypoint):
    """Template for a new API Doc."""
    return {
        "@context": "http://hydrus.com/contexts/"+API+".jsonld",
        "@id": "http://hydrus.com/"+API+"/vocab",
        "@type": "ApiDocumentation",
        "title": title,
        "description": desc,
        "entrypoint": entrypoint,
        "supportedClass": [
        ],
        "possibleStatus": [
        ]
    }


def hydra_class(class_, title, desc, entrypoint):
    """Template for a new class."""
    return {
        "@context": "http://hydrus.com/context/"+class_+".jsonld",
        "@id": "http://hydrus.com/"+entrypoint+"/vocab/"+class_,
        "@type": "Class",
        "title": title,
        "description": desc,
        "supportedProperty": [

        ],
        "supportedOperation": [

        ]
    }


def hydra_prop(prop, title, read, write, required):
    """Template for a new property."""
    return {
      "@type": "SupportedProperty",
      "title": title,
      "property": prop,
      "required": required,
      "readable": read,
      "writeable": write
    }


def hydra_op(id_, title, method, expects, returns, status):
    """Template for a new Operation."""
    return {
            "@type": "Operation",
            "@id": id_,
            "title": title,
            "method": method,
            "expects": expects,
            "returns": returns,
            "possibleStatus": status
        }
