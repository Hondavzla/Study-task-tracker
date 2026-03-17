document.addEventListener("DOMContentLoaded", () => {
  // Find every chevron toggle button on the page.
  const buttons = document.querySelectorAll(".chevron-btn");

  // Add click behavior for each accordion toggle.
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      // Read the target panel id from the data attribute.
      const targetId = button.getAttribute("data-target");
      const panel = document.getElementById(targetId);
      if (!panel) return;

      // Toggle open state on both panel and chevron.
      panel.classList.toggle("open");
      button.classList.toggle("open");

      // Keep aria-expanded in sync for accessibility.
      const expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
    });
  });
});
