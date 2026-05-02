from pathlib import Path
import dxcam  # type: ignore
import numpy as np
import cv2
from PIL import Image
from skimage.metrics import structural_similarity as ssim


class EyeStatus:
    def __init__(self, camera: dxcam.DXCamera | None = None):
        self.camera = camera if camera is not None else dxcam.create()
        self.camera.start(target_fps=60)

        self.current_frame: np.ndarray | None = None
        self.current_frame_mini_map_title: np.ndarray | None = None
        self.current_same_map_score: float | None = None
        self.current_is_same_map: bool | None = None
        self.current_frame_mini_map: np.ndarray | None = None
        self.current_yellow_point_position_in_mini_map: tuple[int, int] | None = None
        self.current_red_point_position_in_mini_map: tuple[int, int] | None = None


class Eye:
    def __init__(
        self,
        mini_map_title_path: Path,
        mini_map_title_region: tuple[int, int, int, int],  # (left, upper, right, lower)
        mini_map_region: tuple[int, int, int, int],  # (left, upper, right, lower)
        ssim_same_map_score_threshold: float = 0.999,
        camera: dxcam.DXCamera | None = None,
        status: EyeStatus | None = None,
    ) -> None:
        self.mini_map_title_path = mini_map_title_path
        self.mini_map_title_path.parent.mkdir(parents=True, exist_ok=True)
        self.mini_map_title_path.touch()
        
        self.mini_map_title: np.ndarray | None = cv2.imread(mini_map_title_path, 0)  # type: ignore
        self.mini_map_title_region = mini_map_title_region
        self.mini_map_region = mini_map_region
        self.ssim_same_map_score_threshold = ssim_same_map_score_threshold
        self.status = status if status is not None else EyeStatus(camera)

    def save_screenshot(
        self, path: Path, region: tuple[int, int, int, int] | None = None
    ) -> None:
        if self.update_current_frame() is None:
            return
        current_frame = (
            self.crop_current_frame(region) if region else self.status.current_frame
        )
        if current_frame is None:
            return

        Image.fromarray(current_frame).save(path)

    def save_current_frame_mini_map_title(self) -> None:
        self.save_screenshot(self.mini_map_title_path, self.mini_map_title_region)

    def save_current_frame_mini_map(self, path: Path) -> None:
        self.save_screenshot(path, self.mini_map_region)

    def crop_current_frame(
        self, region: tuple[int, int, int, int]
    ) -> np.ndarray | None:
        if self.status.current_frame is None:
            return None

        left, upper, right, lower = region
        return self.status.current_frame[upper:lower, left:right]

    def update_current_frame(
        self,
    ) -> np.ndarray | None:
        self.status.current_frame = self.status.camera.get_latest_frame()
        return self.status.current_frame

    def update_status(self):
        self.update_current_frame()
        self._update_current_frame_mini_map_title()
        self._update_current_same_map_score()
        self._update_current_is_same_map()
        self._update_current_mini_map()
        self._find_yellow_point_position_in_mini_map()
        self._find_red_point_position_in_mini_map()

    def _update_current_frame_mini_map_title(self) -> np.ndarray | None:
        if self.status.current_frame is None:
            self.status.current_frame_mini_map_title = None
            return None

        mini_map_title_roi = self.crop_current_frame(self.mini_map_title_region)

        self.status.current_frame_mini_map_title = cv2.cvtColor(
            mini_map_title_roi,  # type: ignore
            cv2.COLOR_RGB2GRAY,
        )
        return self.status.current_frame_mini_map_title

    def _update_current_same_map_score(self) -> float | None:
        if self.status.current_frame_mini_map_title is None or self.mini_map_title is None:
            self.status.current_same_map_score = None
            return None

        score, *_rest = ssim(
            self.mini_map_title, self.status.current_frame_mini_map_title, full=True
        )
        self.status.current_same_map_score = score
        return score

    def _update_current_is_same_map(self) -> bool | None:
        if self.status.current_same_map_score is None:
            self.status.current_is_same_map = None
            return self.status.current_is_same_map

        self.status.current_is_same_map = bool(
            self.status.current_same_map_score > self.ssim_same_map_score_threshold
        )
        return self.status.current_is_same_map

    def _update_current_mini_map(self) -> np.ndarray | None:
        if self.status.current_frame is None:
            self.status.current_frame_mini_map = None
            return None

        self.status.current_frame_mini_map = self.crop_current_frame(
            self.mini_map_region
        )
        return self.status.current_frame_mini_map
    
    def _find_yellow_point_position_in_mini_map(self):
        if self.status.current_frame_mini_map is None:
            self.status.current_yellow_point_position_in_mini_map = None
            return None

        roi = self.status.current_frame_mini_map
        yellow_mask = (
            (roi[:, :, 0] == 255) & (roi[:, :, 1] == 255) & (roi[:, :, 2] < 100)
        )
        y_coords, x_coords = np.where(yellow_mask)

        if len(x_coords) == 0 or len(y_coords) == 0:
            self.status.current_yellow_point_position_in_mini_map = None
            return None

        self.status.current_yellow_point_position_in_mini_map = (
            x_coords[0],
            y_coords[0],
        )
        return self.status.current_yellow_point_position_in_mini_map

    def _find_red_point_position_in_mini_map(self):
        if self.status.current_frame_mini_map is None:
            self.status.current_red_point_position_in_mini_map = None
            return None

        roi = self.status.current_frame_mini_map
        red_mask = (roi[:, :, 0] == 255) & (roi[:, :, 1] == 0) & (roi[:, :, 2] == 0)
        y_coords, x_coords = np.where(red_mask)

        if len(x_coords) == 0 or len(y_coords) == 0:
            self.status.current_red_point_position_in_mini_map = None
            return None

        self.status.current_red_point_position_in_mini_map = (x_coords[0], y_coords[0])
        return self.status.current_red_point_position_in_mini_map

    def _update_current_frame_and_mini_map_title_and_same_map_score(self):
        self.update_current_frame()
        self._update_current_frame_mini_map_title()
        self._update_current_same_map_score()
        self._update_current_is_same_map()

    def _update_current_mini_map_and_yellow_red_point_position(self):
        self._update_current_mini_map()
        self._find_yellow_point_position_in_mini_map()
        self._find_red_point_position_in_mini_map()
