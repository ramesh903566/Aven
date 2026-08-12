import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# Find the start of #projects
start_idx = content.find('<section class="scene" id="projects" aria-labelledby="projects-title">')
if start_idx == -1:
    print("Could not find #projects")
    exit(1)

# Find the end of #projects (next section)
end_idx = content.find('<section class="scene" id="skills"', start_idx)
if end_idx == -1:
    print("Could not find end of #projects")
    exit(1)

new_projects_html = """    <section class="scene" id="projects" aria-labelledby="projects-title">
      <div class="scene-inner wide">
        <h2 class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 10vw, 6rem); text-transform: uppercase; line-height: 0.9; margin-bottom: 3rem; letter-spacing: -0.02em;" id="projects-title">EVIDENCE.</h2>
        
        <div class="project-viewer reveal" style="display: grid; grid-template-columns: minmax(280px, 1fr) minmax(320px, 2fr); gap: clamp(2rem, 4vw, 4rem); align-items: start;">
          
          <!-- Tabs List -->
          <div class="project-tabs" style="display: flex; flex-direction: column; gap: 1rem;">
            <button class="project-tab is-active" data-target="proj-synalytix" style="text-align: left; background: transparent; border: 1px solid var(--accent); padding: 1.5rem; color: var(--ink); cursor: pointer; transition: all 0.3s ease;">
              <h3 style="margin: 0 0 0.5rem; font-size: 1.25rem; font-family: Outfit, sans-serif;">Bunny/Synalytix</h3>
              <p style="margin: 0; font-size: 0.9rem; color: var(--muted);">AI-powered personal analytics platform.</p>
            </button>
            <button class="project-tab" data-target="proj-antigravity" style="text-align: left; background: transparent; border: 1px solid rgba(255,255,255,0.1); padding: 1.5rem; color: var(--muted); cursor: pointer; transition: all 0.3s ease;">
              <h3 style="margin: 0 0 0.5rem; font-size: 1.25rem; font-family: Outfit, sans-serif;">Bunny/Antigravity</h3>
              <p style="margin: 0; font-size: 0.9rem;">Offline-first learning and portfolio OS.</p>
            </button>
            <button class="project-tab" data-target="proj-stock" style="text-align: left; background: transparent; border: 1px solid rgba(255,255,255,0.1); padding: 1.5rem; color: var(--muted); cursor: pointer; transition: all 0.3s ease;">
              <h3 style="margin: 0 0 0.5rem; font-size: 1.25rem; font-family: Outfit, sans-serif;">Stock Market System</h3>
              <p style="margin: 0; font-size: 0.9rem;">DBMS for financial data.</p>
            </button>
            <button class="project-tab" data-target="proj-horologium" style="text-align: left; background: transparent; border: 1px solid rgba(255,255,255,0.1); padding: 1.5rem; color: var(--muted); cursor: pointer; transition: all 0.3s ease;">
              <h3 style="margin: 0 0 0.5rem; font-size: 1.25rem; font-family: Outfit, sans-serif;">HOROLOGIUM</h3>
              <p style="margin: 0; font-size: 0.9rem;">Watch encyclopedia reference.</p>
            </button>
          </div>

          <!-- Project Details -->
          <div class="project-content-area system-frame" style="padding: 2rem; min-height: 500px; background: rgba(10,10,10,0.5);">
            
            <!-- Synalytix -->
            <div id="proj-synalytix" class="project-pane" style="display: block;">
              <div class="project-thumbnail" style="width: 100%; height: 240px; background: #111; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem; display: flex; align-items: center; justify-content: center; color: var(--muted);">
                [ Project Preview / Thumbnail ]
              </div>
              <h3 style="font-family: Outfit, sans-serif; font-size: 2rem; margin: 0 0 1rem; color: var(--ink);">Synalytix</h3>
              <p style="color: var(--paper); line-height: 1.6; margin-bottom: 1.5rem;">An AI-powered personal analytics platform that unifies coding, productivity, career, and social-media data into one intelligent dashboard.</p>
              
              <div style="margin-bottom: 1.5rem;">
                <h4 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">Architecture</h4>
                <p style="margin: 0; color: var(--muted); font-size: 0.9rem;">React, TypeScript, Tailwind, FastAPI, PostgreSQL, Redis, Celery, Docker.</p>
              </div>
              
              <div style="margin-bottom: 1.5rem;">
                <h4 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">Status</h4>
                <p style="margin: 0; color: var(--accent); font-weight: 700; font-size: 0.9rem; padding: 0.5rem 1rem; border: 1px solid var(--accent); display: inline-block;">IN PROGRESS / PRODUCTION-VALIDATION STAGE</p>
              </div>
              
              <a href="https://github.com/ramesh903566/Synalytix" target="_blank" class="text-link">GitHub Repository</a>
            </div>

            <!-- Antigravity -->
            <div id="proj-antigravity" class="project-pane" style="display: none;">
              <div class="project-thumbnail" style="width: 100%; height: 240px; background: #111; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem; display: flex; align-items: center; justify-content: center; color: var(--muted);">
                [ Antigravity Preview ]
              </div>
              <h3 style="font-family: Outfit, sans-serif; font-size: 2rem; margin: 0 0 1rem; color: var(--ink);">Antigravity</h3>
              <p style="color: var(--paper); line-height: 1.6; margin-bottom: 1.5rem;">Offline-first learning and portfolio operating system for notes, resources, commands, code snippets, project tracking, Kanban, import/export, and full-text search.</p>
              
              <div style="margin-bottom: 1.5rem;">
                <h4 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">Tech Stack</h4>
                <div style="display: flex; gap: 0.5rem;"><span class="pill">React</span><span class="pill">SQLite</span><span class="pill">Electron</span></div>
              </div>
            </div>

            <!-- Stock Market -->
            <div id="proj-stock" class="project-pane" style="display: none;">
              <div class="project-thumbnail" style="width: 100%; height: 240px; background: #111; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem; display: flex; align-items: center; justify-content: center; color: var(--muted);">
                [ Stock Market DB Preview ]
              </div>
              <h3 style="font-family: Outfit, sans-serif; font-size: 2rem; margin: 0 0 1rem; color: var(--ink);">Stock Market & Portfolio Management System</h3>
              <p style="color: var(--paper); line-height: 1.6; margin-bottom: 1.5rem;">Academic DBMS project for managing stocks, portfolios, transactions, and related financial data.</p>
              <div style="margin-bottom: 1.5rem;">
                <h4 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">Tech Stack</h4>
                <div style="display: flex; gap: 0.5rem;"><span class="pill">MariaDB / SQL</span><span class="pill">Python</span></div>
              </div>
            </div>

            <!-- Horologium -->
            <div id="proj-horologium" class="project-pane" style="display: none;">
              <div class="project-thumbnail" style="width: 100%; height: 240px; background: #111; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem; display: flex; align-items: center; justify-content: center; color: var(--muted);">
                [ Horologium Preview ]
              </div>
              <h3 style="font-family: Outfit, sans-serif; font-size: 2rem; margin: 0 0 1rem; color: var(--ink);">HOROLOGIUM</h3>
              <p style="color: var(--paper); line-height: 1.6; margin-bottom: 1.5rem;">Watch encyclopedia and educational reference. Currently in development.</p>
              <div style="margin-bottom: 1.5rem;">
                <h4 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">Tech Stack</h4>
                <div style="display: flex; gap: 0.5rem;"><span class="pill">React</span><span class="pill">IN PROGRESS</span></div>
              </div>
              <a href="https://github.com/ramesh903566/HOROLOGIUM-" target="_blank" class="text-link">GitHub Repository</a>
            </div>

          </div>
        </div>
      </div>
      
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          const tabs = document.querySelectorAll('.project-tab');
          const panes = document.querySelectorAll('.project-pane');
          
          tabs.forEach(tab => {
            tab.addEventListener('click', () => {
              // Reset all
              tabs.forEach(t => {
                t.classList.remove('is-active');
                t.style.borderColor = 'rgba(255,255,255,0.1)';
                t.style.color = 'var(--muted)';
              });
              panes.forEach(p => p.style.display = 'none');
              
              // Activate clicked
              tab.classList.add('is-active');
              tab.style.borderColor = 'var(--accent)';
              tab.style.color = 'var(--ink)';
              
              const targetId = tab.getAttribute('data-target');
              const targetPane = document.getElementById(targetId);
              if (targetPane) {
                targetPane.style.display = 'block';
                if (window.gsap) {
                  gsap.fromTo(targetPane, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" });
                }
              }
            });
          });
        });
      </script>
    </section>
"""

new_content = content[:start_idx] + new_projects_html + "\n" + content[end_idx:]

with open('portfolio.html', 'w') as f:
    f.write(new_content)

