import os
import sys
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../"))
from backend.PacketSniffer.PacketSniffer import PacketSniffer
from backend.ArpDiscovery.ArpDiscovery import ArpDiscovery
from backend.RipSniffer.RipSniffer import RipSniffer
from backend.UdpDns.UdpDns import UdpDns

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
packet_sniffer = PacketSniffer()
rip_sniffer = RipSniffer()
arp_discovery = ArpDiscovery("172.21.0.1/28")
udp_dns = UdpDns()


@app.get("/sniffer-reports")
def get_sniffer_reports():
    return packet_sniffer.get_reports(5)


@app.post("/sniffer-start")
def start_sniffer():
    packet_sniffer.start()
    return {"status": "started"}


@app.post("/sniffer-stop")
def start_sniffer():
    packet_sniffer.stop()
    return {"status": "stopped"}


@app.post("/arp-start")
def start_arp():
    arp_discovery.start()
    return {"status": "started"}


@app.post("/arp-set-network/{network}/{mask}")
def set_arp_network(network: str, mask: str):
    arp_discovery.set_network(network + "/" + mask)
    return {"status": "network set sucessfully"}


@app.get("/arp-devices")
def get_arp_devices():
    if arp_discovery.finished:
        return {"finished": True}
    return arp_discovery.get_devices()


@app.get("/rip-data")
def get_rip_data():
    return rip_sniffer.get_data()


@app.post("/dns-start")
def start_dns():
    udp_dns.start()
    return {"status": "started"}


@app.post("/dns-stop")
def stop_dns():
    udp_dns.stop()
    return {"status": "stopped"}


@app.get("/dns-data")
def get_dns_data():
    return udp_dns.get_dns_results()
