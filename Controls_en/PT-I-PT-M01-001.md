---
Security Function: Protect (PT)
Category: Protective Technology (PT.PT)
Technology: All
Maturity Level: 1
IPAC: Integration (I)
Defender: Technology
Prerequisite:
---

## Description

SAP network implementations should be managed, monitored, and controlled to protect information in applications and systems.

The control involves the need to securely configure the SAP Router and Web Dispatcher to act as an application-level gateways in the DMZ zone.

## Implementation

External traffic:

The SAP router and web dispatcher should be available in the demilitarized (DMZ) zone in order to filter appropriate traffic before being routed through another firewall.  

Internal traffic:

SAP systems should be placed on a separate subnet within the internal network. This allows an easier way to manage network access policies for SAP systems.

Governance:

The architecture of SAP systems should be properly documented which should include but not limited to connections, communications, data flow, users and used protocols.


## Verification of Control

- SAP Router and Web dispatcher placed in DMZ zone
- ACLs are in place to filter unwanted traffic
- Only necessary ports are allowed to access the network.  
- SAP systems are on a separate subnet inside the organization
- Documentation providing an illustrative view of the SAP architecture

## References:
- BSI APP.4.2 SAP-ERP-System, APP.4.2.A3 Network Security/ Netzsicherheit
- CIS CSC 8, 12, 15
- COBIT 5 DSS05.02, APO13.01
- ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR 4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6
- ISO/IEC 27001:2013 A.13.1.1, A.13.2.1, A.14.1.3
- NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18, CP-8, SC-7, SC-19, SC-20, SC-21, SC-22, SC-23, SC-24, SC-25, SC-29, SC-32, SC-36, SC-37, SC- 38, SC-39, SC-40, SC-41, SC-43
