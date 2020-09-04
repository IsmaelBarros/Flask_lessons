class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def do_something(self):
        raise ValueError()

    def __str__(self):
        return self._name + ", " + self._email


# users = [User("Ismael", "ismael@gmail.com"), User("Maira", "maira@gmail.com")]

# for user in users:
#     user.do_something()

a = {}

b = a.pop('username', None)

print(b)
