# Network API

Network API is a proof of concept web service built using [FastAPI](https://github.com/tiangolo/fastapi).

Primary goal is to simplify the means of collecting structured data from traditional networking equipment through the use of a consistent RESTful HTTP API.

This is accomplished by leveraging existing libraries like [Netmiko](https://ktbyers.github.io/netmiko/), [NTC Templates](https://github.com/networktocode/ntc-templates), and [PyATS](https://developer.cisco.com/pyats/)

Device connections are established through SSH since most organizations do not enable the built-in APIs of networking equipment.

## Development Installation

```bash
git clone git@github.com:mtbutler07/network_api.git
cd network_api
poetry install
poetry shell
pre-commit install
```

## Development Usage

```bash
poetry shell
uvicorn network_api.main:app --reload
```

Docs are available at
[http://127.0.0.1:8000](http://127.0.0.1:8000)
