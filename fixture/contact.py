from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.init_editing()
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def init_editing(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()

    def fill_contact_form(self, contact):
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("mobile", contact.mobile_phone)
        self.app.change_field_value("email", contact.email)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            firstname = element.find_elements_by_css_selector("td")[2].text
            lastname = element.find_elements_by_css_selector("td")[1].text
            contacts.append(Contact(id = id, firstname = firstname, lastname = lastname))
        return contacts







