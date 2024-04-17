import os
import sys
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

current_dir = os.path.dirname(os.path.abspath(__file__))
# dir = os.path.join(current_dir, "PacketSniffer")
# sys.path.append(dir)
# from PacketSniffer import PacketSniffer
# from ArpDiscovery import ArpDiscovery

sys.path.append(os.path.join(current_dir, "ArpDiscovery"))
from ArpDiscovery import ArpDiscovery

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# packet_sniffer = PacketSniffer()
arp_discovery = ArpDiscovery("10.0.0.0/24")


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
    return {"status": "started"}


@app.post("/arp-start")
def start_arp():
    arp_discovery.start()
    return {"status": "started"}


@app.post("/arp-stop")
def stop_arp():
    arp_discovery.stop()
    return {"status": "stopped"}


@app.get("/arp-devices")
def get_arp_devices():
    return arp_discovery.get_devices()
