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


def register_user(nome: str, email: str):
    database_content = os.listdir(f"{database}")
    os.chdir(f"{database}")
    try:
        if not database_content:
            with open("database.json", "w") as json_file:
                data_list = {"data": []}
                dump(data_list, json_file, indent=4)

        if email in database_content:
            raise EmailExistsError(email)

        if type(nome) != str or type(email) != str:
            raise WrongTypesError(nome, email)

        another_list = []

        with open("database.json", "r") as json_file:
            result = load(json_file)
            result_data = result["data"]
            cap = nome.title()
            mail = email.lower()
            id_number = len(database_content) + 1
            json_model = {"nome": f"{cap}", "email": f"{mail}", "id": id_number}
            result_data.append(json_model)
            another_list = result_data
        with open("database.json", "w") as json_file:
            dump({"data": another_list}, json_file, indent=4)
            
        return json_file, 201

    except EmailExistsError as email_error:
        return email_error.message, 409

    except WrongTypesError as types_error:
        return types_error.message, 404


