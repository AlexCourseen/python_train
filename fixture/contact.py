from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_xpath("//*[@type='button'][@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_contact_value(self, cont_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(cont_field_name).click()
            wd.find_element_by_name(cont_field_name).clear()
            wd.find_element_by_name(cont_field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.firstName)
        self.change_contact_value("lastname", contact.lastName)

    def add(self, new_contact_data):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contacts_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_index(index)
        #init edit contact
        wd.find_elements_by_xpath("//*[@title='Edit']")[index].click()
        #fill edit contact form
        self.fill_contact_form(new_contact_data)
        #submit edit contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//*[@type='button'][@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contacts_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count_contacts(self):
        wd = self.app.wd
        self.home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                firstName = element.find_element_by_css_selector("td:nth-child(3)").get_attribute("outerText")
                lastName = element.find_element_by_css_selector("td:nth-child(2)").get_attribute("outerText")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contacts_cache.append(Contact(firstName=firstName, lastName=lastName, id=id))
        return list(self.contacts_cache)


