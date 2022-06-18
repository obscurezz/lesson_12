import json


class JsonLoader:
    def __init__(self, jsonfile):
        self.__jsonfile = jsonfile

    def load_from_json_by_value(self, value: str | None) -> list[dict] | str:
        """Loads data from json file where value is a keyword for search in content"""
        try:
            with open(self.__jsonfile, 'r', encoding='utf-8') as file:
                opened_file = json.load(file)
                result_list = [obj_ for obj_ in opened_file if value.lower() in obj_['content'].lower()]
                return result_list
        except FileNotFoundError:
            return f'No such file in the project'

    def upload_data_to_json(self, value: dict) -> None | str:
        """Uploads new data to json file, based on correct dictionary"""
        try:
            # open to read and load json
            with open(self.__jsonfile, 'r', encoding='utf-8') as file:
                temp_json = json.load(file)
                temp_json.append(value)
            # open to rewrite json with appended data
            with open(self.__jsonfile, 'w', encoding='utf-8') as file:
                json.dump(temp_json, file, ensure_ascii=False, indent=4, separators=(',', ': '))

        except FileNotFoundError:
            return f'No such file in the project'


def create_content_dict(picture: str, content: str) -> dict:
    """Creates correct dictionary to append to json file"""
    return {"pic": picture, "content": content}


def is_filename_allowed(filename: str) -> bool:
    """Checks if our file is the picture"""
    allowed_extensions = {'bmp', 'png', 'jpg', 'jpeg', 'gif'}
    # getting extension of file
    extension: str = filename.split(".")[-1]
    if extension in allowed_extensions:
        return True
    return False
