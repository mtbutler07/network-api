# Network API

The Network API is a proof of concept created to simplify the means of collecting structured data from networking equipment through the use of a RESTful HTTP API using [FastAPI](https://github.com/tiangolo/fastapi).

Device connections are established through SSH since most organizations do not enable the built-in APIs of networking equipment. This is accomplished through the asynchronous multi-vendor library [Netdev](https://github.com/selfuryon/netdev).

Raw output is then parsed and structured using the TextFSM templates provided by [NTC Templates](https://github.com/networktocode/ntc-templates)

## Development Installation

```bash
git clone git@github.com:mtbutler07/network_api.git
cd network_api
python3 -m pip install pipenv
python3 -m pipenv install
```

## Development Usage

```bash
python3.8 -m pipenv shell
uvicorn network_api.main:app --reload
```

Docs are available at
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## Resources

This project was made possible using:

- [FastAPI](https://github.com/tiangolo/fastapi)
- [NTC Templates](https://github.com/networktocode/ntc-templates)
- [Netdev](https://github.com/selfuryon/netdev)
