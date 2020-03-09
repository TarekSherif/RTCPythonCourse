
l1 = [
    {"id": 2, "name": "Manal Fakieh", "salary": 5000},
    {"id": 5, "name": "Mohamed Eid", "salary": 6000},
    {"id": 8, "name": "Marwa Hussen", "salary": 5000},
    {"id": 9, "name": "Yousef Hatem", "salary": 5000},
    {"id": 10, "name": "Shaima Azoz", "salary": 5000},
]


def search_in_list(id):
    for emp in l1:
        if emp["id"] == id:
            return emp
    else:
        return {}


print(search_in_list(11))
