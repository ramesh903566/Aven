import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# 1. Update Navigation
nav_old = """  <nav class="site-nav" aria-label="Primary navigation">
    <a href="#work">Home</a>
    <a href="#about">About</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#security-labs">Security Labs</a>
    <a href="#journey">Experience</a>
    <a href="#contact">Contact</a>
  </nav>"""
nav_new = """  <nav class="site-nav" aria-label="Primary navigation">
    <a href="#work">Home</a>
    <a href="#about">About</a>
    <a href="#journey">Journey</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#security-labs">Security Labs</a>
    <a href="#contact">Contact</a>
  </nav>"""
content = content.replace(nav_old, nav_new)

# 2. Update Hero Eyebrow
hero_old = "CSE STUDENT • DEVELOPER • SECURITY ENTHUSIAST"
hero_new = "CSE STUDENT • DEVELOPER • SECURITY ENGINEER IN TRAINING"
content = content.replace(hero_old, hero_new)

# 3. Reorder Sections
# Extract all sections using regex
import collections

# We will just cut out #journey and #person and place them correctly.
def extract_section(html, section_id):
    pattern = r'<section class="scene[^>]*" id="' + section_id + r'".*?</section>'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        return match.group(0)
    return ""

journey_sec = extract_section(content, "journey")
person_sec = extract_section(content, "person")

# Remove them from their original places
if journey_sec:
    content = content.replace(journey_sec, "")
if person_sec:
    content = content.replace(person_sec, "")

# Insert person inside about (at the end of .scene-inner)
# Extract about
about_sec = extract_section(content, "about")
if about_sec and person_sec:
    # extract inner content of person
    person_inner = re.search(r'<div class="scene-inner personal-band">.*?</div>', person_sec, re.DOTALL)
    if person_inner:
        person_content = person_inner.group(0).replace('class="scene-inner personal-band"', 'class="personal-band reveal"')
        
        # insert into about before closing section
        new_about = about_sec.replace('</section>', '\n      ' + person_content + '\n    </section>')
        content = content.replace(about_sec, new_about)

# Re-extract about just in case we need to append journey after it
about_sec_new = extract_section(content, "about")
if about_sec_new and journey_sec:
    content = content.replace(about_sec_new, about_sec_new + "\n\n    " + journey_sec)


# 4. Refactor Synalytix Details
syn_old = """          <ul class="decision-list reveal">
            <li><strong>Problem:</strong> Developers and creators distribute progress across GitHub, LeetCode, social platforms, career portals, and content channels. Synalytix creates one analytics layer across that activity.</li>
            <li><strong>Architecture:</strong> React / Vite / TypeScript / TailwindCSS, Next.js 16 exploration, FastAPI, PostgreSQL, Redis, Celery, JWT/OAuth, WebSockets, Docker, GitHub Actions, Sentry, and Prometheus.</li>
            <li><strong>Security:</strong> API authorization, IDOR prevention, WebSocket authentication, token rotation, rate limiting, environment-variable security, OAuth security, and production deployment controls.</li>
            <li><strong>Status:</strong> In progress / production-validation stage.</li>
            <li><strong>Links:</strong> <a href="https://github.com/ramesh903566/Synalytix" target="_blank" rel="noopener noreferrer" class="text-link">GitHub</a></li>
          </ul>"""

syn_new = """          <div class="decision-list reveal">
            <div style="margin-bottom: 1.2rem;">
              <h4 style="margin: 0 0 0.2rem; color: var(--ink); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em;">Problem</h4>
              <p style="margin: 0; color: var(--paper); line-height: 1.6;">Developers and creators distribute progress across GitHub, LeetCode, social platforms, career portals, and content channels. Synalytix creates one analytics layer across that activity.</p>
            </div>
            <div style="margin-bottom: 1.2rem;">
              <h4 style="margin: 0 0 0.2rem; color: var(--ink); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em;">Architecture</h4>
              <p style="margin: 0; color: var(--paper); line-height: 1.6;">React / Vite / TypeScript / TailwindCSS, Next.js 16 exploration, FastAPI, PostgreSQL, Redis, Celery, JWT/OAuth, WebSockets, Docker, GitHub Actions, Sentry, and Prometheus.</p>
            </div>
            <div style="margin-bottom: 1.2rem;">
              <h4 style="margin: 0 0 0.2rem; color: var(--ink); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em;">Security</h4>
              <p style="margin: 0; color: var(--paper); line-height: 1.6;">API authorization, IDOR prevention, WebSocket authentication, token rotation, rate limiting, environment-variable security, OAuth security, and production deployment controls.</p>
            </div>
            <div style="margin-bottom: 1.2rem;">
              <h4 style="margin: 0 0 0.2rem; color: var(--ink); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em;">Status</h4>
              <p style="margin: 0; color: var(--accent-2); line-height: 1.6; font-weight: 600;">In progress / production-validation stage.</p>
            </div>
            <div style="margin-top: 1.5rem;">
              <a href="https://github.com/ramesh903566/Synalytix" target="_blank" rel="noopener noreferrer" class="text-link">GitHub</a>
            </div>
          </div>"""

content = content.replace(syn_old, syn_new)

# 5. Fix Architecture overlap
arch_old = """<div class="system-frame architecture reveal" aria-label="Synalytix architecture diagram">"""
arch_new = """<div class="system-frame architecture reveal" aria-label="Synalytix architecture diagram" style="max-width: 100%; overflow: hidden;">"""
content = content.replace(arch_old, arch_new)

# 6. Refactor Mini Projects
mini_old = """          <div class="mini-projects reveal" aria-label="Additional projects">
            <article class="mini-project">
              <h3>Antigravity</h3>
              <p>Offline-first learning and portfolio operating system for notes, resources, commands, code snippets, project tracking, Kanban, import/export, and full-text search.</p>
            </article>
            <article class="mini-project">
              <h3>Stock Market & Portfolio Management System</h3>
              <p>Academic DBMS project for managing stocks, portfolios, transactions, and related financial data with MariaDB / SQL.</p>
            </article>
            <article class="mini-project">
              <h3><a href="https://github.com/ramesh903566/HOROLOGIUM-" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;">HOROLOGIUM</a></h3>
              <p>Watch encyclopedia and educational reference. In development.</p>
            </article>
          </div>"""

mini_new = """          <div class="mini-projects reveal" aria-label="Additional projects" style="display: grid; gap: 1rem; margin-top: 3rem;">
            <article class="system-frame" style="padding: 1.5rem;">
              <h3 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 1rem; text-transform: uppercase; letter-spacing: 0.1em;">Antigravity</h3>
              <p style="margin: 0 0 1rem; color: var(--muted); font-size: 0.95rem; line-height: 1.5;">Offline-first learning and portfolio operating system for notes, resources, commands, code snippets, project tracking, Kanban, import/export, and full-text search.</p>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">React</span>
                <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">SQLite</span>
                <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">Electron</span>
              </div>
            </article>
            <article class="system-frame" style="padding: 1.5rem;">
              <h3 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 1rem; text-transform: uppercase; letter-spacing: 0.1em;">Stock Market & Portfolio Management System</h3>
              <p style="margin: 0 0 1rem; color: var(--muted); font-size: 0.95rem; line-height: 1.5;">Academic DBMS project for managing stocks, portfolios, transactions, and related financial data.</p>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">MariaDB / SQL</span>
                <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">Python</span>
              </div>
            </article>
            <article class="system-frame" style="padding: 1.5rem;">
              <a href="https://github.com/ramesh903566/HOROLOGIUM-" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;">
                <h3 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 1rem; text-transform: uppercase; letter-spacing: 0.1em; text-decoration: underline; text-underline-offset: 4px;">HOROLOGIUM ↗</h3>
              </a>
              <p style="margin: 0 0 1rem; color: var(--muted); font-size: 0.95rem; line-height: 1.5;">Watch encyclopedia and educational reference. Currently in development.</p>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">React</span>
                <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">IN PROGRESS</span>
              </div>
            </article>
          </div>"""
content = content.replace(mini_old, mini_new)

# 7. Add tags to Security Labs
# Using simple replace for specific titles to append badges
lab_1 = '<h3 style="margin: 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.2rem; text-transform: uppercase;">JWT Auth Attack Lab</h3>'
lab_1_new = '<div style="display: flex; justify-content: space-between; align-items: start;"><h3 style="margin: 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.2rem; text-transform: uppercase;">JWT Auth Attack Lab</h3><span class="pill" style="font-size: 0.55rem; min-height: 1.4rem; border-color: var(--accent); color: var(--accent);">COMPLETED</span></div>'
content = content.replace(lab_1, lab_1_new)

lab_2 = '<h3 style="margin: 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.2rem; text-transform: uppercase;">API Authorization Testing</h3>'
lab_2_new = '<div style="display: flex; justify-content: space-between; align-items: start;"><h3 style="margin: 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.2rem; text-transform: uppercase;">API Authorization Testing</h3><span class="pill" style="font-size: 0.55rem; min-height: 1.4rem; border-color: var(--accent); color: var(--accent);">COMPLETED</span></div>'
content = content.replace(lab_2, lab_2_new)

lab_3 = '<h3 style="margin: 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.2rem; text-transform: uppercase;">Docker Security Scan</h3>'
lab_3_new = '<div style="display: flex; justify-content: space-between; align-items: start;"><h3 style="margin: 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.2rem; text-transform: uppercase;">Docker Security Scan</h3><span class="pill" style="font-size: 0.55rem; min-height: 1.4rem; border-color: var(--accent-2); color: var(--accent-2);">IN PROGRESS</span></div>'
content = content.replace(lab_3, lab_3_new)

# 8. Update Journey Heading
journey_head_old = '<h2 class="serif reveal" id="journey-title">Building, engineering, then cybersecurity specialization.</h2>'
journey_head_new = '<h2 class="section-title reveal" id="journey-title" style="font-size: clamp(2.5rem, 6vw, 5rem);">Engineering Journey.</h2><p class="body-copy reveal" style="max-width: 48rem; margin-top: 1rem;">Building, engineering, and focusing towards a cybersecurity specialization.</p>'
content = content.replace(journey_head_old, journey_head_new)

# 9. Format Evidence Section
github_old = """        <div class="evidence-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem; margin-top: 3rem;">
          
          <div class="github-repos reveal">
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 1.5rem;">Open Source & GitHub</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
              <a href="#" class="system-frame" style="padding: 1.5rem; display: block; text-decoration: none; transition: transform 0.2s ease, border-color 0.2s ease;">
                <h4 style="margin: 0 0 0.5rem 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.1rem;">Bunny/Synalytix</h4>
                <p style="margin: 0 0 1rem 0; color: var(--muted); font-size: 0.9rem; line-height: 1.5;">AI-powered personal analytics platform integrating development, productivity and career data.</p>
                <div style="display: flex; gap: 0.5rem;"><span class="pill" style="font-size: 0.65rem; min-height: 1.6rem;">TypeScript</span><span class="pill" style="font-size: 0.65rem; min-height: 1.6rem;">Python</span></div>
              </a>
              <a href="#" class="system-frame" style="padding: 1.5rem; display: block; text-decoration: none; transition: transform 0.2s ease, border-color 0.2s ease;">
                <h4 style="margin: 0 0 0.5rem 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.1rem;">Bunny/Antigravity</h4>
                <p style="margin: 0 0 1rem 0; color: var(--muted); font-size: 0.9rem; line-height: 1.5;">Offline-first learning and portfolio operating system.</p>
                <div style="display: flex; gap: 0.5rem;"><span class="pill" style="font-size: 0.65rem; min-height: 1.6rem;">React</span></div>
              </a>
            </div>
          </div>

          <div class="tech-writing reveal">
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 1.5rem;">Technical Writing</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
              <a href="#" style="padding-bottom: 1rem; border-bottom: 1px solid rgba(242, 238, 229, 0.1); display: block; text-decoration: none; transition: transform 0.2s ease;">
                <p style="margin: 0 0 0.25rem 0; color: var(--accent-2); font-family: Outfit, sans-serif; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">System Design · 5 min read</p>
                <h4 style="margin: 0; color: var(--paper); font-size: 1.1rem; font-weight: 500;">How I Designed Authentication for a FastAPI Application</h4>
              </a>
              <a href="#" style="padding-bottom: 1rem; border-bottom: 1px solid rgba(242, 238, 229, 0.1); display: block; text-decoration: none; transition: transform 0.2s ease;">
                <p style="margin: 0 0 0.25rem 0; color: var(--accent-2); font-family: Outfit, sans-serif; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">Cybersecurity · 8 min read</p>
                <h4 style="margin: 0; color: var(--paper); font-size: 1.1rem; font-weight: 500;">Building a SIEM Detection Rule</h4>
              </a>
            </div>
          </div>

        </div>"""

github_new = """        <div class="evidence-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 4rem; margin-top: 3rem;">
          
          <div class="github-repos reveal">
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 1.5rem;">Open Source & GitHub</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
              <a href="https://github.com/ramesh903566/Synalytix" target="_blank" rel="noopener noreferrer" class="system-frame" style="padding: 1.5rem; display: block; text-decoration: none; transition: transform 0.2s ease, border-color 0.2s ease;">
                <h4 style="margin: 0 0 0.5rem 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.1rem; text-decoration: underline; text-underline-offset: 4px;">Bunny/Synalytix ↗</h4>
                <p style="margin: 0 0 1rem 0; color: var(--muted); font-size: 0.9rem; line-height: 1.5;">AI-powered personal analytics platform integrating development, productivity and career data.</p>
                <div style="display: flex; gap: 0.5rem;"><span class="pill" style="font-size: 0.65rem; min-height: 1.6rem;">TypeScript</span><span class="pill" style="font-size: 0.65rem; min-height: 1.6rem;">Python</span></div>
              </a>
              <a href="https://github.com/ramesh903566" target="_blank" rel="noopener noreferrer" class="system-frame" style="padding: 1.5rem; display: block; text-decoration: none; transition: transform 0.2s ease, border-color 0.2s ease;">
                <h4 style="margin: 0 0 0.5rem 0; color: var(--ink); font-family: Outfit, sans-serif; font-size: 1.1rem; text-decoration: underline; text-underline-offset: 4px;">Bunny/Antigravity ↗</h4>
                <p style="margin: 0 0 1rem 0; color: var(--muted); font-size: 0.9rem; line-height: 1.5;">Offline-first learning and portfolio operating system.</p>
                <div style="display: flex; gap: 0.5rem;"><span class="pill" style="font-size: 0.65rem; min-height: 1.6rem;">React</span></div>
              </a>
            </div>
          </div>

          <div class="tech-writing reveal">
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 1.5rem;">Technical Writing</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
              <a href="https://linkedin.com/in/ramesh988025" target="_blank" rel="noopener noreferrer" style="padding: 1.5rem; border: 1px solid rgba(242, 238, 229, 0.1); background: rgba(242, 238, 229, 0.02); display: block; text-decoration: none; transition: transform 0.2s ease, border-color 0.2s ease;">
                <p style="margin: 0 0 0.5rem 0; color: var(--accent-2); font-family: Outfit, sans-serif; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">System Design · LinkedIn</p>
                <h4 style="margin: 0; color: var(--paper); font-size: 1.1rem; font-weight: 500; text-decoration: underline; text-underline-offset: 4px;">How I Designed Authentication for a FastAPI Application ↗</h4>
              </a>
              <a href="https://linkedin.com/in/ramesh988025" target="_blank" rel="noopener noreferrer" style="padding: 1.5rem; border: 1px solid rgba(242, 238, 229, 0.1); background: rgba(242, 238, 229, 0.02); display: block; text-decoration: none; transition: transform 0.2s ease, border-color 0.2s ease;">
                <p style="margin: 0 0 0.5rem 0; color: var(--accent-2); font-family: Outfit, sans-serif; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">Cybersecurity · LinkedIn</p>
                <h4 style="margin: 0; color: var(--paper); font-size: 1.1rem; font-weight: 500; text-decoration: underline; text-underline-offset: 4px;">Building a SIEM Detection Rule ↗</h4>
              </a>
            </div>
          </div>

        </div>"""
content = content.replace(github_old, github_new)

# 10. Certifications Empty Space Fix
# The CSS change already reduced min-height. I will make sure the scene inner isn't artificially spaced.
# It uses .editorial-stack which adds some gap, that is fine.

# 11. Rename portfolio.html references in sitemap
# We'll do this in bash, not here.

with open('portfolio.html', 'w') as f:
    f.write(content)

