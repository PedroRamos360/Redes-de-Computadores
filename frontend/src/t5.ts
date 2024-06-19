import Api from "./api/Api.js";

console.log("COMEÇou");
const startBtn = document.getElementById("startBtn");

const api = new Api();

let sliceStart = 0;
let sliceInterval = 10;

startBtn?.addEventListener("click", () => {
  alert(
    "Tcp Analyzer inicializando, aguarde enquanto os dados estão sendo buscados"
  );
  setInterval(async () => {
    const data = await api.get(
      `/tcp-data?slice_start=${sliceStart}&slice_end=${
        sliceStart + sliceInterval
      }`
    );
    console.log({
      data,
    });
    sliceStart += sliceInterval;
  }, 5000);
});
