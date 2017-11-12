from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, nickname=None, company=None, address=None,
                 all_phones_from_homepage=None, homephone=None, workphone=None, mobilephone=None,
                 secondaryphone=None, all_emails_from_homepage=None, email=None, email2=None, email3=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.all_phones_from_homepage=all_phones_from_homepage
        self.homephone = homephone
        self.workphone=workphone
        self.mobilephone = mobilephone
        self.secondaryphone=secondaryphone
        self.all_emails_from_homepage=all_emails_from_homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3

    def __repr__(self):
        return "%s:%s (%s) (%s) (%s) (%s)" % (self.id, self.firstname, self.lastname, self.address, self.mobilephone, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
