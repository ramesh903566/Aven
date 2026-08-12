import re
with open('portfolio.html', 'r') as f:
    content = f.read()

# Replace footer text if it's not exactly that
old_footer_pattern = r'<footer.*?</footer>'
new_footer = """
  <footer class="site-footer" style="padding: 2rem 0; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 4rem;">
    <p style="color: var(--dim); font-family: 'Space Mono', monospace; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; margin: 0;">&copy; 2026 RAMESH. BUILT WITH INTENTION.</p>
  </footer>
"""
content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)

with open('portfolio.html', 'w') as f:
    f.write(content)

