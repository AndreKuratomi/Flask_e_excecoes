from dotenv import load_dotenv
import os
from os import getenv

from json import dump, dumps, load, loads
from register_errors.errors import EmailExistsError, WrongTypesError

load_dotenv()

database = getenv("DATABASE")


def read_register():
    database_content = os.listdir(f"{database}")
    os.chdir(f"{database}")

    if database_content:
        try:
            with open("database.json", "r") as json_file:
                load(json_file)
        except:
            print("irk")
            data_list = {"data": []}
            with open("database.json", "w") as json_file:
                dump(data_list, json_file, indent=4)
            with open("database.json", "r") as json_file:
                result = load(json_file)
                return result, 200

        with open("database.json", "r") as json_file:
            result = load(json_file)
            return result, 200

    new_database = {"data": []}
    with open("database.json", "w") as json_file:
        dump(new_database, json_file, indent=4)
    with open("database.json", "r") as json_file:
        result = load(json_file)
        return result, 200



def register_user(data_json, name, email):
    try:
        if not data_json:
            with open("database.json", "w") as json_file:
                json_model = {"data": [{"email": f"{email}", "nome": f"{name}", "id": 1}]}
                dump(json_model, json_file, indent=4), 201

        if email in data_json:
            raise EmailExistsError(email)

        if type(name) != str or type(email) != str:
            raise WrongTypesError(name, email)

        with open(f"{data_json}", "w") as json_file:
            # id_number = 0
            # for id in data_json.data:

            json_model = {"email": f"{email}", "nome": f"{name}", "id": 1}
            data_json.data.append(json_model, json_file, indent=4), 201

        return data_json, 201

    except EmailExistsError as email_error:
        return email_error.message, 409

    except WrongTypesError as types_error:
        return types_error.message, 404


