const message = document.querySelector("#message");

export function showMessage(text, isError = false) {
  message.textContent = text;
  message.classList.toggle("error", isError);
  message.setAttribute("role", isError ? "alert" : "status");
  message.tabIndex = 0;
  message.title = "Click to dismiss";
  message.hidden = false;
}

export function clearMessage() {
  message.hidden = true;
  message.removeAttribute("tabindex");
  message.removeAttribute("title");
}

message.addEventListener("click", clearMessage);
message.addEventListener("keydown", (event) => {
  if (event.key === "Enter" || event.key === " " || event.key === "Escape") {
    event.preventDefault();
    clearMessage();
  }
});
