import __builtin__

if '_' not in __builtin__.__dict__:
    __builtin__._ = lambda s: s

class ClientSideError(RuntimeError):
    pass

class InvalidInput(ClientSideError):
    def __init__(self, fieldname, value, msg=''):
        self.fieldname = fieldname
        self.value = value
        self.msg = msg

    def __unicode__(self):
        return _(u"Invalid input for field/attribute %s. Value: '%s'. %s") % (
                 self.fieldname, self.value, self.msg)

    def __str__(self):
        return unicode(self).encode('utf8', 'ignore')

class UnknownFunction(ClientSideError):
    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return _(u"Unknown function name: %s") % (self.name)

    def __str__(self):
        return unicode(self).encode('utf8', 'ignore')
