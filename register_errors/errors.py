from json import dump, dumps, load


class EmptyDatabase(Exception):
    def __init__(self):
        data_list = {"data": []}
        # json_string_data = dumps(data_list)
        with open("database.json", "w") as json_file:
            dump(data_list, json_file, indent=4)


class EmptyDirectory(Exception):
    def __init__(self):
        new_database = {"data": [{"email": "mail@mail.com", "id": 1, "name": "Lorem Ipsum Dolor, Phd"}]}
        with open("database.json", "w") as json_file:
            dump(new_database, json_file, indent=4)
        with open("database.json", "r") as json_file:
            result = load(json_file)
            return result, 200


class EmailExistsError(Exception):
    def __init__(self, email):
        self.message = {"message": f"{email} already exists!"}, 409
        super().__init__(self.message)


class WrongTypesError(Exception):
    types = {
        str: "string",
        int: "integer",
        float: "float",
        bool: "boolean",
        list: "list",
        dict: "dict"
    }

    def __init__(self, name, email):
        self.message = {
            "wrong fields": [
                {
                    "name": f"{type(name)}"
                },
                {
                    "email": f"{type(email)}"
                }
            ]
        }
        super().__init__(self.message)


