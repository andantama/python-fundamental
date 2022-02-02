users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
    }
}
print(users)
print(users["email"])

print("\nUbah DICT ke JSON")
import json
result = json.dumps(users)
print(result)

with open("result.json", "w") as file:
    json.dump(users, file)
