from fastapi import APIRouter

from network_api import ssh

router = APIRouter()

DEVICE_TYPE: str = "cisco_ios"


@router.get("/{host}/version")
async def device_version(host: str):
    commands: list = ["show version"]
    return await ssh.device_cli(host=host, device_type=DEVICE_TYPE, commands=commands)


@router.get("/{host}/interface")
async def device_interface(host: str):
    commands: list = ["show interfaces"]
    return await ssh.device_cli(host=host, device_type=DEVICE_TYPE, commands=commands)


@router.get("/{host}/vlan")
async def device_vlan(host: str):
    commands: list = ["show vlan"]
    return await ssh.device_cli(host=host, device_type=DEVICE_TYPE, commands=commands)
