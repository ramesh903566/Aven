import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# 1. HERO SECTION UPDATES
# Remove eyebrow
content = content.replace('<p class="hero-eyebrow reveal" style="color: var(--accent); font-family: Outfit, sans-serif; font-size: clamp(0.8rem, 2vw, 1.2rem); letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 1.5rem; font-weight: 700;">CSE STUDENT • DEVELOPER • SECURITY ENGINEER</p>', '')

# Rewrite the hero title and deck into a grid
old_hero_title = """        <h1 class="hero-title" id="hero-title" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(4rem, 12vw, 10rem); text-transform: uppercase; line-height: 0.85; margin: 0 0 2rem 0; letter-spacing: -0.02em;">
          <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">I BUILD</div></span>
          <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">SECURE</div></span>
          <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">SYSTEMS.</div></span>
        </h1>
        <p class="hero-deck reveal" style="max-width: 38rem; font-size: clamp(1rem, 2.5vw, 1.25rem); color: var(--paper); line-height: 1.6; margin-bottom: 3rem;">Ramesh (Bunny) is a Computer Science student in Bangalore specializing in cybersecurity engineering through backend systems, cloud architecture, and application security.</p>"""

new_hero_title = """        <div style="display: grid; grid-template-columns: minmax(280px, 1fr) auto; gap: clamp(2rem, 5vw, 6rem); align-items: center; margin-bottom: 4rem;">
          <div class="hero-deck reveal" style="padding: 2rem; border: 1px solid rgba(255,255,255,0.1); background: rgba(10,10,10,0.6); max-width: 32rem;">
            <p style="font-size: clamp(1rem, 1.5vw, 1.15rem); color: var(--paper); line-height: 1.7; margin: 0;">Ramesh (Bunny) is a Computer Science student in Bangalore specializing in cybersecurity engineering through backend systems, cloud architecture, and application security.</p>
          </div>
          <h1 class="hero-title" id="hero-title" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(4rem, 10vw, 10rem); text-transform: uppercase; line-height: 0.85; margin: 0; letter-spacing: -0.02em; text-align: right;">
            <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">I BUILD</div></span>
            <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">SECURE</div></span>
            <span style="display: block; overflow: hidden;"><div style="display: block; transform: translateY(100%);">SYSTEMS.</div></span>
          </h1>
        </div>"""
content = content.replace(old_hero_title, new_hero_title)

# Remove "12+ Security Labs"
old_stats = """        <div class="hero-stats reveal" style="display: flex; gap: clamp(2rem, 5vw, 4rem); margin-bottom: 3rem; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 1.5rem 0; max-width: 48rem;">
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
        </div>"""

new_stats = """        <div class="hero-stats reveal" style="display: flex; gap: clamp(2rem, 5vw, 4rem); margin-bottom: 3rem; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 1.5rem 0; max-width: 32rem;">
          <div>
            <h4 style="margin: 0; font-family: Outfit, sans-serif; font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 800; color: var(--ink);">05+</h4>
            <p style="margin: 0; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted);">Projects Delivered</p>
          </div>
          <div>
            <h4 style="margin: 0; font-family: Outfit, sans-serif; font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 800; color: var(--ink);">03+</h4>
            <p style="margin: 0; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted);">Years Focus</p>
          </div>
        </div>"""
content = content.replace(old_stats, new_stats)

# 2. ABOUT SECTION UPDATE
old_about = '<p class="body-copy reveal">Boxing, calisthenics, bike riding, and physical training reinforce the same qualities needed in engineering: discipline, consistency, controlled aggression, resilience, and staying composed under pressure.</p>'
new_about = '<p class="body-copy reveal">Discipline, consistency, controlled focus, resilience, and staying composed under pressure form the foundation of my engineering approach. The same dedication required for continuous self-improvement translates directly to solving complex software problems and building secure systems.</p>'
content = content.replace(old_about, new_about)

with open('portfolio.html', 'w') as f:
    f.write(content)

