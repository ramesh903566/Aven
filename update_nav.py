import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# Update Nav HTML
old_nav = """  <nav class="site-nav" aria-label="Primary navigation">
    <a href="#work">Home</a>
    <a href="#about">About</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#security">Security</a>
    <a href="#journey">Experience</a>
    <a href="#contact">Contact</a>
  </nav>"""

new_nav = """  <nav class="site-nav" aria-label="Primary navigation">
    <a href="#work">Home</a>
    <a href="#about">About</a>
    <a href="#journey">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#certifications">Roadmap</a>
    <a href="#github">Evidence</a>
    <a href="#contact">Contact</a>
  </nav>"""

content = content.replace(old_nav, new_nav)

# Update sectionNavMap
old_map = """        const sectionNavMap = {
          "security-labs": "security",
          person: "about",
          certifications: "journey",
          github: "journey"
        };"""

new_map = """        const sectionNavMap = {
          person: "about"
        };"""

content = content.replace(old_map, new_map)

with open('portfolio.html', 'w') as f:
    f.write(content)

