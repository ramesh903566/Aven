import re

with open('portfolio.html', 'r') as f:
    content = f.read()

# Remove CharacterSequence class entirely
content = re.sub(r'class CharacterSequence \{.*?\n      \}\n', '', content, flags=re.DOTALL)

# Remove portfolioData entirely
content = re.sub(r'const portfolioData = \{.*?\};\n', '', content, flags=re.DOTALL)

# Remove sequence instantiation and createSkillOrbit
remove_block = """      const loader = document.getElementById("loader");
      const loaderPercent = document.getElementById("loader-percent");
      const loaderProgress = document.getElementById("loader-progress");
      const canvas = document.getElementById("character-canvas");
      const sequence = new CharacterSequence({
        canvas,
        frameCount: portfolioData.frames.count,
        currentFrame: portfolioData.frames.path,
        criticalCount: portfolioData.frames.criticalCount,
        onProgress: (value) => {
          const percent = Math.min(100, Math.round(value * 100));
          loaderPercent.textContent = `${String(percent).padStart(2, "0")}%`;
          loaderProgress.style.width = `${percent}%`;
        }
      });

      function createSkillOrbit() {
        const orbit = document.getElementById("skill-orbit");
        const count = portfolioData.skills.length;
        portfolioData.skills.forEach((skill, index) => {
          const token = document.createElement("span");
          token.className = "skill-token magnetic";
          token.textContent = skill.name;
          token.title = `${skill.name}: ${skill.status}`;
          token.setAttribute("aria-label", `${skill.name}: ${skill.status}`);
          const angle = (index / count) * 360;
          const radius = index % 3 === 0 ? "15.2rem" : index % 3 === 1 ? "12rem" : "8.7rem";
          token.style.setProperty("--angle", `${angle}deg`);
          token.style.setProperty("--radius", radius);
          token.style.setProperty("--mobile-radius", index % 3 === 0 ? "9.5rem" : "7rem");
          orbit.appendChild(token);
        });
      }"""

new_block = """      const loader = document.getElementById("loader");
      const loaderPercent = document.getElementById("loader-percent");
      const loaderProgress = document.getElementById("loader-progress");"""

content = content.replace(remove_block, new_block)

# Remove call to createSkillOrbit()
content = content.replace("      createSkillOrbit();\n", "")

# Remove skill-token gsap animation because the tokens are gone
gsap_skill_old = """        gsap.to(".skill-token", {
          y: prefersReducedMotion ? 0 : -8,
          duration: 2.4,
          repeat: -1,
          yoyo: true,
          ease: "sine.inOut",
          stagger: { each: 0.08, from: "random" },
          scrollTrigger: {
            trigger: "#skills",
            start: "top bottom",
            end: "bottom top",
            toggleActions: "play pause resume pause"
          }
        });"""
content = content.replace(gsap_skill_old, "")

with open('portfolio.html', 'w') as f:
    f.write(content)

