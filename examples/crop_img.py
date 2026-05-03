from chrono_marco2 import ndarray_img
from pathlib import Path


path = Path(__file__).parent / "data" / "tmp"
a = ndarray_img.load(path / "tmp_screenshot.png")
ndarray_img.save(a, path / "tmp_cropped.png", (500, 200, 900, 600))
