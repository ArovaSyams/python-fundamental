import re

url = input("URL = ")

# (A|B)
# (...)
# (?:...) =  tidak termasuk dalam .group()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"username: {username}")

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url):
    print(f"Username: {matches.group(1)}")

