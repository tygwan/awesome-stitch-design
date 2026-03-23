# Contributing to Awesome Stitch Design

Thank you for your interest in contributing! This project collects the best Google Stitch design prompts and resources.

## How to Contribute

### Option 1: Pull Request (Preferred)

1. Fork this repository
2. Add your prompt to `README.md` and the gallery (`docs/index.html`)
3. Add a preview screenshot to `docs/previews/{category}/`
4. Submit a Pull Request

### Option 2: Issue

[Submit a resource via Issue](https://github.com/tygwan/awesome-stitch-design/issues/new?template=submit-resource.yml) and we'll add it for you.

## Adding a Design Prompt

Contributing a prompt requires 3 files:

### Step 1: Add to README.md

Add your prompt under the correct category/subcategory:

```markdown
- **Your Title** - `Your detailed Stitch prompt text here` — Brief description of the result.
```

Categories: Marketing & Public, Product & App, Commerce, Utility, Admin.

### Step 2: Add a preview image

1. Generate your design in [Google Stitch](https://stitch.withgoogle.com)
2. Download the screenshot (1280px width recommended)
3. Save to `docs/previews/{category}/your-filename.png`

Category folders: `marketing`, `product`, `commerce`, `utility`, `admin`

### Step 3: Add a gallery card

In `docs/index.html`, find the `const cards = [...]` array and add your entry:

```javascript
{
  id: 'your-unique-id',
  title: 'Your Title',
  description: 'Brief description of the result.',
  prompt: 'Your full Stitch prompt text...',
  image: 'previews/{category}/your-filename.png',
  category: 'marketing', // or product, commerce, utility, admin
  device: 'Desktop',     // or Mobile
  discussionNumber: null, // maintainer will create the Discussion
  featured: false,
  contributor: { username: 'your-github-username', name: 'Your Name' }
}
```

> The maintainer will create a GitHub Discussion for voting and assign the `discussionNumber` after merging.

## Adding a Resource Link

For non-prompt resources (tutorials, tools, articles), add to the appropriate section in `README.md`:

```markdown
- [Resource Title](https://example.com) - Brief description of the resource.
```

Keep entries in alphabetical order within resource sections.

## Quality Standards

- **Original or properly attributed** — Do not submit others' work without credit.
- **Working links** — All URLs must be accessible.
- **English descriptions** — Descriptions should be in English.
- **SFW content only** — No inappropriate content.
- **Tested prompts** — Prompts must produce meaningful results in Stitch.

## Pull Request Checklist

- [ ] The resource/prompt is related to Google Stitch
- [ ] Preview screenshot is included (for prompts)
- [ ] Gallery card entry added to `docs/index.html` (for prompts)
- [ ] Format guidelines are followed
- [ ] Entry is in the correct category

## Questions?

Feel free to [open an issue](https://github.com/tygwan/awesome-stitch-design/issues) if you have any questions.
