from typing import Dict


class FileManager:
    def __init__(self, file_paths):
        self._file_paths: Dict[str, str] = file_paths
    
    @property
    def text_file(self):
        return self._file_paths.get("text_file.txt")
    
    @property
    def text_files(self) -> Dict[str, str]:
        return {name: path for name, path in self.file_paths.items() if name.endswith('.txt')}
