# NW Automation with NAPALM pack from StackStorm

## Content of the repo:
- This repo shows how to implement network automation using NAPALM pack from StackStorm. The objective is to illustrate how to implement network automation in a multi-vendor network.
- As of now, the repo is focusing on one use-case (implementing an eBGP peering) and two network vendors (Arista and Juniper). Both the number of use-cases as well as the type of vendors can be expanded. The later is limited to a list of supported vendors by NAPALM, see NAPALM section below.
- Some workflows in this repo uses information in the [network_iac repo](https://github.com/mab27/network_iac).
- Nota:
	- The st2 NAPALM pack is still in **experimental state**. Anticipate some display issues with some actions (for example different behavior for same action on two different network OS).
	- The workflows have been written and tested against virtual appliances: Arista vEOS and Juniper vMX. For Juniper, expect some slight differences between vMX and other Juniper devices (like vSRX and vQFX).

## What is NAPALM?
- [NAPALM](https://napalm.readthedocs.io/en/latest/index.html) stands for Network Automation and Programmability Abstraction Layer with Multivendor support.
- It is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.
- NAPALM supports several methods to connect to the devices, to manipulate configurations or to retrieve data.
- StackStorm includes a NAPALM pack in order to facilitate multi-vendor rnetwork automation.
- You can retrive the pack from [stackstorm-exchange](https://exchange.stackstorm.org/) website or direclty on the [NAPALM pack github repo](https://github.com/StackStorm-Exchange/stackstorm-napalm)

## How to (in order):
- Use stackstorm command to install the pack (includes git clone, install dependencies, registration etc ...):
```
st2 pack install napalm
```
- Edit the ```napalm.yaml``` configuration file, you'll find in this repo the [example I used](https://github.com/mab27/st2_napalm/blob/master/napalm.yaml).
	- A reload of the config is required upon each modificatiton to that file. To do that you can either use the ```st2ctl``` command: ```sudo st2ctl reload --register-configs``` or the use the pack register feature: ```st2 pack register napalm```.
- Copy the content of ```my_pack``` folder in ```/opt/stacksotrm/packs/default/``` and register the content.
- Read the [Wiki](https://github.com/mab27/st2_napalm/wiki) to understand the content and follow the instructions to reproduce the tests.
