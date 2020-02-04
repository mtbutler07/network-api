import asyncio
from os import environ

import netdev
from ntc_templates.parse import parse_output


async def device_cli(host: str, device_type: str, commands: list) -> dict:

    params = {
        "host": host,
        "device_type": device_type,
        "username": environ.get("USERNAME"),
        "password": environ.get("PASSWORD"),
    }

    async with netdev.create(**params) as device:

        results = dict()

        for command in commands:

            data = await device.send_command(command)
            results[command] = parse_output(platform=device_type, command=command, data=data)

        return results

