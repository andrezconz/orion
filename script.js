document.addEventListener('DOMContentLoaded', () => {
    // Scroll Animations
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.8s forwards ease-out';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-up, .column-card, .card, .service-item');
    animatedElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease-out';
        el.style.transitionDelay = `${index * 0.1}s`;
        observer.observe(el);
    });

    // Framework Interaction
    const nodes = document.querySelectorAll('.node');
    const details = document.querySelectorAll('.detail-item');

    nodes.forEach((node, index) => {
        node.addEventListener('mouseenter', () => {
            // Remove active class from all
            nodes.forEach(n => n.classList.remove('active'));
            details.forEach(d => d.classList.remove('active-detail'));
            
            // Add to current
            node.classList.add('active');
            details[index].classList.add('active-detail');
        });
    });

    // Reset to "DECIDIR" as default active (index 3)
    const resetToDefault = () => {
        nodes.forEach(n => n.classList.remove('active'));
        details.forEach(d => d.classList.remove('active-detail'));
        nodes[3].classList.add('active');
        details[3].classList.add('active-detail');
    };

    const frameworkSection = document.querySelector('.framework-diagram');
    frameworkSection.addEventListener('mouseleave', resetToDefault);

    // Form Handling
    const form = document.querySelector('.lead-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = form.querySelector('input').value;
            const button = form.querySelector('button');
            
            button.textContent = 'Enviando...';
            button.disabled = true;

            setTimeout(() => {
                button.textContent = '¡Gracias!';
                form.querySelector('input').value = '';
                button.style.backgroundColor = '#48BB78'; // Success green
            }, 1000);
        });
    }

    // Hero tracking span animation
    const titleSpan = document.querySelector('.hero-title span');
    if (titleSpan) {
        titleSpan.style.letterSpacing = '0px';
        setTimeout(() => {
            titleSpan.style.transition = 'letter-spacing 2s ease-in-out';
            titleSpan.style.letterSpacing = '4px';
        }, 500);
    }
});
