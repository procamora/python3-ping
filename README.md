# python3-ping


This library provides an easy way to ping using the _ping_ command provided by the operating system. The reason for using the operating system command is so that you do not need to be root to send an ICMP packet.


# Installation

Installation can be done through the _pip3_ command:



```bash
pip3 install procamora-ping --user
```


You can also update the library with:



```bash
python3 -m pip install --user --upgrade procamora-ping
```



# Basic Usage


To use this class the first thing to do is import the library:


```python
from procamora_ping.logger import get_logger, logging
from procamora_ping.ping import ping
```




```python
ips: List[Text] = ["192.168.1.1", "192.168.1.11", "192.168.1.56"]

for ip in ips:
    texto: bool = ping(ip)
    if texto:
        logger.info("{} up".format(ip))
    else:
        logger.info("{} down".format(ip))
```



