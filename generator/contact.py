from model.contact import Contact
import random
import string
import os.path
import jsonpickle
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
    elif o =="-f":
        f = a

def random_string_for_names(prefix, maxlen):
    symbols = string.ascii_letters + "'" + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phones(maxlen):
    symbols = string.digits*3 + " +()" + "-"*3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_address(maxlen):
    symbols = string.ascii_letters + string.digits + " ,."*5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_email(maxlen):
    symbols = string.ascii_letters*3 + string.digits + "-_#&+"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string_for_names("name", 15), lastname=random_string_for_names("surname", 20),
            nickname=random_string_for_address(20), company=random_string_for_names("company", 30),
            address=random_string_for_address(60), homephone=random_string_for_phones(14),
            workphone=random_string_for_phones(14), mobilephone=random_string_for_phones(14),
            secondaryphone=random_string_for_phones(14),email=random_string_for_email(30) + "@" + random.choice(["mail.ru", "gmail.com",
            "yandex.ru", "i.ua", "ukr.net"])) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))