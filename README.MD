# NW Automation with NAPALM pack from StackStorm

## Content of the repo:
- This repo contains information on how to implement network automation using NAPALM pack from StackStorm. The objective is to show how to use NAPALM Pack by manualy invoking actions and custom workflows as well as automatically trigger actions/workflows (via rules). The examples are based on two network OSs: Juniper Junos and Arista EOS. 
	- For information, the st2 NAPALM pack is still in experimental state. Anticipate some display issues with some actions (for example different behaviour for same action on two different network OS).

## What is NAPALM?
- [NAPALM](https://napalm.readthedocs.io/en/latest/index.html) stands for Network Automation and Programmability Abstraction Layer with Multivendor support.
- It is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.
- NAPALM supports several methods to connect to the devices, to manipulate configurations or to retrieve data.
- StackStorm includes a NAPALM pack in order to facilitate multi-vendor rnetwork automation.
- You can retrive the pack from [stackstorm-exchange](https://exchange.stackstorm.org/) website or direclty on the [NAPALM pack github repo](https://github.com/StackStorm-Exchange/stackstorm-napalm)

## How to:
- Use stackstorm command to install the pack (includes git clone, install dependencies, registration etc ...):
```
st2 pack install napalm
```
- Edit the ```napalm.yaml``` configuration file, you'll find in this repo the example I used.  
- Follow the instructions on the [Wiki](https://github.com/mab27/st2_napalm/wiki).
