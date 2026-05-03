from pathlib import Path
import numpy as np
import cv2
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import pyautogui


def load(path: Path, flags: int | None = None) -> np.ndarray | None:
    arr = None
    if flags is not None:
        arr: np.ndarray | None = cv2.imread(path, flags)
    else:
        arr: np.ndarray | None = cv2.imread(path)
    return arr


def save(
    img: np.ndarray | None,
    path: Path,
    region: tuple[int, int, int, int] | None = None,  # (left, upper, right, lower)
) -> None:
    if img is None:
        return

    img = crop(img, region) if region is not None else img

    if img is None:
        return

    Image.fromarray(img).save(path)


def crop(
    img: np.ndarray | None,
    region: tuple[int, int, int, int],  # (left, upper, right, lower)
) -> np.ndarray | None:
    if img is None:
        return None

    left, upper, right, lower = region
    return img[upper:lower, left:right]


def find_mask_first_position(mask: bool) -> tuple[int, int] | None:
    y_coords, x_coords = np.where(mask)

    if len(x_coords) == 0 or len(y_coords) == 0:
        return None

    return (x_coords[0], y_coords[0])
