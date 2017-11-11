from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, nickname=None, company=None, address=None, mobile_phone=None, email=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.mobile_phone = mobile_phone
        self.email = email

    def __repr__(self):
        return "%s:%s %s: %s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
