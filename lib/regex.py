import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z]'*([A-z][ \-]{0,1})*"
name_regex = re.compile(name)

phone_number = r"\({0,1}[0-9]{3}\){0,1}[ \-]{0,1}[0-9]{3}[\-]{0,1}[0-9]{4}"
phone_regex = re.compile(phone_number)

email_address = r"^[^\d][.A-z0-9]+@[a-z]+.[a-z]{3}"
email_regex = re.compile(email_address)