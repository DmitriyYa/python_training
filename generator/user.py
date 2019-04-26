from model.myuser import MyUser
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default values
n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [MyUser(first_name="", last_name="", home_phone="", address="", email="")] + [
    MyUser(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 5),
           last_name=random_string("last_name", 10), nick_name=random_string("nick_name", 5),
           title=random_string("title", 5), company=random_string("company", 10),
           home_phone=random_string("home_phone", 15), mobile_phone=(random_string("mobile_phone", 15)),
           work_phone=random_string("work_phone", 15),
           fax_phone=random_string("fax_phone", 15), email=random_string("email", 10),
           email2=random_string("email2", 10), email3=random_string("email3", 10),
           homepage=random_string("homepage", 10), address=random_string("address", 20),
           address2=random_string("address2", 20), phone2=random_string("phone2", 10), notes=random_string("notes", 50))
    for i in range(n)
]

config_file_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(config_file_json, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))