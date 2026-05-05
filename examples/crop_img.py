from chrono_marco2 import ndarray_img
from pathlib import Path
from PIL import Image

def crop_image(input_path: Path, output_path: Path, crop_region: tuple[int, int, int, int]):
    # Crop the image to the region (left, upper, right, lower)
    img = Image.open(input_path)
    cropped_img = img.crop(crop_region)
    cropped_img.save(output_path)


path = Path(__file__).parent / "data" / "tmp"
crop_image(path / "tmp_screenshot.png", path / "tmp_cropped.png", (470, 290, 830, 390))
