import cv2
from pathlib import Path


if __name__ == "__main__":
    path = Path("./a/b/c") / "e.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
    i = cv2.imread(path, 0)  # type: ignore
    print(i)
