from enum import Enum


class DeviceTypes(str, Enum):
    ios = "cisco_ios"


class CLIParserTypes(str, Enum):
    genie = "genie"
