# families = {
#     "wifqo": "family",
#     "arova": "family",
#     "syams": "foreign"
# }

# print(families["arova"])

# for family in families:
#     print(family, families[family])

# =================

families = [
    {"name": "wifqo", "type": "family", "age": 12},
    {"name": "arova", "type": "family", "age": 15},
    {"name": "syams", "type": "foreigner", "age": 23},
    {"name": "tralala", "type": "family", "age": None},
]

for family in families:
    print(family["name"], family["type"], family["age"], sep=", ")
