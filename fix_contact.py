with open('portfolio.html', 'r') as f:
    content = f.read()

contact_html = """
    <!-- CONTACT -->
    <section class="scene contact" id="contact" aria-labelledby="contact-title">
      <div class="scene-inner text-center" style="text-align: center; max-width: 600px; margin: 0 auto; padding: 4rem 1.25rem;">
        <h2 class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 10vw, 6rem); text-transform: uppercase; line-height: 0.9; margin-bottom: 2rem; letter-spacing: -0.02em;" id="contact-title">Contact.</h2>
        <p class="body-copy reveal" style="color: var(--muted); margin-bottom: 3rem;">Ready to build secure, performant systems together? Let's connect.</p>
        <div class="contact-links reveal">
          <a href="mailto:ramesh@example.com" class="contact-link magnetic">Email</a>
          <a href="https://linkedin.com/in/ramesh" class="contact-link magnetic" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          <a href="https://github.com/ramesh903566" class="contact-link magnetic" target="_blank" rel="noopener noreferrer">GitHub</a>
        </div>
      </div>
    </section>

    """

content = content.replace("<footer", contact_html + "<footer")

with open('portfolio.html', 'w') as f:
    f.write(content)
