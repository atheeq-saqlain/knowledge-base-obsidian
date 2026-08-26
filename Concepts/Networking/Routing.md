---
slug: networking-routing
---

## Definition

**Routing** is the process of selecting paths and forwarding data packets between networks or [[Network Segmentation and Subnets|subnets]] so traffic reaches its destination [[IP Address]].

## Description

When source and destination devices are not on the same local network, routers examine each packet's destination IP and decide the next hop toward that address. Routing tables — built manually or learned via protocols like BGP and OSPF — encode those decisions.

**Simplified path:**

```text
Laptop (192.168.1.5)
  → home router
  → ISP router
  → internet backbone
  → destination server (203.0.113.42)
```

Routers operate at Layer 3. They do not terminate application connections themselves; they forward packets based on network topology and policy.

Routing connects segmented networks: traffic from a public web subnet may be routed into a private application subnet, subject to firewall rules. Without routing, isolated subnets could not communicate even when policy allows it.
