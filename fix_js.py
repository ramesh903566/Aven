with open('portfolio.html', 'r') as f:
    content = f.read()

# 1. Update sectionNavMap
navmap_old = """        const sectionNavMap = {
          work: "work",
          about: "about",
          projects: "projects",
          skills: "skills",
          security: "security",
          "security-labs": "security-labs",
          journey: "journey",
          person: "about",
          certifications: "journey",
          github: "journey"
        };"""

navmap_new = """        const sectionNavMap = {
          work: "work",
          about: "about",
          journey: "journey",
          projects: "projects",
          skills: "skills",
          security: "skills",
          "security-labs": "security-labs",
          certifications: "security-labs",
          github: "security-labs",
          contact: "contact"
        };"""

content = content.replace(navmap_old, navmap_new)

# 2. Update .reveal GSAP logic
reveal_old = """        gsap.utils.toArray(".reveal").forEach((item) => {
          gsap.from(item, {
            y: prefersReducedMotion ? 0 : 34,
            opacity: 0,
            duration: prefersReducedMotion ? 0.001 : 1,
            ease: "power3.out",
            scrollTrigger: {
              trigger: item,
              start: "top 84%",
              toggleActions: "play none none reverse"
            }
          });
        });"""

reveal_new = """        gsap.utils.toArray(".reveal").forEach((item) => {
          gsap.fromTo(item, 
            {
              y: prefersReducedMotion ? 0 : 34,
              autoAlpha: 0
            },
            {
              y: 0,
              autoAlpha: 1,
              duration: prefersReducedMotion ? 0.001 : 1,
              ease: "power3.out",
              scrollTrigger: {
                trigger: item,
                start: "top 84%",
                toggleActions: "play none none reverse"
              }
            }
          );
        });"""

content = content.replace(reveal_old, reveal_new)

with open('portfolio.html', 'w') as f:
    f.write(content)

