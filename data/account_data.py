from datetime import date
from models.Account import Account

def create_accounts():
    a1 = Account(
        id = "I19273",
        email = "janetthomas@gmail.com",
        name = "Janet Thomas",
        dob = date(1961,4,17),
        addr1 = "44 North St",
        addr2 = "Indian Hills",
        city = "Wichita"
    )

    acc_list = list()
    acc_list.append(a1)
    return acc_list