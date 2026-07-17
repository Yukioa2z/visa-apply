const tabs = Array.from(document.querySelectorAll("[role='tab']"));
const panels = Array.from(document.querySelectorAll("[role='tabpanel']"));
const copyButton = document.querySelector("[data-copy-command]");
const copyStatus = document.querySelector(".copy-status");

function activateTab(tab) {
  const target = tab.dataset.target;

  tabs.forEach((item) => {
    const isActive = item === tab;
    item.classList.toggle("is-active", isActive);
    item.setAttribute("aria-selected", String(isActive));
    item.tabIndex = isActive ? 0 : -1;
  });

  panels.forEach((panel) => {
    const isActive = panel.id === `panel-${target}`;
    panel.classList.toggle("is-active", isActive);
    panel.hidden = !isActive;
  });

  copyStatus.textContent = "";
}

tabs.forEach((tab, index) => {
  tab.addEventListener("click", () => activateTab(tab));
  tab.addEventListener("keydown", (event) => {
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;

    event.preventDefault();
    const direction = event.key === "ArrowRight" ? 1 : -1;
    const nextIndex = (index + direction + tabs.length) % tabs.length;
    activateTab(tabs[nextIndex]);
    tabs[nextIndex].focus();
  });
});

async function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text);
    return;
  }

  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  textarea.remove();
}

copyButton.addEventListener("click", async () => {
  const activePanel = document.querySelector(".command-panel.is-active");
  if (!activePanel) return;

  try {
    await copyText(activePanel.dataset.command);
    copyStatus.textContent = "Command copied.";
  } catch {
    copyStatus.textContent = "Copy failed. Select the command manually.";
  }
});
