from typing import Optional

from fastapi import APIRouter

from network_api import ssh
from network_api.models import CLIParserTypes, DeviceTypes

router = APIRouter()


@router.get("/version")
async def device_version(
    host: str, device_type: DeviceTypes, parser: Optional[CLIParserTypes] = None
):
    command = "show version"
    params = {"host": host, "device_type": device_type, "command": command}

    if parser and parser.value == "genie":
        params["use_genie"] = True

    response = ssh.device_cli(**params)
    return response


@router.get("/interface")
async def device_interface(
    host: str, device_type: DeviceTypes, parser: Optional[CLIParserTypes] = None
):
    command = "show interfaces"
    params = {"host": host, "device_type": device_type, "command": command}

    if parser and parser.value == "genie":
        params["use_genie"] = True

    response = ssh.device_cli(**params)
    return response


@router.get("/vlan")
async def device_vlan(
    host: str, device_type: DeviceTypes, parser: Optional[CLIParserTypes] = None
):
    command = "show vlan"
    params = {"host": host, "device_type": device_type, "command": command}

    if parser and parser.value == "genie":
        params["use_genie"] = True

    response = ssh.device_cli(**params)
    return response
