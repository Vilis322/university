class Person:
    name = ''
    parent = None


grandmother = Person()
grandmother.name = "Grandmother"

mother = Person()
mother.name = "Mother"
mother.parent = grandmother

daughter = Person()
daughter.name = "Daughter"
daughter.parent = mother

print(daughter.name)

print(daughter.parent.name)

print(daughter.parent.parent.name)
