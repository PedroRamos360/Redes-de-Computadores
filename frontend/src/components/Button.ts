import Api from "../api/Api.js";

console.log("COMEÇou")
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');

const api = new Api();

startBtn?.addEventListener('click', () => {
  alert("Sniffer inicializado, aguarde até que o sniffer encontre pacotes.");
  void api.post("/sniffer-start");
});

stopBtn?.addEventListener('click', () => {
  alert("Sniffer finalizado.");
  void api.post("/sniffer-stop");
});

