# Worksheet 1.5: Person class

from datetime import date
class Person:
    """im going to kill myself"""
    def __init__(self,name,birth):
        """im going to kill myself"""
        try:
            name = str(name)
            birth = birth.date()
            self.name = name
            self.birth = birth
        except:
            raise TypeError
    def is_birthday(self):
        """im going to kill myself"""
        today = str(date.today()[4:])
        birthday = str(self.birth[4:])
        if today == birthday:
            return True
        else:
            return False
    def initials(self):
        """im going to kill myself"""
        initials = ""
        for i in range (len(self.name.title())):
            if self.name[i].isupper():
                initials += self.name[i]
        return initials
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
