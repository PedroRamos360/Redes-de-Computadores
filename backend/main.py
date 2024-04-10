import os
import sys
from typing import Union

current_dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.join(current_dir, "PacketSniffer")
sys.path.append(dir)
from PacketSniffer import PacketSniffer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])
packet_sniffer = PacketSniffer()


@app.get("/sniffer-reports")
def get_sniffer_reports():
    return packet_sniffer.get_reports(5)


@app.post("/sniffer-start")
def start_sniffer():
    packet_sniffer.start()
    return {"status": "started"}


@app.post("/sniffer-stop")
def start_sniffer():
    packet_sniffer.start()
    return {"status": "started"}
