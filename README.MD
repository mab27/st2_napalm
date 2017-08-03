# NW Automation with NAPALM pack from StackStorm

## Content of the repo:
- This repo contains information on how to implement network automation using NAPALM pack from StackStorm.
- [NAPALM](https://napalm.readthedocs.io/en/latest/index.html) stands for Network Automation and Programmability Abstraction Layer with Multivendor support.
- It is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.
- NAPALM supports several methods to connect to the devices, to manipulate configurations or to retrieve data.
- StackStorm includes a NAPALM pack in order to facilitate multi-vendor rnetwork automation.
- You can retrive the pack from [stackstorm-exchange](https://exchange.stackstorm.org/) website or direclty on the [NAPALM pack github repo](https://github.com/StackStorm-Exchange/stackstorm-napalm)

## How to install this pack:
- Use stackstorm command to install the pack (includes git clone, install dependencies, registration etc ...):
```
st2 pack install napalm
```
Then  follow the instructions on the Wiki from the repo.
