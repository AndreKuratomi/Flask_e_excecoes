from json import dump, dumps, load


class EmptyDatabase(Exception):
    def __init__(self):
        data_list = {"data": []}
        # json_string_data = dumps(data_list)
        with open("database.json", "w") as json_file:
            dump(data_list, json_file, indent=4)


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
                    "name": f"{self.types[type(name)]}"
                },
                {
                    "email": f"{self.types[type(email)]}"
                }
            ]
        }
        super().__init__(self.message)


