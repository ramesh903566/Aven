import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# 1. Fix "EVIDENCE." to "PROJECTS." in the #projects section
content = re.sub(
    r'<h2 class="section-title reveal"[^>]*id="projects-title">EVIDENCE\.</h2>',
    '<h2 class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 10vw, 6rem); text-transform: uppercase; line-height: 0.9; margin-bottom: 3rem; letter-spacing: -0.02em;" id="projects-title">Projects.</h2>',
    content
)

# 2. Rebuild the #contact section
contact_start = content.find('<!-- CONTACT -->')
if contact_start == -1:
    contact_start = content.find('<section class="scene contact" id="contact"')

footer_start = content.find('<footer')

if contact_start != -1 and footer_start != -1:
    new_contact = """
    <!-- CONTACT -->
    <section class="scene contact" id="contact" aria-labelledby="contact-title" style="min-height: 100vh; display: flex; align-items: center;">
      <div class="scene-inner wide">
        <h2 class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(4rem, 12vw, 8rem); text-transform: uppercase; line-height: 0.9; margin-bottom: 2rem; letter-spacing: -0.02em; color: var(--paper);" id="contact-title">
          Let's build<br>
          something<br>
          worth<br>
          securing.
        </h2>
        <p class="body-copy reveal" style="color: var(--muted); margin-bottom: 4rem; max-width: 600px; font-size: 1.1rem; line-height: 1.6;">
          Available for collaboration, early engineering work, cybersecurity<br>
          learning projects, and ambitious systems that need careful builders.
        </p>
        
        <div class="contact-links reveal" style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; justify-content: flex-start;">
          <a href="mailto:ramesh@example.com" class="contact-link magnetic" style="border: 1px solid rgba(255,255,255,0.1); padding: 1rem 2rem; color: var(--paper); text-decoration: none; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; transition: all 0.3s ease;">Email —</a>
          <a href="https://github.com/ramesh903566" class="contact-link magnetic" target="_blank" rel="noopener noreferrer" style="border: 1px solid rgba(255,255,255,0.1); padding: 1rem 2rem; color: var(--paper); text-decoration: none; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; transition: all 0.3s ease;">GitHub —</a>
          <a href="https://linkedin.com/in/ramesh" class="contact-link magnetic" target="_blank" rel="noopener noreferrer" style="border: 1px solid rgba(255,255,255,0.1); padding: 1rem 2rem; color: var(--paper); text-decoration: none; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; transition: all 0.3s ease;">LinkedIn —</a>
          <a href="RameshResume.pdf" class="contact-link magnetic" target="_blank" style="border: 1px solid rgba(255,255,255,0.1); padding: 1rem 2rem; color: var(--paper); text-decoration: none; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; transition: all 0.3s ease;">Resume / Download CV —</a>
        </div>
      </div>
    </section>

"""
    content = content[:contact_start] + new_contact + content[footer_start:]

with open('portfolio.html', 'w') as f:
    f.write(content)

