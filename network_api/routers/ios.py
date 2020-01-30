from fastapi import APIRouter

from network_api import ssh

router = APIRouter()

DEVICE_TYPE: str = "cisco_ios"


@router.get("/{host}/version")
async def device_version(host: str):
    command: str = "show version"
    return await ssh.device_cli(host=host, device_type=DEVICE_TYPE, command=command)


@router.get("/{host}/interface")
async def device_interface(host: str):
    command: str = "show interfaces"
    return await ssh.device_cli(host=host, device_type=DEVICE_TYPE, command=command)


@router.get("/{host}/vlan")
async def device_vlan(host: str):
    command: str = "show vlan"
    return await ssh.device_cli(host=host, device_type=DEVICE_TYPE, command=command)
