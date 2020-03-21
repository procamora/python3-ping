#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import platform
import subprocess
from typing import NoReturn, Text, List

from procamora_logging.logger import get_logging

logger: logging = get_logging(False, 'ping')


def ping(hostname: Text) -> bool:
    # Posibles opciones: 'Linux', 'Darwin', 'Java', 'Windows'
    command: Text
    if platform.uname()[0] == 'Linux':
        command = f'ping -c 1 {hostname}'
    elif platform.uname()[0] == 'Windows':
        command = f'ping -n 1 {hostname}'
    else:
        logger.error(f'{platform.uname()[0]} operating system temporarily not supported')
        raise OSError(f'{platform.uname()[0]} operating system temporarily not supported')

    logger.debug(command)

    a: subprocess.CompletedProcess = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 0 -> Ejecucion correcta (online)
    # 1 -> Error (ofline)
    response: bool = False
    if a.returncode == 0:
        response = True

    # and then check the response...
    if response:
        logger.debug(f'{hostname} is up!!')
    else:
        logger.debug(f'{hostname} is down :(')
    return response


def main() -> NoReturn:
    ips: List[Text] = ["192.168.1.1", "192.168.1.11", "192.168.1.0"]

    for ip in ips:
        texto: bool = ping(ip)
        if texto:
            logger.info("{} up".format(ip))
        else:
            logger.info("{} down".format(ip))


if __name__ == '__main__':
    main()
