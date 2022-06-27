class ContactHelper:
    def __init__(self, app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstName)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastName)

    def add(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.home_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #init edit contact
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        #fill edit contact form
        self.fill_contact_form(contact)
        #submit edit contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.home_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//*[@type='button'][@value='Delete']").click()
        wd.switch_to.alert.accept()
