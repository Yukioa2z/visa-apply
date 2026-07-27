const copyButtons = Array.from(document.querySelectorAll("[data-copy-command]"));
const command = document.querySelector("[data-command]");
const copyToast = document.querySelector(".copy-toast");
const downloadCount = document.querySelector("[data-download-count]");
const downloadCountValue = document.querySelector("[data-download-count-value]");
let copyToastTimer;

const NPM_PACKAGE = "@yukioa2z/visa-apply";
const NPM_LAUNCH_DATE = "2026-07-20";

async function updateDownloadCount() {
  if (!downloadCount || !downloadCountValue) return;

  const today = new Date().toISOString().slice(0, 10);
  const packageName = encodeURIComponent(NPM_PACKAGE);
  const endpoint =
    `https://api.npmjs.org/downloads/point/${NPM_LAUNCH_DATE}:${today}/${packageName}`;

  try {
    const response = await fetch(endpoint, { mode: "cors" });
    if (!response.ok) throw new Error(`npm downloads returned ${response.status}`);

    const result = await response.json();
    if (!Number.isFinite(result.downloads)) {
      throw new Error("npm downloads response did not include a number");
    }

    downloadCountValue.textContent = new Intl.NumberFormat("en").format(result.downloads);
    downloadCount.dataset.status = "live";
  } catch {
    downloadCountValue.textContent = downloadCount.dataset.fallbackCount || "500+";
    downloadCount.dataset.status = "fallback";
  }
}

function showCopyToast(message) {
  if (!copyToast) return;

  window.clearTimeout(copyToastTimer);
  copyToast.textContent = message;
  copyToast.classList.add("is-visible");

  copyToastTimer = window.setTimeout(() => {
    copyToast.classList.remove("is-visible");
    copyToast.textContent = "";
  }, 2200);
}

async function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await navigator.clipboard.writeText(text);
      return;
    } catch {
      // Fall through when clipboard access is blocked by the browser.
    }
  }

  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  document.body.appendChild(textarea);
  textarea.select();
  const copied = document.execCommand("copy");
  textarea.remove();
  if (!copied) throw new Error("Copy command was rejected");
}

copyButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    if (!command) return;

    try {
      await copyText(command.dataset.command);
      showCopyToast("Copied, now paste to your agent.");
    } catch {
      showCopyToast("Copy failed. Copy the command below.");
    }
  });
});

updateDownloadCount();
