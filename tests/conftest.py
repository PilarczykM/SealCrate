import os
import shutil
import tempfile
from typing import Dict, Tuple
import pytest

from tests.model import FileManager

directory = os.path.join(os.path.dirname(__file__), "test_files")

@pytest.fixture()
def fixture_file_manager():
    temp_dir, file_paths = _copy_content(directory)
    file_manager = FileManager(file_paths)
    yield file_manager
    shutil.rmtree(temp_dir)

@pytest.fixture()
def fixture_text_file_path(fixture_file_manager):
    yield fixture_file_manager.text_file


def _copy_content(source_dir: str) -> Tuple[str, Dict[str, str]]:
    temp_dir = tempfile.mkdtemp()
    file_paths = {}
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        if os.path.isfile(source_file):
            destination_file = os.path.join(temp_dir, file_name)
            shutil.copyfile(source_file, destination_file)
            file_paths[file_name] = destination_file
    return temp_dir, file_paths
