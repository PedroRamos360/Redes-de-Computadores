from scapy.all import *
from backend.PcapReader import PcapReader
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


class TcpAnalyzer:
    def __init__(self):
        pcapReader = PcapReader(current_dir + "/tcp.pcap")
        print("Carregando pcap TCP...")
        self.packets = pcapReader.get_content()
        print("Pcap TCP carregado!")

    def get_data(self, slice_start, slice_end):
        data = []
        for packet in self.packets[slice(slice_start, slice_end)]:
            try:
                if TCP in packet:
                    tcp_layer = packet[TCP]
                    packet_data = {
                        "srcPort": tcp_layer.sport,
                        "dstPort": tcp_layer.dport,
                        "seq": tcp_layer.seq,
                        "ack": tcp_layer.ack,
                        "dataOffset": str(tcp_layer.dataofs),
                        "reserved": str(tcp_layer.reserved),
                        "flags": {
                            "urg": str(tcp_layer.flags & 32),
                            "ack": str(tcp_layer.flags & 16),
                            "psh": str(tcp_layer.flags & 8),
                            "rst": str(tcp_layer.flags & 4),
                            "syn": str(tcp_layer.flags & 2),
                            "fin": str(tcp_layer.flags & 1),
                        },
                    }
                    data.append(packet_data)
            except Exception as e:
                print(f"Error processing packet: {e}")

        return data
