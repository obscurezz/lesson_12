from pathlib import Path

BASE_DIR: str = Path(__file__).resolve().parent

UPLOAD_FOLDER: str = BASE_DIR.joinpath('uploads')

UPLOAD_IMAGES_DIR: str = UPLOAD_FOLDER.joinpath('images')


def image_to_path(filename: str) -> str:
    return UPLOAD_IMAGES_DIR.joinpath(filename)