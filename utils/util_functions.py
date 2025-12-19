
from models.user import User
from utils.storage import load_from_json, save_to_json


def add_user(args):
    retrieved_data = load_from_json("data/data.json")
    all_users = [user for user in retrieved_data["users"]]
    user = next((u for u in all_users if u["name"] == args.name), None)

    if user:
        print(f"User with name {args.name} already exists. The user id is {user['id']}")
    else:
        new_user = User(args.name, args.email)
        retrieved_data["users"].append(new_user.to_dict())
        save_to_json("data/data.json", retrieved_data)
        print(f"✅ User {new_user.name} added successfully with id {new_user.id}")