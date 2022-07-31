from model.contact import Contact
import random
import os.path
import jsonpickle
import string #хранит константы символов
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #десять пробелов для частоты появления их
    # сгенерирована случайная длинна не больше MAX
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstName="", lastName="", homePhone="", mobilePhone="", workPhone="", secondaryPhone="",
                    address="", email="", email2="", email3="")] + \
           [Contact(lastName=random_string('lastName', 10), firstName=random_string('firstName', 20),
                    homePhone=random_string('homePhone', 20), mobilePhone=random_string('mobilePhone', 20),
                    workPhone=random_string('workPhone', 20), secondaryPhone=random_string('secondaryPhone', 20),
                    address=random_string('address', 20), email=random_string('email', 20),
                    email2=random_string('email2', 20), email3=random_string('email3', 20))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)# ..-точки для перехода на один урровень верх,
 # чтобы получилось "..data/<file_name>.json"

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
