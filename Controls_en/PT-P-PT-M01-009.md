---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: SAP ABAP  
Maturity Level: 1
IPAC: Platform (P)
Defender: Technology
Prerequisite:
---

## Description

Securing malicious or unrecognized access to the application servers through the message server is critical to maintaining the integrity, availability, and confidentiality of different requests between application servers of an SAP system working as a cluster.

Applicable for ABAP and Java systems.

## Implementation

A network device acting as a rogue application servers can pose a high risk to the organization if communication is allowed to legitimate application servers.

Access control lists (ACLs) must be configured for the message server to contain and defend against attacks on the trust relationship between legitimate application servers.

- ACL file should not contain an entry for to allow all hosts (i.e. HOST=* is critical)
- Split ports on message server for internal (1) and external communication (2)
- Profile parameter rdisp/msserv_internal defines the internal ports to use
- Block communication from external to the port defined in profile parameter rdisp/msserv_internal
- Deny external monitoring of the message server though setting the profile parameter ms/monitor=0
- Deny external administration of the message server though setting the profile parameter ms/admin_port=0

(1) - Internal communication is for communication between different application serves in the organization

(2) - External communication is for communication with the users/clients

## Verification of Control

- Verify the ACLs for the message server fro the profile parameter ms/acl_info
- Verify that HOST=* is not defined in the ACL
- Verify that ports are split for internal and external traffic and that the firewall is blocking communication to the internal port for all hosts not belonging to the system cluster.
- Verify that profile parameter ms/monitor=0
- Verify that profile parameter ms/admin_port=0

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A9 Protection and monitoring of the message server (B) / Absicherung und Überwachung des Message-Servers (B)
- SAP Security Baseline Template V2.1: 2.2.1.4, 2.2.1.4.1, 2.2.1.4.2
