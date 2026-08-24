---
slug:
---

## Definition

A **subnet** is a contiguous range of [[IP Address|IP addresses]] within a larger network, defined by a network prefix and mask, so devices in the same subnet can reach each other locally while traffic to other subnets is forwarded by a router.

## Description

A subnet carves one big address space into smaller, manageable blocks. Each block gets a **network address** (the subnet itself) and a set of assignable **host addresses** for devices.

**CIDR notation** expresses this compactly: `10.0.1.0/24` means the first 24 bits are fixed as the network portion and the remaining 8 bits identify hosts.

| Notation | Subnet mask (IPv4) | Usable host addresses (typical) |
|----------|-------------------|-----------------------------------|
| `/24` | `255.255.255.0` | 254 |
| `/16` | `255.255.0.0` | 65,534 |
| `/8` | `255.0.0.0` | ~16.7 million |

**Example — one `/16` split into `/24` subnets:**

```text
10.0.0.0/16   (parent network)
  10.0.1.0/24   (subnet A — e.g. web tier)
  10.0.2.0/24   (subnet B — e.g. app tier)
  10.0.3.0/24   (subnet C — e.g. database tier)
```

Devices on `10.0.1.10` and `10.0.1.50` are on the same subnet: they can communicate directly at Layer 2 (same broadcast domain). A device on `10.0.2.15` is on a different subnet; reaching it requires a **default gateway** (usually a router interface on each subnet, e.g. `10.0.1.1`).

In cloud and data-center design, subnets are often tagged **public** (routes to the internet via an internet gateway) or **private** (no direct inbound internet route). That layout supports network segmentation: related workloads share a subnet, and policy controls what may cross subnet boundaries.

**Tradeoff:** smaller subnets conserve address space per segment but limit how many hosts each tier can hold; larger subnets fit more hosts but widen the broadcast domain and blast radius.
