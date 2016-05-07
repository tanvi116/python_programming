class SomeClass:
    first = ""
    second = ""

def DoIt(o,a):
    return (getattr(o,a))


o = SomeClass()
o.first = "fizz"
o.second = "buzz"

print DoIt(o,"first")
print DoIt(o,"second")

