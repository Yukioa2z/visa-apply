const copyButtons = Array.from(document.querySelectorAll("[data-copy-command]"));
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

copyButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    if (!command) return;

    const isHeroButton = button.classList.contains("hero-copy-button");
    const defaultLabel = button.textContent;

    try {
      await copyText(command.dataset.command);

      if (isHeroButton) {
        button.textContent = "Copied";
        window.setTimeout(() => {
          button.textContent = defaultLabel;
        }, 1600);
      } else {
        copyStatus.textContent = "Command copied.";
      }
    } catch {
      if (isHeroButton) {
        button.textContent = "Copy failed";
        window.setTimeout(() => {
          button.textContent = defaultLabel;
        }, 1600);
      } else {
        copyStatus.textContent = "Copy failed. Select the command manually.";
      }
    }
  });
});
