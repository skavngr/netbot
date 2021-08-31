# NetBot
A versatile command and control center (CCC) for DDoS Botnet Attack Simulation &amp; Load Generation.

**Disclaimer**
---

_The use of this software and scripts downloaded on this repository is done at your own discretion and risk and with agreement that you will be solely responsible for any damage to your or other computer system or availability disruption that results from such activities. You are solely responsible for the usage in connection with any of the software, and the author will not be liable for any damages that you may suffer or incur availability disruption on other systems in connection with using, modifying or distributing any of this software. No advice or information, whether oral or written, obtained by you from the author or from this website shall create any warranty for the software._

What is _NetBot_?
--
- Proof-of-Concept code that simulates a Client-Server botnet environment.
- Easily helps setting up a botnet chain that reports to your CCC.
- Assists in simulating DDoS attacks towards the target. (_Experimental/Research Usage Only_)

Requirements
--
- Python 3

Supports
--
- Tested on Debian, Ubuntu, CentOS and MacOS High Sierra.

FYI - *Prototype Warning*
--
- This is simply a prototype code and may not fully work up to your expectations. Feel free to fork the project and modify it to meet your needs. 
- Currently working on making it more robust execution, look and feel features.
- (_under development_) more attack vectors and variants. (_as of now supports HTTP Flooding & Ping Flood only._)


Source Code
--
- _netbot_server.py_ : This is the actual CCC Server. 
- _netbot_config.py_ : CCC loads the information about the targets to attack. 
- _netbot_client.py_ : This is the client code (bots).

How do I setup/test _NetBot_?
--
- You can test this software in a single machine itself, but the ultimate point of this software to deploy the client (bots) on different machines and the server code (CCC) on your machine.
  - **very important** Make sure you modify the CCC server address on the _netbot_client.py_ code, else the bots will not connect to your CCC.
- More to be added in Wiki section soon.



NetBot CCC Server
--
![netbot intro](https://raw.githubusercontent.com/skavngr/netbot/main/netbot_server.PNG)
