class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def show_info(self):
        print("Ім'я:", self.name)
        print("Телефон:", self.phone)
        print("Email:", self.email)
        print("------")



contacts = []


contact1 = Contact("Іван", "0991234567", "ivan@gmail.com")
contact2 = Contact("Марія", "0987654321", "maria@gmail.com")
contact3 = Contact("Олег", "0971112233", "oleg@gmail.com")

contacts.append(contact1)
contacts.append(contact2)
contacts.append(contact3)


for contact in contacts:
    contact.show_info()