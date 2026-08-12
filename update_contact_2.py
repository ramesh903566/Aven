import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# 1. Remove Evidence Section
# First, let's find the boundaries more accurately.
start_github = content.find('<section class="scene" id="github"')
end_github = content.find('<!-- CONTACT -->')
if end_github == -1:
    end_github = content.find('<section class="scene contact" id="contact"')

if start_github != -1 and end_github != -1:
    content = content[:start_github] + content[end_github:]

# 2. Remove Evidence from Nav
content = content.replace('<a href="#github">Evidence</a>\n', '')
content = content.replace('<a href="#github">Evidence</a>', '')

# 3. Update Contact Section
content = re.sub(
    r'<a href="mailto:[^"]*" class="contact-link magnetic"[^>]*>Email —</a>',
    r'''<div class="email-container magnetic" style="display: inline-flex; align-items: center; border: 1px solid rgba(255,255,255,0.1); padding: 1rem 2rem; color: var(--paper); font-family: 'Space Mono', monospace; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; transition: all 0.3s ease;">
            <span id="email-trigger" style="cursor: pointer;">EMAIL —</span>
            <span id="email-text" style="display: none; color: var(--accent); margin-left: 1rem; padding-left: 1rem; border-left: 1px solid rgba(255,255,255,0.1); text-transform: lowercase;">ramesh@example.com</span>
            <button id="copy-btn" style="display: none; background: transparent; border: none; cursor: pointer; color: var(--muted); margin-left: 0.5rem; align-items: center; justify-content: center;" title="Copy to clipboard">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: stroke 0.3s ease;">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
              </svg>
            </button>
          </div>''',
    content
)

# 4. Update LinkedIn
content = content.replace('https://linkedin.com/in/ramesh', 'https://linkedin.com/in/ramesh988025')

# 5. Add JS for the Email interaction
js_snippet = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          const emailTrigger = document.getElementById('email-trigger');
          const emailText = document.getElementById('email-text');
          const copyBtn = document.getElementById('copy-btn');
          
          if (emailTrigger && emailText && copyBtn) {
            emailTrigger.addEventListener('click', () => {
              emailText.style.display = 'inline-block';
              copyBtn.style.display = 'inline-flex';
            });
            
            copyBtn.addEventListener('click', () => {
              navigator.clipboard.writeText('ramesh@example.com').then(() => {
                const svg = copyBtn.querySelector('svg');
                svg.style.stroke = 'var(--accent)';
                setTimeout(() => {
                  svg.style.stroke = 'currentColor';
                }, 2000);
              });
            });
          }
        });
      </script>
"""
if 'email-trigger' not in content:
    content = content.replace('</body>', js_snippet + '\n</body>')

with open('portfolio.html', 'w') as f:
    f.write(content)
