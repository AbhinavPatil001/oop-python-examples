# Class: Blueprint for Man
class Man():
    # Methods: Functions that describe the behavior of Man
    def createName(Self,Name):
        Self.Name = Name
    def displayName(Self):
        return f"{Self.Name}"
    def sayHello(Self):
        return f"Hello {Self.Name}"

# Object: An instance of the Man class
man = Man()
