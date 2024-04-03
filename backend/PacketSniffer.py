from scapy.all import sniff
from scapy.layers.inet import IP
import threading


class PacketSniffer:
    def __init__(self):
        self.__results = []
        self.__destination_ips = {}
        self.__source_ips = {}
        self.__destination_countries = {}
        self.__stop_sniffing = threading.Event()
        self.__sniffer_thread = threading.Thread(target=self.__start_sniffing)

    def __start_sniffing(self):
        filter_expression = "ip and tcp"
        while not self.__stop_sniffing.is_set():
            self.__results = sniff(count=100, filter=filter_expression)
            self.__extract_src_and_dst_ips()
            self.__extract_destination_countries()

    def __extract_src_and_dst_ips(self):
        print(self.__results.show())
        for pkt in self.__results:
            if IP in pkt:
                src_ip = pkt[IP].src
                dst_ip = pkt[IP].dst
                if src_ip in self.__source_ips:
                    self.__source_ips[src_ip] += 1
                else:
                    self.__source_ips[src_ip] = 1
                if dst_ip in self.__destination_ips:
                    self.__destination_ips[dst_ip] += 1
                else:
                    self.__destination_ips[dst_ip] = 1

    def __extract_destination_countries(self):
        pass

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
