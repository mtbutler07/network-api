from os import environ

from netmiko import ConnectHandler

from network_api.models import DeviceTypes


def device_cli(
    host: str,
    device_type: DeviceTypes,
    command: str,
    username: str = environ.get("SSH_USER"),
    password: str = environ.get("SSH_PASS"),
    use_genie: bool = False,
) -> dict:

    with ConnectHandler(
        host=host,
        device_type=device_type,
        username=username,
        password=password,
    ) as conn:

        results = conn.send_command(
            command,
            use_genie=use_genie,
        )

    return results
