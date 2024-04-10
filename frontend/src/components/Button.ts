import Api from "../api/Api";

export async function start() {
  const api = new Api();
  await api.post("/sniffer-start");
}

export async function stop() {
  const api = new Api();
  await api.post("/sniffer-stop");
}
