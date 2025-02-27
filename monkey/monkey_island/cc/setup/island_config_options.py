from __future__ import annotations

from common.utils.file_utils import expand_path
from monkey_island.cc.server_utils.consts import (
    DEFAULT_CERTIFICATE_PATHS,
    DEFAULT_CRT_PATH,
    DEFAULT_DATA_DIR,
    DEFAULT_KEY_PATH,
    DEFAULT_LOG_LEVEL,
    DEFAULT_START_MONGO_DB,
)

_DATA_DIR = "data_dir"
_SSL_CERT = "ssl_certificate"
_SSL_CERT_FILE = "ssl_certificate_file"
_SSL_CERT_KEY = "ssl_certificate_key_file"
_MONGODB = "mongodb"
_START_MONGODB = "start_mongodb"
_LOG_LEVEL = "log_level"


class IslandConfigOptions:
    def __init__(self, config_contents: dict = None):
        if not config_contents:
            config_contents = {}
        self.data_dir = config_contents.get(_DATA_DIR, DEFAULT_DATA_DIR)

        self.log_level = config_contents.get(_LOG_LEVEL, DEFAULT_LOG_LEVEL)

        self.start_mongodb = config_contents.get(
            _MONGODB, {_START_MONGODB: DEFAULT_START_MONGO_DB}
        ).get(_START_MONGODB, DEFAULT_START_MONGO_DB)

        self.crt_path = config_contents.get(_SSL_CERT, DEFAULT_CERTIFICATE_PATHS).get(
            _SSL_CERT_FILE, DEFAULT_CRT_PATH
        )
        self.key_path = config_contents.get(_SSL_CERT, DEFAULT_CERTIFICATE_PATHS).get(
            _SSL_CERT_KEY, DEFAULT_KEY_PATH
        )

        self._expand_paths()

    def _expand_paths(self):
        self.data_dir = expand_path(str(self.data_dir))
        self.crt_path = expand_path(str(self.crt_path))
        self.key_path = expand_path(str(self.key_path))

    def update(self, target: dict):
        self.__dict__.update(target)
        self._expand_paths()
