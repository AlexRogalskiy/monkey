import logging
from typing import Optional

from infection_monkey.i_puppet import UnknownPluginError
from infection_monkey.puppet.plugin_type import PluginType

logger = logging.getLogger()


class PluginRegistry:
    def __init__(self):
        """
        `self._registry` looks like -
            {
                PluginType.EXPLOITER: {
                    "ZerologonExploiter": ZerologonExploiter,
                    "SMBExploiter": SMBExploiter
                },
                PluginType.PBA: {
                    "CommunicateAsBackdoorUser": CommunicateAsBackdoorUser
                }
            }
        """
        self._registry = {}

    def load_plugin(self, plugin: object, plugin_type: PluginType) -> None:
        self._registry.setdefault(plugin_type, {})
        self._registry[plugin_type][plugin.__class__.__name__] = plugin

        logger.debug(f"Plugin '{plugin.__class__.__name__}' loaded")

    def get_plugin(self, plugin_name: str, plugin_type: PluginType) -> Optional[object]:
        try:
            plugin = self._registry[plugin_type][plugin_name]
        except KeyError:
            raise UnknownPluginError(
                f"Unknown plugin '{plugin_name}' of type '{plugin_type.value}'"
            )

        logger.debug(f"Plugin '{plugin_name}' found")

        return plugin
