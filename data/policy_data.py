from models.Policy import Policy, Policy_List
from datetime import date

def create_policies():
    p1 = Policy(id="1",
                account_id="I19273",
                status="Closed",
                product="Travel",
                startDate = date(2023,4,17),
                endDate = date(2024,4,17),
                provider = "ACME Insurance",
                premium = 245.33,
                notes = "Includes extra cover of $2000 for camera equipment."
                )
    p2 = Policy(id="2",
                account_id="I19273",
                status="Active",
                product="Home",
                startDate=date(2022, 1, 17),
                endDate=date(2025, 1, 17),
                provider = "Speedy",
                premium = 245.33,
                notes = "Important information about this policy"
                )
    p_list = list()
    p_list.append(p1)
    p_list.append(p2)

    return p_list