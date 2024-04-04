from scapy.all import sniff
from scapy.layers.inet import IP
import threading
from IpToCountry import IpToCountry


class PacketSniffer:
    def __init__(self):
        self.__results = []
        self.__destination_ips = {}
        self.__source_ips = {}
        self.__destination_countries = {}
        self.__stop_sniffing = threading.Event()
        self.__sniffer_thread = threading.Thread(target=self.__start_sniffing)
        print("Loading ip to country csv...")
        self.__ip_to_country = IpToCountry("ip_to_country.csv")

    def __start_sniffing(self):
        filter_expression = "ip and tcp"
        while not self.__stop_sniffing.is_set():
            print("sniffing 10 packets...")
            self.__results = sniff(count=10, filter=filter_expression)
            print(self.__results.show())
            self.__parse_results()

    def __parse_results(self):
        for pkt in self.__results:
            if IP in pkt:
                src_ip = pkt[IP].src
                dst_ip = pkt[IP].dst
                self.__add_source_ip_entry(src_ip)
                self.__add_destination_ip_entry(dst_ip)
                self.__add_country_entry(dst_ip)

    def __add_country_entry(self, ip: str):
        country = self.__ip_to_country.get_country(ip)
        if country in self.__destination_countries:
            self.__destination_countries[country] += 1
        else:
            self.__destination_countries[country] = 1

    def __add_source_ip_entry(self, ip: str):
        if ip in self.__source_ips:
            self.__source_ips[ip] += 1
        else:
            self.__source_ips[ip] = 1

    def __add_destination_ip_entry(self, ip: str):
        if ip in self.__destination_ips:
            self.__destination_ips[ip] += 1
        else:
            self.__destination_ips[ip] = 1

    def start(self):
        self.__sniffer_thread.start()

    def stop(self):
        self.__stop_sniffing.set()
        self.__sniffer_thread.join()

    def get_reports(self):
        return {
            "sourceIps": self.__source_ips,
            "destinationIps": self.__destination_ips,
            "destinationCountries": self.__destination_countries,
        }
