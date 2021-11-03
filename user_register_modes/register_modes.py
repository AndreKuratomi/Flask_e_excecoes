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


def register_user(email: str, name: str):
    database_content = os.listdir(f"{database}")
    os.chdir(f"{database}")
    try:
        if not database_content:
            with open("database.json", "w") as json_file:
                id_number = len(database_content) + 1
                json_model = {"data": [{"nome": f"{name}", "email": f"{email.lower()}", "id": {id_number}}]}
                dump(json_model, json_file, indent=4)
            with open("database.json", "r") as json_file:
                result = load(json_file)
                return result, 201

        if email in database_content:
            raise EmailExistsError(email)

        if type(name) != str or type(email) != str:
            raise WrongTypesError(name, email)

        with open(f"{database_content}", "w") as json_file:
            id_number = len(database_content) + 1
            json_model = {"nome": f"{name}", "email": f"{email.lower()}", "id": f"{id_number}"}
            database_content.append(json_model, json_file, indent=4), 201

        return database_content, 201

    except EmailExistsError as email_error:
        return email_error.message, 409

    except WrongTypesError as types_error:
        return types_error.message, 404


