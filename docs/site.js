const copyButtons = Array.from(document.querySelectorAll("[data-copy-command]"));
const copyStatus = document.querySelector(".copy-status");
const command = document.querySelector("[data-command]");
const copyToast = document.querySelector(".copy-toast");
let copyToastTimer;

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

    const isHeroButton = button.classList.contains("hero-copy-button");

    try {
      await copyText(command.dataset.command);

      if (isHeroButton) {
        showCopyToast("Copied, now paste to your agent.");
      } else {
        copyStatus.textContent = "Command copied.";
      }
    } catch {
      if (isHeroButton) {
        showCopyToast("Copy failed. Copy the command below.");
      } else {
        copyStatus.textContent = "Copy failed. Select the command manually.";
      }
    }
  });
});
