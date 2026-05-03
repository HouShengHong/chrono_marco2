import threading
import logging
from typing import Callable

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


class AlertMonitor:
    def __init__(
        self,
        check_func: Callable[..., bool],  # 回傳布林值：True 代表異常
        on_alert: Callable[..., None],  # 觸發告警時要執行的函數
        interval: int = 5,
        name: str = "Monitor",
        check_args: tuple = (),  # check_func 的位置參數
        check_kwargs: dict | None = None,  # check_func 的關鍵字參數
        alert_args: tuple = (),  # on_alert 的位置參數
        alert_kwargs: dict | None = None,  # on_alert 的關鍵字參數
    ) -> None:
        self.check_func = check_func
        self.on_alert = on_alert
        self.interval = interval
        self.name = name

        # 參數處理
        self.check_args = check_args
        self.check_kwargs = check_kwargs or {}
        self.alert_args = alert_args
        self.alert_kwargs = alert_kwargs or {}

        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None

    def _run(self) -> None:
        logging.info(f"[{self.name}] 監控已啟動")
        while not self._stop_event.is_set():
            try:
                # 執行檢查，看是否發生異常
                is_triggered = self.check_func(*self.check_args, **self.check_kwargs)

                if is_triggered:
                    logging.warning(f"⚠️  [{self.name}] 偵測到異常！執行告警動作...")
                    self.on_alert(*self.alert_args, **self.alert_kwargs)
                else:
                    # logging.info(f"[{self.name}] 狀態正常")
                    pass

            except Exception as e:
                logging.error(f"[{self.name}] 運作中斷: {e}")

            self._stop_event.wait(self.interval)

    def start(self) -> None:
        if self._thread is None or not self._thread.is_alive():
            self._stop_event.clear()
            self._thread = threading.Thread(target=self._run, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        if self._thread:
            self._stop_event.set()
            self._thread.join()
