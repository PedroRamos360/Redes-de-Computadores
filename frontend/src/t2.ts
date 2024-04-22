import Api from "./api/Api.js";

console.log("COMEÇou");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");

const api = new Api();

interface ArpDevice {
  ipAddress: string;
  macAddress: string;
  vendor: string;
}

function replaceEntries(arpDevices: ArpDevice[]) {
  const tableBody = document
    .getElementById("deviceTable")
    ?.getElementsByTagName("tbody")?.[0];

  if (!tableBody) throw new Error("Table not found!");

  tableBody.innerHTML = "";

  for (const arpDevice of arpDevices) {
    const newRow = tableBody.insertRow();
    const macCell = newRow.insertCell(0);
    const ipCell = newRow.insertCell(1);
    const fabricanteCell = newRow.insertCell(2);
    macCell.innerHTML = arpDevice.macAddress;
    ipCell.innerHTML = arpDevice.ipAddress;
    fabricanteCell.innerHTML = arpDevice.vendor;
  }
}

startBtn?.addEventListener("click", () => {
  alert("Arp inicializado, coletando dispotivos");
  void api.post("/arp-start");
});

stopBtn?.addEventListener("click", () => {
  alert("Arp finalizado.");
  void api.post("/arp-stop");
});

async function addArpDevicesInTable() {
  const data = await api.get("/arp-devices");
  replaceEntries(data);
}

void addArpDevicesInTable();

setInterval(async () => {
  await addArpDevicesInTable();
}, 2000);
