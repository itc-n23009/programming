name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}


def dict_info(dict_tbl, key):
    return dict_tbl.get(key, "key is not found")


print(dict_info(name_age, "satou"))
print(dict_info(name_age, "yamada"))
