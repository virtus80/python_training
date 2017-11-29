from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='fitrstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        nickname = Optional(str, column='nickame')
        company = Optional(str, column='company')
        address = Optional(str, column='address')
        homephone = Optional(str, column='home')
        workphone = Optional(str, column='work')
        mobilephone = Optional(str, column='mobile')
        secondaryphone = Optional(str, column='phone2')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders, autocommit=True)
        self.db.generate.mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, nickname=contact.nickname,
            company=contact.company, address=contact.address, homephone=contact.homephone, workphone=contact.workphone, mobilephone=contact.mobilephone,
            secondaryphone=contact.secondaryphone, email=contact.email, email2=contact.email2, email3=contact.email3)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))