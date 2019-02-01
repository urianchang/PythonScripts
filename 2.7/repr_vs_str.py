def type_name(class_type):
    """
    Given a Class Type Definition, determine the string form of its name and module location.

    :param __builtin__.type class_type: The type definition of a class

    :return: String containing class name and model location if present.
    :rtype: str
    """
    name = []
    module = getattr(class_type, '__module__', None)
    if module is not None:
        name.append(module)

    name.append(class_type.__name__)
    return '.'.join(name)


class Something(Exception):
    description = {
        'color': "blue",
        'size': "HUGE",
    }
    details = {}

    def __str__(self):
        return repr((self.description, self.details))

    def __repr__(self):
        class_name = type_name(type(self))
        rpr = u'{0}(color={1.description!r}, details={1.details!r}>'
        return rpr.format(class_name, self).encode('utf8')


a = Something()
print "%s(%r)" % (a, a)
print "{0!s}({1!r})".format(a, a)
