import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# Apply a brutalist border to the project-study class
old_proj = """    .project-study {
      display: grid;
      grid-template-columns: minmax(0, 0.9fr) minmax(22rem, 1.1fr);
      gap: clamp(2rem, 5vw, 5rem);
      align-items: start;
    }"""

new_proj = """    .project-study {
      display: grid;
      grid-template-columns: minmax(0, 0.9fr) minmax(22rem, 1.1fr);
      gap: clamp(2rem, 5vw, 5rem);
      align-items: start;
      border: 1px solid var(--line);
      padding: clamp(2rem, 5vw, 4rem);
      background: rgba(10, 10, 10, 0.5);
    }"""

content = content.replace(old_proj, new_proj)

with open('portfolio.html', 'w') as f:
    f.write(content)
