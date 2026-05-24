// Highlight active nav link based on scroll position
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll("nav a");

function onScroll() {
  let current = "";
  sections.forEach((section) => {
    if (window.scrollY >= section.offsetTop - 120) {
      current = section.id;
    }
  });
  navLinks.forEach((link) => {
    link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
  });
}

window.addEventListener("scroll", onScroll, { passive: true });
