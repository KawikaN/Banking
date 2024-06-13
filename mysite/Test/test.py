class person():
    def __init__(self, hi):
        self.hi = hi
    def a(self):
        return  self.hi

class freind(person):
    def b(self):
        return super().a()


kawika = freind("hi")

users = []


users.append("hey")

print(users)