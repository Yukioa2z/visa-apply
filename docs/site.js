const copyButton = document.querySelector("[data-copy-command]");
const copyStatus = document.querySelector(".copy-status");
const command = document.querySelector("[data-command]");

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

copyButton.addEventListener("click", async () => {
  if (!command) return;

  try {
    await copyText(command.dataset.command);
    copyStatus.textContent = "Command copied.";
  } catch {
    copyStatus.textContent = "Copy failed. Select the command manually.";
  }
});
