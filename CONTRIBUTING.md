# Contributing to Awesome Stitch Design

Thank you for your interest in contributing! This project curates the best Google Stitch design prompts and resources in one place.

There are two ways to contribute: **Pull Request** (preferred) or **Issue**.

---

## Option 1: Pull Request (Preferred)

Contributing a prompt requires editing just **2 files**. CI handles everything else.

### Step 1: Fork the repo

Fork [tygwan/awesome-stitch-design](https://github.com/tygwan/awesome-stitch-design) and clone your fork locally.

### Step 2: Add one line to README.md

Find the correct category and subcategory in `README.md` and add your entry:

```markdown
- [Your Title](https://tygwan.github.io/awesome-stitch-design/#your-slug) - Short description of the design.
```

**Slug rules:** lowercase, hyphens instead of spaces, no special characters.

| Original title | Slug |
|---|---|
| SaaS Product Landing | `saas-product-landing` |
| E-Commerce Dashboard | `e-commerce-dashboard` |
| Mobile Fitness App | `mobile-fitness-app` |

### Step 3: Add a preview screenshot

Save your Stitch-generated screenshot to:

```
previews/{category}/{your-slug}.png
```

**Category folders:**

| Category | Folder |
|---|---|
| Prompts: Marketing and Public | `marketing` |
| Prompts: Product and App | `product` |
| Prompts: Commerce | `commerce` |
| Prompts: Utility | `utility` |
| Prompts: Admin | `admin` |

Recommended: **1280px width**, PNG format.

### Step 4: Submit your PR

Push your branch and open a pull request. That's it — only 2 files.

### What happens next

- CI runs **awesome-lint** to validate your README entry format.
- After merge, CI **auto-generates `prompts.json`** from README so the gallery stays in sync.
- Your **GitHub profile** (as the PR author) is automatically displayed as the contributor in the gallery.

> **You do not need to edit** `prompts.json`, `index.html`, `metadata.json`, or any other file.

> **Note:** A maintainer may add supplementary metadata (device, featured, discussionNumber) in `metadata.json` after your PR is merged.

---

## Option 2: Submit via Issue

Prefer not to deal with git? Use the issue template and a maintainer will add it for you:

[Submit a resource via Issue](https://github.com/tygwan/awesome-stitch-design/issues/new?template=submit-resource.yml)

---

## Adding a Resource (Non-Prompt)

For non-prompt resources such as tutorials, tools, or articles, just add a line to the appropriate resource section in `README.md`:

```markdown
- [Resource Title](https://example.com) - Brief description.
```

No preview image is needed for resource contributions.

---

## Quality Standards

- **Original or properly attributed** — Do not submit others' work without credit.
- **Working links** — All URLs must be accessible.
- **English descriptions** — Descriptions should be in English.
- **SFW content only** — No inappropriate content.
- **Tested prompts** — Prompts must produce meaningful results in Stitch.

---

## Pull Request Checklist

- [ ] Added one line to README.md in the correct category
- [ ] Preview screenshot added to `previews/{category}/{slug}.png`
- [ ] Followed awesome list format: `- [Title](url) - Description.`

---

## Questions?

Feel free to [open an issue](https://github.com/tygwan/awesome-stitch-design/issues) if you have any questions.
