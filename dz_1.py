import re


def email_parse(email_address):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    if not pattern.match(email_address):
        raise ValueError(f'wrong email:{email_address}')
    print(pattern.match(email_address).groupdict())


try:
    email_parse('someone@geekbrains.ru')
    email_parse('wolfrumilkik')
except ValueError as err:
    print(err)
