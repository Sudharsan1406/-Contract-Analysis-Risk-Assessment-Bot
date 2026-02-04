import os
import uuid

ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}


def get_file_extension(filename: str) -> str:
    """
    Returns file extension without dot.
    Example: contract.pdf -> pdf
    """
    return filename.split(".")[-1].lower()


def is_allowed_file(filename: str) -> bool:
    """
    Check if uploaded file type is supported.
    """
    return get_file_extension(filename) in ALLOWED_EXTENSIONS


def generate_temp_filename(original_name: str) -> str:
    """
    Generates a safe temporary filename to avoid collisions.
    """
    ext = get_file_extension(original_name)
    unique_id = uuid.uuid4().hex
    return f"{unique_id}.{ext}"


def ensure_directory(path: str):
    """
    Create directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)
