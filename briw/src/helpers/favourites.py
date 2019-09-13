def addFavourite(user_id, drink_id, people):
    try:
        user = people[user_id]
        if not "favourites" in user.keys():
            user["favourites"] = []
        user["favourites"].append(drink_id)
        people[user_id] = user
        return people, True
    except:
        return people, False

def removeFavourite(user_id, drink_id, people):
    try:
        people[user_id]["favourites"].remove(drink_id)
        return people, True
    except:
        return people, False