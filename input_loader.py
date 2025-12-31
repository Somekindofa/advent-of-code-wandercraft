from pathlib import Path

class InputLoader:    
    def __init__(self, filename):
        """Initialize with the input filename"""
        if not Path(filename).exists():
            raise ValueError(f"The file {filename} does not exist.")
        self.filename = filename
        self._content = None
    
    def load(self):
        """Load the file content into memory"""
        with open(self.filename, 'r') as f:
            self._content = f.read()
        return self._content
    
    @property
    def content(self):
        """Get the loaded content."""
        if self._content is None:
            self.load()
        return self._content
