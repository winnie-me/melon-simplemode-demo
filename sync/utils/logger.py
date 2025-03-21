import logging
from google.cloud import logging as cloud_logging
import os


class LoggerSingleton:
    """로거 싱글톤 클래스.

    이 클래스는 애플리케이션 전체에서 하나의 로거 인스턴스를 유지합니다.
    """
    _instance = None
    _initialized = False
    _logger = None
    _cloud_logging_client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # 이미 초기화되었으면 아무것도 하지 않음
        if self._initialized:
            return

        # Cloud Logging 클라이언트 초기화
        self._cloud_logging_client = cloud_logging.Client()
        self._cloud_logging_client.setup_logging()

        # 기본 로거 설정
        self._logger = logging.getLogger("cloud_run_job")

        # 로그 레벨은 환경 변수에서 가져오거나 기본값 사용
        log_level_name = os.environ.get("LOG_LEVEL", "INFO")
        log_level = getattr(logging, log_level_name)
        self._logger.setLevel(log_level)

        # 초기화 완료 표시
        self._initialized = True

        # 로거 초기화 로그
        self._logger.info("Logger initialized with level: %s", log_level_name)

    def get_logger(self):
        """설정된 로거 인스턴스를 반환합니다."""
        return self._logger

    def set_log_level(self, level):
        """로그 레벨을 동적으로 변경합니다."""
        # 문자열로 전달된 경우 실제 로그 레벨로 변환
        if isinstance(level, str):
            level = getattr(logging, level.upper())

        self._logger.setLevel(level)
        self._logger.info("Log level changed to %s", logging.getLevelName(level))

    def get_cloud_client(self):
        """Cloud Logging 클라이언트를 반환합니다."""
        return self._cloud_logging_client


# 편의를 위한 함수 - 외부에서 사용할 API
def get_logger():
    """로거 인스턴스를 반환합니다."""
    return LoggerSingleton().get_logger()


def set_log_level(level):
    """로그 레벨을 설정합니다."""
    LoggerSingleton().set_log_level(level)


def get_cloud_logging_client():
    """Cloud Logging 클라이언트를 반환합니다."""
    return LoggerSingleton().get_cloud_client()