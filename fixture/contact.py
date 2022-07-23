from model.contact import Contact
import re


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
        self.change_contact_value("home", contact.homePhone)
        self.change_contact_value("mobile", contact.mobilePhone)
        self.change_contact_value("work", contact.workPhone)
        self.change_contact_value("phone2", contact.secondaryPhone)

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
        #init edit [index] contact
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
            for row in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = row.find_elements_by_tag_name("td")
                firstName = cells[2].text
                lastName = cells[1].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                # all_phones = cells[5].text.splitlines() - нарезка текста splitlines"""
                # self.contacts_cache.append(Contact(firstName=firstName, lastName=lastName, id=id,
                                                  # homePhone=all_phones[0], mobilePhone=all_phones[1],
                                                   # workPhone=all_phones[2], secondaryPhone=all_phones[3]))
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contacts_cache.append(Contact(firstName=firstName, lastName=lastName, id=id,address=address,
                                                   all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page = all_phones))
        return list(self.contacts_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homePhone = wd.find_element_by_name("home").get_attribute("value")
        mobilePhone = wd.find_element_by_name("mobile").get_attribute("value")
        workPhone = wd.find_element_by_name("work").get_attribute("value")
        secondaryPhone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstName=firstname, lastName=lastname, id=id, homePhone=homePhone, mobilePhone=mobilePhone,
                       workPhone=workPhone, secondaryPhone=secondaryPhone, address=address, email=email, email2=email2,
                       email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homePhone = re.search("H: (.*)", text).group(1)
        workPhone = re.search("W: (.*)", text).group(1)
        mobilePhone = re.search("M: (.*)", text).group(1)
        secondaryPhone = re.search("P: (.*)", text).group(1)
        return Contact(homePhone=homePhone, mobilePhone=mobilePhone,
                       workPhone=workPhone, secondaryPhone=secondaryPhone)





