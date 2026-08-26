---
slug: networking-dns
---

## Definition

**DNS** (Domain Name System) is a distributed naming service that translates human-readable domain names into the [[IP Address|IP addresses]] computers use to reach hosts on a network.

## Description

People remember names like `travelbody.com` more easily than numeric addresses. DNS bridges that gap: when you type a domain in a browser, a DNS resolver looks up the corresponding IP address so your device knows where to connect.

**Typical lookup flow:**

1. Browser requests `travelbody.com`
2. DNS resolver queries authoritative or cached records
3. Resolver returns an IP address (e.g. `203.0.113.42`)
4. The client opens a connection to that IP (often on a specific port)

DNS is hierarchical. Root servers, TLD servers, and authoritative name servers cooperate to answer queries. Results are often cached at the OS, browser, or ISP level to reduce latency.

Without DNS, users would need to memorize IP addresses for every website and service they use.
