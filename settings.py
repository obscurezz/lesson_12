from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent

LOGS_FOLDER: Path = BASE_DIR.joinpath('logs')

UPLOAD_FOLDER: Path = BASE_DIR.joinpath('uploads')

UPLOAD_IMAGES_DIR: Path = UPLOAD_FOLDER.joinpath('images')


def image_to_path(filename: str) -> Path:
    return UPLOAD_IMAGES_DIR.joinpath(filename)
