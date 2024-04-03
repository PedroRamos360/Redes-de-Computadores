from typing import Union
from PacketSniffer import PacketSniffer

from fastapi import FastAPI

app = FastAPI()

packet_sniffer = PacketSniffer()
packet_sniffer.start()


@app.get("/reports")
def get_reports():
    return packet_sniffer.get_reports()
