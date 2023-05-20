import json

def idk(user:str):
    str(user)
    with open("users.json", "r+") as file:
        data = json.load(file)

    try:
        with open("users.json", "w") as file:
            data[user] = int(data[user]) + 1
            json.dump(data, file)


    except KeyError:
        # User does not exist in Json,
        # lets add them to the json
        with open("users.json", "w") as file:
            temp_dict = {user: 1}
            data.update(temp_dict)
            file.seek(0)
            json.dump(data, file)
    

    with open("users.json","r") as file:
        data = json.load(file)
        return f"{user}'s Based counter: {data[user]}"
