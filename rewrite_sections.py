import re

with open('portfolio.html', 'r') as f:
    content = f.read()

start_idx = content.find('<section class="scene" id="skills"')
end_idx = content.find('<footer')

if start_idx == -1 or end_idx == -1:
    print("Could not find bounds")
    exit(1)

new_html = """
    <!-- TECH STACK & TOOLS -->
    <section class="scene" id="skills" aria-labelledby="skills-title">
      <div class="scene-inner wide">
        <div class="reveal" style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
          <div style="width: 8px; height: 8px; background: var(--accent); border-radius: 50%;"></div>
          <span style="color: var(--accent); font-family: 'Space Mono', monospace; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Tech Stack & Tools</span>
        </div>
        <h2 class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 8vw, 5rem); text-transform: capitalize; line-height: 0.9; margin-bottom: 4rem; letter-spacing: -0.02em;" id="skills-title">Where I am with each</h2>
        
        <div class="tech-grid reveal" style="display: flex; flex-wrap: wrap; gap: 2rem; margin-bottom: 4rem;">
          <div class="tech-circle" style="width: 140px; height: 140px; border-radius: 50%; background: var(--accent); color: white; display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; cursor: pointer; transition: transform 0.3s ease;">Languages</div>
          <div class="tech-circle" style="width: 140px; height: 140px; border-radius: 50%; border: 2px solid var(--line); color: var(--ink); display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease;">OS &<br>Systems</div>
          <div class="tech-circle" style="width: 140px; height: 140px; border-radius: 50%; border: 2px solid var(--line); color: var(--ink); display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease;">Networking</div>
          <div class="tech-circle" style="width: 140px; height: 140px; border-radius: 50%; border: 2px solid var(--line); color: var(--ink); display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease;">Security<br>Tools</div>
          <div class="tech-circle" style="width: 140px; height: 140px; border-radius: 50%; border: 2px solid var(--line); color: var(--ink); display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease;">Cloud</div>
          <div class="tech-circle" style="width: 140px; height: 140px; border-radius: 50%; border: 2px solid var(--line); color: var(--ink); display: flex; align-items: center; justify-content: center; text-align: center; font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease;">SIEM /<br>Detection</div>
        </div>

        <div class="tech-detail reveal system-frame" style="padding: 1.5rem 2rem; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--line); max-width: 800px; background: rgba(10,10,10,0.5);">
          <span style="font-family: 'Space Mono', monospace; font-size: 1.1rem; color: var(--ink);">Python — CS50 coursework</span>
          <span style="color: var(--accent); border: 1px solid var(--accent); padding: 0.4rem 0.8rem; font-family: 'Space Mono', monospace; font-size: 0.85rem; text-transform: uppercase;">IN PROGRESS</span>
        </div>
      </div>
    </section>

    <!-- TARGET CERTIFICATIONS & ROADMAP -->
    <section class="scene" id="certifications" aria-labelledby="roadmap-title">
      <div class="scene-inner wide">
        <div class="reveal" style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
          <div style="width: 8px; height: 8px; background: var(--accent); border-radius: 50%;"></div>
          <span style="color: var(--accent); font-family: 'Space Mono', monospace; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Target Certifications & Roadmap</span>
        </div>
        <h2 class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 8vw, 5rem); text-transform: capitalize; line-height: 0.9; margin-bottom: 4rem; letter-spacing: -0.02em;" id="roadmap-title">Where this is heading</h2>
        
        <div class="roadmap-carousel reveal" style="display: flex; gap: 2rem; overflow-x: auto; padding-bottom: 2rem; snap-type: x mandatory; scrollbar-width: none;">
          <div class="roadmap-card" style="min-width: 400px; padding: 2.5rem; border: 1px solid var(--line); background: rgba(10,10,10,0.5); scroll-snap-align: start;">
            <p style="color: var(--accent); font-family: 'Space Mono', monospace; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em; margin: 0 0 1rem;">SOC TRACK</p>
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.75rem; color: var(--ink); margin: 0 0 1.5rem;">SOC Level 1 → SOC Level 2</h3>
            <p style="color: var(--muted); line-height: 1.6; margin-bottom: 2rem;">Security Analyst foundation: SIEM, detection engineering, phishing analysis, network & endpoint monitoring, threat hunting, incident response.</p>
            <span style="border: 1px solid var(--line); color: var(--ink); padding: 0.5rem 1rem; font-family: 'Space Mono', monospace; font-size: 0.8rem;">NOT STARTED</span>
          </div>
          
          <div class="roadmap-card" style="min-width: 400px; padding: 2.5rem; border: 1px solid var(--line); background: rgba(10,10,10,0.5); scroll-snap-align: start;">
            <p style="color: var(--accent); font-family: 'Space Mono', monospace; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em; margin: 0 0 1rem;">SPECIALIZATION</p>
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.75rem; color: var(--ink); margin: 0 0 1.5rem;">Security Engineer:<br>Defending AWS</h3>
            <p style="color: var(--muted); line-height: 1.6; margin-bottom: 2rem;">The endgame stage. Cloud architecture security, IAM, container orchestration, infrastructure-as-code deployments.</p>
            <span style="border: 1px solid var(--line); color: var(--ink); padding: 0.5rem 1rem; font-family: 'Space Mono', monospace; font-size: 0.8rem;">NOT STARTED</span>
          </div>
        </div>
        
        <div class="carousel-dots" style="display: flex; justify-content: center; gap: 0.5rem; margin-top: 1rem;">
          <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--line);"></div>
          <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--accent);"></div>
          <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--line);"></div>
          <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--line);"></div>
        </div>
      </div>
    </section>

    <!-- EVIDENCE -->
    <section class="scene" id="github" aria-labelledby="evidence-title">
      <div class="scene-inner wide">
        <h2 class="section-title reveal" style="font-family: Outfit, sans-serif; font-weight: 800; font-size: clamp(3rem, 10vw, 6rem); text-transform: uppercase; line-height: 0.9; margin-bottom: 4rem; letter-spacing: -0.02em;" id="evidence-title">EVIDENCE.</h2>
        
        <div class="evidence-grid reveal" style="display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 5vw, 6rem);">
          <!-- Left: Open Source -->
          <div>
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.25rem; text-transform: uppercase; margin-bottom: 2rem; color: var(--ink);">Open Source & GitHub</h3>
            
            <div style="display: flex; flex-direction: column; gap: 1rem;">
              <article class="system-frame" style="padding: 1.5rem; border: 1px solid var(--line); background: rgba(10,10,10,0.5);">
                <h4 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 1.1rem;">Bunny/Synalytix</h4>
                <p style="margin: 0 0 1.5rem; color: var(--muted); font-size: 0.95rem; line-height: 1.5;">AI-powered personal analytics platform integrating development, productivity and career data.</p>
                <div style="display: flex; gap: 0.5rem;">
                  <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">TYPESCRIPT</span>
                  <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">PYTHON</span>
                </div>
              </article>
              
              <article class="system-frame" style="padding: 1.5rem; border: 1px solid var(--line); background: rgba(10,10,10,0.5);">
                <h4 style="margin: 0 0 0.5rem; color: var(--ink); font-size: 1.1rem;">Bunny/Antigravity</h4>
                <p style="margin: 0 0 1.5rem; color: var(--muted); font-size: 0.95rem; line-height: 1.5;">Offline-first learning and portfolio operating system.</p>
                <div style="display: flex; gap: 0.5rem;">
                  <span class="pill" style="min-height: 1.6rem; font-size: 0.65rem;">REACT</span>
                </div>
              </article>
            </div>
          </div>
          
          <!-- Right: Technical Writing -->
          <div>
            <h3 style="font-family: Outfit, sans-serif; font-size: 1.25rem; text-transform: uppercase; margin-bottom: 2rem; color: var(--ink);">Technical Writing</h3>
            
            <div style="display: flex; flex-direction: column; gap: 2rem;">
              <article style="border-bottom: 1px solid var(--line); padding-bottom: 1rem;">
                <p style="color: var(--accent); font-family: 'Space Mono', monospace; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; margin: 0 0 0.5rem;">SYSTEM DESIGN • 5 MIN READ</p>
                <h4 style="margin: 0; color: var(--ink); font-size: 1.1rem; font-weight: 400;">How I Designed Authentication for a FastAPI Application</h4>
              </article>
              
              <article style="border-bottom: 1px solid var(--line); padding-bottom: 1rem;">
                <p style="color: var(--accent); font-family: 'Space Mono', monospace; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; margin: 0 0 0.5rem;">CYBERSECURITY • 8 MIN READ</p>
                <h4 style="margin: 0; color: var(--ink); font-size: 1.1rem; font-weight: 400;">Building a SIEM Detection Rule</h4>
              </article>
            </div>
          </div>
        </div>
      </div>
    </section>

"""

new_content = content[:start_idx] + new_html + "\n    " + content[end_idx:]

with open('portfolio.html', 'w') as f:
    f.write(new_content)

