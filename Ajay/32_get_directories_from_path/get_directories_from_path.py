import re


def get_directories_from_path(path):
    directories = re.findall(r'\b(\w+)(?=/)(?!\.)', path)
    return directories
