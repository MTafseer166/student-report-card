#contact book

names = ["Ali", "Sara", "Hina", "Ali", "Bilal", "Sara"]
phones = ("0300-111", "0301-222", "0302-333", "0300-111", "0303-444", "0301-222")

correction= set(names)
phone_correction= set(phones)

print("Different people are:", len(correction))

contacts = {
    "Ali": "0300-111",
    "Sara": "0301-222",
    "Hina": "0302-333",
    "Ali": "0300-111",
    "Bilal" : "0303-444",
    "Sara" : "0301-222"
}

contacts.update({"zain": "0304-555"})

search = input("Enter your name:")
print(contacts.get(search, "Contact not found"))

contacts.pop("Bilal")

for name, phone in contacts.items():
    print(name, "->", phone)