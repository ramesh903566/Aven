import re

def extract_section(html, section_id):
    pattern = r'<section class="scene[^>]*" id="' + section_id + r'".*?</section>'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        return match.group(0)
    return ""

with open('portfolio.html', 'r') as f:
    content = f.read()

# 1. Update CSS Variables
old_vars = """    :root {
      --ink: #f2eee5;
      --paper: #d8cfc0;
      --muted: #a79f91;
      --dim: #6e685f;
      --charcoal: #0a0a08;
      --panel: rgba(14, 14, 12, 0.58);
      --line: rgba(242, 238, 229, 0.14);
      --accent: #c86f45;
      --accent-2: #7fb0a1;
      --blueprint: #9cb7c8;
      --danger: #d76155;
      --shadow: rgba(0, 0, 0, 0.58);
    }"""
new_vars = """    :root {
      --ink: #ffffff;
      --paper: #e0e0e0;
      --muted: #999999;
      --dim: #555555;
      --charcoal: #050505;
      --panel: rgba(10, 10, 10, 0.8);
      --line: rgba(255, 255, 255, 0.1);
      --accent: #E6332A;
      --accent-2: #E6332A;
      --blueprint: #9cb7c8;
      --danger: #E6332A;
      --shadow: rgba(0, 0, 0, 0.8);
    }"""
content = content.replace(old_vars, new_vars)

# Remove old backgrounds
content = re.sub(r'body \{\s*margin: 0;\s*min-width: 320px;\s*background:.*?;', 'body {\n      margin: 0;\n      min-width: 320px;\n      background: #050505;', content, flags=re.DOTALL)
content = re.sub(r'body::after \{.*?\}', '', content, flags=re.DOTALL)

# 2. Hero Section Redesign
# Remove canvas HTML
content = re.sub(r'<div id="canvas-stage".*?</div>\s*<div class="lighting-layer".*?</div>', '', content, flags=re.DOTALL)

old_hero_css = """    .scene.hero::before {
      content: "";
      position: absolute;
      inset: 0;
      z-index: 0;
      background-image: url("assets/hero-bg.jpg");
      background-size: cover;
      background-position: center;
      opacity: 0.15;
      mix-blend-mode: luminosity;
    }"""
new_hero_css = """    .scene.hero::before {
      content: "";
      position: absolute;
      right: -10vw;
      top: 50%;
      transform: translateY(-50%);
      width: 50vw;
      height: 50vw;
      border-radius: 50%;
      background-color: var(--accent);
      z-index: 0;
      opacity: 0.9;
      filter: blur(1px);
    }
    
    @media (max-width: 768px) {
      .scene.hero::before {
        width: 80vw;
        height: 80vw;
        right: -20vw;
        top: 25%;
        transform: none;
      }
    }"""
content = content.replace(old_hero_css, new_hero_css)

old_hero_html = extract_section(content, "work")

new_hero_html = """    <section class="scene hero" id="work" aria-labelledby="hero-title" style="position: relative; z-index: 2; display: flex; flex-direction: column; justify-content: center; overflow: hidden;">
      <div class="scene-inner hero-copy" style="max-width: 100%; z-index: 2; position: relative;">
        <p class="hero-eyebrow reveal" style="color: var(--accent); font-family: Outfit, sans-serif; font-size: clamp(0.8rem, 2vw, 1.2rem); letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 1.5rem; font-weight: 700;">CSE STUDENT • DEVELOPER • SECURITY ENGINEER</p>
        <h1 class="hero-title" id="hero-title" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(4rem, 12vw, 10rem); text-transform: uppercase; line-height: 0.85; margin: 0 0 2rem 0; letter-spacing: -0.02em;">
          <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">I BUILD</div></span>
          <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">SECURE</div></span>
          <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">SYSTEMS.</div></span>
        </h1>
        <p class="hero-deck reveal" style="max-width: 38rem; font-size: clamp(1rem, 2.5vw, 1.25rem); color: var(--paper); line-height: 1.6; margin-bottom: 3rem;">Ramesh (Bunny) is a Computer Science student in Bangalore specializing in cybersecurity engineering through backend systems, cloud architecture, and application security.</p>
        
        <div class="hero-stats reveal" style="display: flex; gap: clamp(2rem, 5vw, 4rem); margin-bottom: 3rem; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 1.5rem 0; max-width: 48rem;">
          <div>
            <h4 style="margin: 0; font-family: Outfit, sans-serif; font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 800; color: var(--ink);">05+</h4>
            <p style="margin: 0; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted);">Projects Delivered</p>
          </div>
          <div>
            <h4 style="margin: 0; font-family: Outfit, sans-serif; font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 800; color: var(--ink);">12+</h4>
            <p style="margin: 0; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted);">Security Labs</p>
          </div>
          <div>
            <h4 style="margin: 0; font-family: Outfit, sans-serif; font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 800; color: var(--ink);">03+</h4>
            <p style="margin: 0; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted);">Years Focus</p>
          </div>
        </div>

        <div class="hero-ctas reveal">
          <a href="#projects" class="text-link" style="background: var(--accent); color: var(--ink); border-color: var(--accent); font-weight: 700;">View Projects</a>
          <a href="#contact" class="text-link">Contact Me</a>
        </div>
      </div>
    </section>

    <section class="scene" style="min-height: auto; padding: 6rem 1.25rem; background: var(--accent); color: var(--charcoal); display: flex; align-items: center; justify-content: center; text-align: center; border-radius: 0;">
      <h2 class="reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(2rem, 6vw, 5rem); text-transform: uppercase; line-height: 0.9; margin: 0; letter-spacing: -0.02em;">
        SECURITY ISN'T AN ADD-ON.<br>IT'S THE ARCHITECTURE.
      </h2>
    </section>"""
content = content.replace(old_hero_html, new_hero_html)


# 3. Update Skills Section
old_skills_html = extract_section(content, "skills")
if old_skills_html:
    new_skills_html = """    <section class="scene" id="skills" aria-labelledby="skills-title">
      <div class="scene-inner">
        <h2 class="section-title reveal" id="skills-title" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 10vw, 6rem); text-transform: uppercase; line-height: 0.9; margin-bottom: 4rem; letter-spacing: -0.02em;">WHAT I DO</h2>
        
        <div class="skills-grid reveal" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0;">
          
          <article style="padding: 2.5rem; border: 1px solid var(--line); border-bottom: 1px solid var(--line); border-right: 1px solid var(--line);">
            <span style="display: block; font-family: Outfit, sans-serif; font-weight: 800; font-size: 1.5rem; color: var(--accent); margin-bottom: 1.5rem;">01</span>
            <h3 style="margin: 0 0 1rem; font-family: Outfit, sans-serif; font-weight: 700; font-size: 1.25rem; text-transform: uppercase; color: var(--ink);">Backend Engineering</h3>
            <p style="margin: 0; color: var(--muted); line-height: 1.6; font-size: 0.95rem;">Designing robust APIs, handling complex data flows, and architecting scalable server-side systems with Python, FastAPI, Node.js, and PostgreSQL.</p>
          </article>

          <article style="padding: 2.5rem; border: 1px solid var(--line); border-bottom: 1px solid var(--line);">
            <span style="display: block; font-family: Outfit, sans-serif; font-weight: 800; font-size: 1.5rem; color: var(--accent); margin-bottom: 1.5rem;">02</span>
            <h3 style="margin: 0 0 1rem; font-family: Outfit, sans-serif; font-weight: 700; font-size: 1.25rem; text-transform: uppercase; color: var(--ink);">Application Security</h3>
            <p style="margin: 0; color: var(--muted); line-height: 1.6; font-size: 0.95rem;">Integrating security into the SDLC. Vulnerability assessment, secure coding practices, JWT/OAuth hardening, and mitigating OWASP Top 10 threats.</p>
          </article>

          <article style="padding: 2.5rem; border: 1px solid var(--line); border-right: 1px solid var(--line);">
            <span style="display: block; font-family: Outfit, sans-serif; font-weight: 800; font-size: 1.5rem; color: var(--accent); margin-bottom: 1.5rem;">03</span>
            <h3 style="margin: 0 0 1rem; font-family: Outfit, sans-serif; font-weight: 700; font-size: 1.25rem; text-transform: uppercase; color: var(--ink);">Cloud Infrastructure</h3>
            <p style="margin: 0; color: var(--muted); line-height: 1.6; font-size: 0.95rem;">Deploying and managing scalable systems. Docker containerization, CI/CD pipelines, AWS fundamentals, and infrastructure-as-code principles.</p>
          </article>

          <article style="padding: 2.5rem; border: 1px solid var(--line);">
            <span style="display: block; font-family: Outfit, sans-serif; font-weight: 800; font-size: 1.5rem; color: var(--accent); margin-bottom: 1.5rem;">04</span>
            <h3 style="margin: 0 0 1rem; font-family: Outfit, sans-serif; font-weight: 700; font-size: 1.25rem; text-transform: uppercase; color: var(--ink);">Frontend Systems</h3>
            <p style="margin: 0; color: var(--muted); line-height: 1.6; font-size: 0.95rem;">Building performant, accessible, and responsive user interfaces using React, TypeScript, TailwindCSS, and raw modern CSS/HTML.</p>
          </article>

        </div>
      </div>
    </section>"""
    content = content.replace(old_skills_html, new_skills_html)

# 4. Modify GSAP JS
content = re.sub(r'const portfolioData = \{.*?\};\n', '', content, flags=re.DOTALL)
content = re.sub(r'const canvas = document\.getElementById\("character-canvas"\);.*?// Navigation', '// Navigation', content, flags=re.DOTALL)

# In setupAnimations, remove sequence and canvas animations
# and fix the hero title animation to animate the 'div's instead of 'i's.
old_setup = """        if (!prefersReducedMotion) {
          gsap.to(sequence.state, {
            frame: portfolioData.frames.count - 1,
            snap: "frame",
            ease: "none",
            scrollTrigger: {
              trigger: document.body,
              start: "top top",
              end: "bottom bottom",
              scrub: 1.1
            },
            onUpdate: sequence.render
          });

          gsap.to(canvas, {
            scale: 1.06,
            xPercent: -3,
            ease: "none",
            scrollTrigger: {
              trigger: "#work",
              start: "top top",
              end: "bottom top",
              scrub: true
            }
          });

          gsap.to(".lighting-layer", {
            "--light-x": "62%",
            "--light-y": "46%",
            ease: "none",
            scrollTrigger: {
              trigger: document.body,
              start: "top top",
              end: "bottom bottom",
              scrub: true
            }
          });

        } else {
          sequence.state.frame = 0;
          sequence.render();
        }

        gsap.to(".hero-title i", {"""

new_setup = """        gsap.to(".hero-title div", {"""

content = content.replace(old_setup, new_setup)

# Update font families for titles to match brutalist
content = re.sub(r'class="section-title reveal".*?>', lambda m: m.group(0).replace('class="section-title reveal"', 'class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 10vw, 6rem); text-transform: uppercase; line-height: 0.9; margin-bottom: 2rem; letter-spacing: -0.02em;"'), content)

with open('portfolio.html', 'w') as f:
    f.write(content)

