
# ========= unpack list/tuple/dict

# def total(lira, kurus):
#     return (lira * 100) + kurus

# money = [5, 50]
# money = {"lira": 5, "kurus": 50}

# unpacking list/tuple dengan *
# unpacking dict dengan **
# print(total(**money), "kurus")


# ========== optional vary arg in function =========
# * to tuple form
# ** to dict form
def f(*args, **kwargs):
    print(args, kwargs)

f(5, lira=5)