import threading
import sys
from typing import List
from ping3 import ping
import ipaddress
from get_device_info import get_device_info
from get_manufacturer import load_oui_database, get_mac_manufacturer


class ArpDiscovery:
    __network = None
    __devices_discovered = []

    def __init__(self):
        self.__stop_arp = threading.Event()
        self.__arp_thread = threading.Thread(target=self.__start_arp)

    def __start_arp(self):
        pass

    def start():
        self.__arp_thread.start()

    def stop():
        self.__stop_arp.set()
        self.__arp_thread.join()

    def get_all_ips_in_network(network_cidr):
        try:
            network = ipaddress.IPv4Network(network_cidr, strict=False)
            ip_list = [str(ip) for ip in network.hosts()]
            return ip_list
        except ValueError as e:
            return str(e)

    def ping_and_print_info(ip, timeout, devices: list):
        oui_database = load_oui_database()
        response = ping(ip, timeout)
        if response is not None and response is not False:
            device_info = get_device_info(ip)
            if device_info is not None:
                new_device = Device(
                    ip,
                    device_info["mac"],
                    get_mac_manufacturer(device_info["mac"], oui_database),
                    "on",
                )
                print(
                    ip,
                    new_device.macAddress,
                    new_device.vendor,
                    new_device.status,
                )
                devices.append(new_device)
            else:
                new_device = Device(ip, "-", "-", "off")
                print(
                    new_device.ipAddress,
                    new_device.macAddress,
                    new_device.vendor,
                    new_device.status,
                )
                devices.append(new_device)
        else:
            new_device = Device(ip, "-", "-", "off")
            print(
                new_device.ipAddress,
                new_device.macAddress,
                new_device.vendor,
                new_device.status,
            )
            devices.append(new_device)


class Device:
    def __init__(self, ipAddress: str, macAddress: str, vendor: str, status: str):
        self.ipAddress = ipAddress
        self.macAddress = macAddress
        self.vendor = vendor
        self.status = status
