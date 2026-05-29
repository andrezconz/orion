document.addEventListener("DOMContentLoaded", () => {
  const observerOptions = {
    threshold: 0.12,
    rootMargin: "0px 0px -40px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.animation = "fadeInUp 0.75s forwards ease-out";
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const animatedElements = document.querySelectorAll(
    ".animate-up, .column-card, .card, .service-item, .detail-item, .proof-grid > div, .trayectoria-item",
  );

  animatedElements.forEach((el, index) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(24px)";
    el.style.animationDelay = `${Math.min(index * 0.05, 0.35)}s`;
    observer.observe(el);
  });

  const nodes = document.querySelectorAll(".node");
  const details = document.querySelectorAll(".detail-item");

  const activateFrameworkStep = (index) => {
    nodes.forEach((node) => node.classList.remove("active"));
    details.forEach((detail) => detail.classList.remove("active-detail"));

    if (nodes[index] && details[index]) {
      nodes[index].classList.add("active");
      details[index].classList.add("active-detail");
    }
  };

  nodes.forEach((node, index) => {
    node.addEventListener("mouseenter", () => activateFrameworkStep(index));
    node.addEventListener("focus", () => activateFrameworkStep(index));
    node.addEventListener("click", () => activateFrameworkStep(index));
  });

  const frameworkSection = document.querySelector(".framework-diagram");
  if (frameworkSection && nodes.length > 3 && details.length > 3) {
    frameworkSection.addEventListener("mouseleave", () => activateFrameworkStep(3));
  }

  // Language-aware form messages
  const lang = document.documentElement.lang || "es";
  const isEN = lang.startsWith("en");

  const form = document.querySelector(".lead-form");
  if (form) {
    const note = form.querySelector(".form-note");
    const button = form.querySelector("button");

    form.addEventListener("submit", (event) => {
      event.preventDefault();

      button.textContent = isEN ? "Request prepared" : "Solicitud preparada";
      button.disabled = true;

      if (note) {
        note.textContent = isEN
          ? "Thank you. The next step is to connect this form to your email or CRM to receive the request."
          : "Gracias. El siguiente paso es conectar este formulario con tu correo o CRM para recibir la solicitud.";
      }

      setTimeout(() => {
        button.textContent = isEN ? "Prepare Request" : "Preparar solicitud";
        button.disabled = false;
        form.reset();
      }, 4200);
    });
  }
});

