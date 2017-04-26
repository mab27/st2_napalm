[![Build Status](https://travis-ci.org/mab27/st2_vyatta.svg?branch=master)](https://travis-ci.org/mab27/st2_vyatta)

# Auomating Junos with NAPALM pack from StackStorm

## Content of the repo:
- This repo contains information on how to implement network automation suing NAPALM pack from StackStorm.
- [NAPALM](https://napalm.readthedocs.io/en/latest/index.html) stands for Network Automation and Programmability Abstraction Layer with Multivendor support.
- It is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.
- NAPALM supports several methods to connect to the devices, to manipulate configurations or to retrieve data.
- StackStorm includes a NAPALM pack in order to facilitate multi-vendor rnetwork automation.
- You can retrive the pack from [stackstorm-exchange](https://exchange.stackstorm.org/) website or direclty on the [NAPALM pack github repo](https://github.com/StackStorm-Exchange/stackstorm-napalm)

## How to install this pack:
- Show all interfaces:
```
st2 pack install napalm
```
Then  follow the instructions on the README from the repo.

## Getting started with actions of the pack:

- Configuration:

- Validation:

- Device's information:


### Interfaces:
- Show all interfaces:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_interfaces hostname=vmx1
..
id: 58fe01387cae220853c42511
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      .local.:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      cbp0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:05:86:71:08:11
        speed: -1
      demux0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      dsc:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      em1:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:CE
        speed: 1000
      em2:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:D8
        speed: 1000
      em3:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:E2
        speed: 1000
      em4:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:EC
        speed: 1000
      em5:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:F6
        speed: 1000
      em6:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:00
        speed: 1000
      em7:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:0A
        speed: 1000
      em8:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:14
        speed: 1000
      em9:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:1E
        speed: 1000
      fxp0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3411.0
        mac_address: 00:0C:29:88:F0:C4
        speed: 1000
      ge-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:00
        speed: 1000
      ge-0/0/1:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:01
        speed: 1000
      ge-0/0/2:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:02
        speed: 1000
      ge-0/0/3:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:03
        speed: 1000
      ge-0/0/4:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:04
        speed: 1000
      ge-0/0/5:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:05
        speed: 1000
      ge-0/0/6:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:06
        speed: 1000
      ge-0/0/7:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:07
        speed: 1000
      ge-0/0/8:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3370.0
        mac_address: 00:05:86:71:08:08
        speed: 1000
      ge-0/0/9:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 3369.0
        mac_address: 00:05:86:71:08:09
        speed: 1000
      gre:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      ipip:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      irb:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:05:86:71:0B:F0
        speed: -1
      lc-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: 800
      lo0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      lsi:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      mtun:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      pfe-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: 800
      pfh-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: 800
      pimd:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      pime:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      pip0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:05:86:71:0B:B0
        speed: -1
      pp0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      tap:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      vtep:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
  stderr: ''
  stdout: ''
```

- Display IP adressing of all interfaces:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_interfaces hostname=vmx1 ipaddresses=true
..
id: 58fe020d7cae220853c4251a
status: succeeded
parameters: 
  hostname: vmx1
  ipaddresses: true
result: 
  exit_code: 0
  result:
    raw:
      em1.0:
        ipv4:
          172.16.0.1:
            prefix_length: 16
        ipv6:
          fe80::20c:29ff:fe88:f0ce:
            prefix_length: 64
      ge-0/0/0.0:
        ipv4:
          192.168.0.30:
            prefix_length: 24
      ge-0/0/1.0:
        ipv4:
          172.16.0.30:
            prefix_length: 24
      lo0.16384:
        ipv4:
          127.0.0.1:
            prefix_length: 32
      lo0.16385:
        ipv4:
          128.0.0.1:
            prefix_length: 32
          128.0.0.4:
            prefix_length: 32
        ipv6:
          fe80::20c:290f:fc88:f0c4:
            prefix_length: 128
  stderr: ''
  stdout: ''
```

- Show one specific interface:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_interfaces hostname=vmx1 interface=ge-0/0/1
..
id: 58fe01c37cae220853c42514
status: succeeded
parameters: 
  hostname: vmx1
  interface: ge-0/0/1
result: 
  exit_code: 0
  result:
    raw:
      description: ''
      is_enabled: true
      is_up: true
      last_flapped: 3509.0
      mac_address: 00:05:86:71:08:01
      name: ge-0/0/1
      speed: 1000
  stderr: ''
  stdout: ''
```

- Show the counters for one specific interface:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_interfaces hostname=vmx1 interface=ge-0/0/1 counters=true
..
id: 58fe01da7cae220853c42517
status: succeeded
parameters: 
  counters: true
  hostname: vmx1
  interface: ge-0/0/1
result: 
  exit_code: 0
  result:
    raw:
      name: ge-0/0/1
      rx_broadcast_packets: 0
      rx_discards: 0
      rx_errors: 0
      rx_multicast_packets: 0
      rx_octets: 604
      rx_unicast_packets: 0
      tx_broadcast_packets: 0
      tx_discards: 0
      tx_errors: 0
      tx_multicast_packets: 0
      tx_octets: 11568
      tx_unicast_packets: 0
  stderr: ''
  stdout: ''
```

- Show the ARP table:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_arp_table hostname=vmx1
..
id: 58fe03637cae220853c4251d
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
    - age: 806.0
      interface: ge-0/0/0.0
      ip: 192.168.0.10
      mac: 00:0C:29:8F:3E:11
    - age: 709.0
      interface: ge-0/0/0.0
      ip: 192.168.0.120
      mac: 00:0C:29:BF:23:31
  stderr: ''
  stdout: ''
```

- Show the LLDP neighbors:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_lldp_neighbors hostname=vmx1
..
id: 58ff7a777cae22077ffd0cdb
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      ge-0/0/0:
      - hostname: localhost
        port: 00:0c:29:8f:3e:11
      ge-0/0/1:
      - hostname: localhost
        port: 00:0c:29:8f:3e:1b
  stderr: ''
  stdout: ''
```


### Configuration & facts:
- Show the running configuration on a device:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_config hostname=vmx1
.
id: 58fe040d7cae220853c42520
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      candidate: "
## Last changed: 2017-04-24 13:47:22 UTC
version 14.1R4.9;
system {
    root-authentication {
        encrypted-password "$1$gjKQdWCJ$dYlWeP6CI2eWBCt4Dz.hH0";
    }
    login {
        user mab {
            uid 2000;
            class super-user;
            authentication {
                encrypted-password "$1$56iSMRiJ$l4F0kQnMFk2SeALRTmWz30";
            }
        }
    }
    services {
        ssh {
            root-login allow;
        }
        netconf {
            ssh;
            traceoptions {
                file netconf;
                flag all;
            }
        }
    }
    syslog {
        user * {
            any emergency;
        }
        file messages {
            any notice;
            authorization info;
        }
        file interactive-commands {
            interactive-commands any;
        }
    }
}
interfaces {
    ge-0/0/0 {
        unit 0 {
            family inet {
                address 192.168.0.30/24;
            }
        }
    }
    ge-0/0/1 {
        unit 0 {
            family inet {
                address 172.16.0.30/24;
            }
        }
    }
}
routing-options {
    forwarding-table {
        export bgp-ecmp;
    }
}
protocols {
    bgp {
        group underlay {
            type external;
            import bgp-in;
            export bgp-out;
            local-as 101;
            multipath multiple-as;
            neighbor 172.16.0.40 {
                peer-as 102;
            }
        }
    }
}
policy-options {
    policy-statement bgp-ecmp {
        then {
            load-balance per-packet;
        }
    }
    policy-statement bgp-in {
        then accept;
    }
    policy-statement bgp-out {
        then accept;
    }
}
"
      running: "
## Last changed: 2017-04-24 13:47:22 UTC
version 14.1R4.9;
system {
    root-authentication {
        encrypted-password "$1$gjKQdWCJ$dYlWeP6CI2eWBCt4Dz.hH0";
    }
    login {
        user mab {
            uid 2000;
            class super-user;
            authentication {
                encrypted-password "$1$56iSMRiJ$l4F0kQnMFk2SeALRTmWz30";
            }
        }
    }
    services {
        ssh {
            root-login allow;
        }
        netconf {
            ssh;
            traceoptions {
                file netconf;
                flag all;
            }
        }
    }
    syslog {
        user * {
            any emergency;
        }
        file messages {
            any notice;
            authorization info;
        }
        file interactive-commands {
            interactive-commands any;
        }
    }
}
interfaces {
    ge-0/0/0 {
        unit 0 {
            family inet {
                address 192.168.0.30/24;
            }
        }
    }
    ge-0/0/1 {
        unit 0 {
            family inet {
                address 172.16.0.30/24;
            }
        }
    }
}
routing-options {
    forwarding-table {
        export bgp-ecmp;
    }
}
protocols {
    bgp {
        group underlay {
            type external;
            import bgp-in;
            export bgp-out;
            local-as 101;
            multipath multiple-as;
            neighbor 172.16.0.40 {
                peer-as 102;
            }
        }
    }
}
policy-options {
    policy-statement bgp-ecmp {
        then {
            load-balance per-packet;
        }
    }
    policy-statement bgp-in {
        then accept;
    }
    policy-statement bgp-out {
        then accept;
    }
}
"
      startup: ''
  stderr: ''
  stdout: ''
```

- Perform a configuration consitency check (compare actual config to a golden config stored on a github repo):
```
mab@mab-infra:/opt/stackstorm/packs/napalm$ sudo st2 run napalm.check_consistency hostname=vmx1
...
id: 58fe14f27cae220853c42541
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    deviation: true
    diff_contents: "--- 
+++ 
@@ -1,13 +1,16 @@
+
 version 14.1R4.9;
 system {
     root-authentication {
-        encrypted-password "$1$gjKQdWCJ$dYlWeP6CI2eWBCt4Dz.hH0";     }
+        encrypted-password "$1$gjKQdWCJ$dYlWeP6CI2eWBCt4Dz.hH0";
+    }
     login {
         user mab {
             uid 2000;
             class super-user;
             authentication {
-                encrypted-password "$1$56iSMRiJ$l4F0kQnMFk2SeALRTmWz30";             }
+                encrypted-password "$1$56iSMRiJ$l4F0kQnMFk2SeALRTmWz30";
+            }
         }
     }
     services {
@@ -52,7 +55,7 @@
     }
 }
 routing-options {
-    forwarding-table {                  
+    forwarding-table {
         export bgp-ecmp;
     }
 }
@@ -82,4 +85,4 @@
     policy-statement bgp-out {
         then accept;
     }
-}+}
"
  stderr: ''
  stdout: ''
```

```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.check_consistency hostname=vmx1
..
id: 58fe20607cae220853c42565
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    deviation: true
    diff_contents: "--- 
+++ 
@@ -1,3 +1,4 @@
+
 version 14.1R4.9;
 system {
     root-authentication {
"
  stderr: ''
  stdout: ''
```

- Get the facts from on a device:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.get_facts hostname=vmx1
..
id: 58fe04627cae220853c42523
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      fqdn: ''
      hostname: ''
      interface_list:
      - ge-0/0/0
      - lc-0/0/0
      - pfe-0/0/0
      - pfh-0/0/0
      - ge-0/0/1
      - ge-0/0/2
      - ge-0/0/3
      - ge-0/0/4
      - ge-0/0/5
      - ge-0/0/6
      - ge-0/0/7
      - ge-0/0/8
      - ge-0/0/9
      - .local.
      - cbp0
      - demux0
      - dsc
      - em1
      - em2
      - em3
      - em4
      - em5
      - em6
      - em7
      - em8
      - em9
      - fxp0
      - gre
      - ipip
      - irb
      - lo0
      - lsi
      - mtun
      - pimd
      - pime
      - pip0
      - pp0
      - tap
      - vtep
      model: VMX
      os_version: 14.1R4.9
      serial_number: VM55E771B3CD
      uptime: 4260
      vendor: Juniper
  stderr: ''
  stdout: ''
```

### Connectivity:
- Perform a ping (to a specified destimation) on a device:
```
mab@mab-infra:~/automation/st2_napalm_junos$ sudo st2 run napalm.ping hostname=vmx1 destination=192.168.0.10
...
id: 58fe04d17cae220853c42526
status: succeeded
parameters: 
  destination: 192.168.0.10
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      success:
        packet_loss: 0
        probes_sent: 5
        results:
        - ip_address: 192.168.0.10
          rtt: 3.306
        - ip_address: 192.168.0.10
          rtt: 2.009
        - ip_address: 192.168.0.10
          rtt: 2.513
        - ip_address: 192.168.0.10
          rtt: 1.941
        - ip_address: 192.168.0.10
          rtt: 1.292
        rtt_avg: 2.212
        rtt_max: 3.306
        rtt_min: 1.292
        rtt_stddev: 0.67
  stderr: ''
  stdout: ''
```

- Obtain the BGP neighbors for a device:
```
mab@mab-infra:/opt/stackstorm/packs/napalm$ sudo st2 run napalm.get_bgp_neighbors hostname=vmx1 
..
id: 58fe19117cae220853c42547
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      172.16.0.40:
        address_family: {}
        description: ''
        is_enabled: true
        is_up: false
        local_as: 101
        remote_as: 102
        remote_id: ''
        uptime: 9520
  stderr: ''
  stdout: ''
```

- Get the route for a specific destination: 
```

```


## Webhooks: 

### What are Webhooks: 
- Systems that push data to the ST2 API when an event you are interested in occurs.
- Webhooks come handy is when you want to consume events from a 3rd party service which already offer webhooks integration - e.g. GitHub
- Webhooks aren't directly created --> they're created via rules.

The rules in this pack are written using one of the default triggers: ```core.st2.webhook``` --> This means that the rule will be watching for incoming events that are in the form of a custom webhook.

POST-ing data to a custom webhook will cause a trigger with the following attributes to be dispatched:
- **trigger** - Trigger name.
- **trigger.headers** - Dictionary containing the request headers.
- **trigger.body** - Dictionary containing the request body.

These allows the rule to check if the event matches any of its criteria, if yes, then the corresponding action/workflow will be fired.

### Pre-requisistes (Before trying rules):
- Make sure the rules are registered and available by list the available rules for the pack:
```
mab@mab-infra:/opt/stackstorm/packs/napalm/rules$ sudo st2 rule list -p napalm
+-----------------------------+--------+-----------------------------------+---------+
| ref                         | pack   | description                       | enabled |
+-----------------------------+--------+-----------------------------------+---------+
| napalm.bgp_prefix_exceeded  | napalm | Webhook which handles a BGP       | True    |
|                             |        | neighbour exceeding it's prefix   |         |
|                             |        | limit                             |         |
| napalm.configuration_change | napalm | Webhook which handles when a      | True    |
|                             |        | device has been configured and    |         |
|                             |        | changes commited                  |         |
| napalm.interface_down       | napalm | Webhook which handles an          | True    |
|                             |        | interface going down on a network |         |
|                             |        | device.                           |         |
+-----------------------------+--------+-----------------------------------+---------+
```
- If needed, restart the rules service:
```
sudo st2ctl restart --register-rules
```
- Obtain an authentication token. You'll need it to replace **$TOKEN** in the cURL commands below:
```
st2 auth login -p password
```

### Usefull commands to verify rules enforcement and actions/workflows executions:
- Check the latest rules enforced:
```
st2 rule-enforcement list -n 5
```
- Check the details of the emitted trigger  (obtain **trigger_id** from previous command):
```
st2 trigger-instance get **trigger_id**
```
- Check the latest actions/workflows executed:
```
st2 execution list -n 5
```

### Examples:

- Trigger the **bgp_prefix_exceeded** rule: send the call via cURL command:
```
curl -k -H "Content-Type:application/json" -H "X-Auth-Token:$TOKEN" -d '{"logsource":"vmx1","message":"BGP-EXCEED-LIMIT","neighbour":"192.168.0.40","asnum":"102","prefixes":"50"}' http://localhost:9101/v1/webhooks/napalm_bgp_prefix_exceeded
```
- Check if the rule has been enforced:
```
mab@mab-infra:/opt/stackstorm/packs/napalm/rules$ sudo st2 rule-enforcement list -n 5+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| id                       | rule.ref              | trigger_instance_id   | execution_id          | enforced_at           |
+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| 5900dbc37cae22046eaac323 | vyatta.webhook_cfg_ip | 5900dbc27cae22046eaac | 5900dbc37cae22046eaac | Wed, 26 Apr 2017      |
|                          | _route                | 31f                   | 322                   | 17:41:23 UTC          |
| 5900dbc97cae22046eaac330 | vyatta.webhook_cfg_ip | 5900dbc97cae22046eaac | 5900dbc97cae22046eaac | Wed, 26 Apr 2017      |
|                          | _route                | 32c                   | 32f                   | 17:41:29 UTC          |
| 5900dbcf7cae22046eaac33d | vyatta.webhook_cfg_ip | 5900dbcf7cae22046eaac | 5900dbcf7cae22046eaac | Wed, 26 Apr 2017      |
|                          | _route                | 335                   | 339                   | 17:41:35 UTC          |
| 5900dbd57cae22046eaac34a | vyatta.webhook_cfg_ip | 5900dbd57cae22046eaac | 5900dbd57cae22046eaac | Wed, 26 Apr 2017      |
|                          | _route                | 342                   | 347                   | 17:41:41 UTC          |
| 5900dc8e7cae22046eaac357 | napalm.bgp_prefix_exc | 5900dc8e7cae22046eaac | 5900dc8e7cae22046eaac | Wed, 26 Apr 2017      |
|                          | eeded                 | 353                   | 356                   | 17:44:46 UTC          |
+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
```

- Check the details of the trigger:
```
mab@mab-infra:/opt/stackstorm/packs/napalm/rules$ sudo st2 trigger-instance get 5900dc8e7cae22046eaac353
+-----------------+--------------------------------------------------------------+
| Property        | Value                                                        |
+-----------------+--------------------------------------------------------------+
| id              | 5900dc8e7cae22046eaac353                                     |
| trigger         | core.f36458c4-f95e-4d17-8efd-9437ae8c5abe                    |
| occurrence_time | 2017-04-26T17:44:46.386000Z                                  |
| payload         | {                                                            |
|                 |     "body": {                                                |
|                 |         "neighbour": "192.168.0.40",                         |
|                 |         "prefixes": "50",                                    |
|                 |         "message": "BGP-EXCEED-LIMIT",                       |
|                 |         "logsource": "vmx1",                                 |
|                 |         "asnum": "102"                                       |
|                 |     },                                                       |
|                 |     "headers": {                                             |
|                 |         "Content-Length": "106",                             |
|                 |         "X-Request-Id":                                      |
|                 | "b2b9af8c-d459-4169-8a32-eed44df8531c",                      |
|                 |         "Accept": "*/*",                                     |
|                 |         "X-Auth-Token": "$TOKEN",  |
|                 |         "Host": "localhost:9101",                            |
|                 |         "User-Agent": "curl/7.47.0",                         |
|                 |         "Content-Type": "application/json"                   |
|                 |     }                                                        |
|                 | }                                                            |
| status          | processed                                                    |
+-----------------+--------------------------------------------------------------+
```

- Check the details of the action/workflow execution resulted from this trigger (action is failing in this example, but the purpose is to show action firing and arguments passing from webhook to action:
```
sudo st2 execution get 5900dc8e7cae22046eaac356
id: 5900dc8e7cae22046eaac356
action.ref: napalm.bgp_prefix_exceeded_chain
parameters: 
  asnum: '102'
  hostname: vmx1
  message: BGP-EXCEED-LIMIT
  neighbour: 192.168.0.40
  prefixes: 50
status: failed (0s elapsed)
start_timestamp: 2017-04-26T17:44:46.476967Z
end_timestamp: 2017-04-26T17:44:46.806902Z
result: 
  error: Unable to find node with name "show_bgp_neighbours" referenced in "default".
  traceback: "  File "/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2actions/container/base.py", line 90, in _do_run
    runner.pre_run()
  File "/opt/stackstorm/runners/action_chain_runner/action_chain_runner.py", line 279, in pre_run
    raise runnerexceptions.ActionRunnerPreRunError(e.message)
"
```
