# Worksheet 1.5: Person class

import datetime
class Person:
    """this defines a person name and birthday"""
    def __init__(self,name,birth):
        """initialises the person object"""
        name = str(name)
        if isinstance(birth, datetime.date):
            raise TypeError
        self.name = name
        self.birth = birth
    def is_birthday(self):
        """check if it is persons birthday yay :D"""
        today = str(date.today()[4:])
        birthday = str(self.birth[4:])
        if today == birthday:
            return True
        else:
            return False
    def initials(self):
        """persons initials"""
        initials = ""
        for i in range (len(self.name.title())):
            if self.name[i].isupper():
                initials += self.name[i]
        return initials
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
