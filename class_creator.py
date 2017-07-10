"""Generate classes from parsed_classes with proper getter and setter for each Property."""

from api_docs.server_doc import server_doc
from api_docs.drone_doc import drone_doc


def create_setter(prop):
    """Create a setter for a given Property."""
    template = """def set_%s(self, value):
    self.%s = value""" % (prop["title"], prop["title"])
    name = "set_%s" % prop["title"]
    exec(template)
    return eval(name), name


def create_getter(prop):
    """Create a setter for a given Property."""
    template = """def get_%s(self):
    return self.%s""" % (prop["title"], prop["title"])
    name = "get_%s" % prop["title"]
    exec(template)
    return eval(name), name


def create_class(class_):
    """Create a class using a Hydra Class."""
    class_name = class_["title"]
    Class_ = type(class_name, (), {})

    # Adding setters and getters for class properties
    for prop in class_["supportedProperty"]:
        getfn, getname = create_getter(prop)
        setfn, setname = create_setter(prop)
        setattr(Class_, getname, getfn)
        setattr(Class_, setname, setfn)

    return Class_


def create_classes(classes):
    """Create a classes using parsed_classes."""
    class_dict = dict()
    for class_ in classes:
        class_dict[class_["title"]] = create_class(class_)
    return class_dict


if __name__ == "__main__":
    server_parsed_classes = server_doc["supportedClass"]
    drone_parsed_classes = drone_doc["supportedClass"]

    class_ = create_classes(drone_parsed_classes)
    print(class_)
