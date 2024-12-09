from models.Customer import Customer, Customer_List

def create_customers():
    janet = Customer(
        name="Janet Thomas",
        age=64,
        id="I19273",
        email="janetthomas@gmail.com",
        recent_change="Recently turned 64",
    )

    john = Customer(
        name="John Collins",
        age=41,
        id="I72652",
        email="johncollins@xyzcompany.com",
        recent_change="Child recently turned 25",
    )

    oliver = Customer(
        name="Oliver Paul",
        age=42,
        id="I61492",
        email="oliverpaul@gmail.com",
        recent_change="Purchased new vehicle",
    )

    mary = Customer(
        name="Mary Green",
        age=46,
        id="I18624",
        email="marygreen@abcinsurance.com",
        recent_change="Recently moved to new home",
    )

    sam = Customer(
        name="Sam Anthony",
        age=42,
        id="I92675",
        email="samanthony@xyzcompany.com",
        recent_change="Dental coverage upgraded",
    )

    customer_list = list()
    customer_list.append(john)
    customer_list.append(janet)
    customer_list.append(oliver)
    customer_list.append(mary)
    customer_list.append(sam)

    customer_list = Customer_List(
        totalSize=5,
        records=customer_list
    )

    return customer_list
