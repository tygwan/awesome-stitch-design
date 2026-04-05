# Getting Started with Google Stitch

New to Google Stitch? This guide covers everything you need to go from zero to your first AI-generated UI design.

## What is Google Stitch?

[Google Stitch](https://stitch.withgoogle.com) is an AI-powered UI design tool from Google Labs. Describe a user interface in plain language and Stitch generates a high-fidelity, production-quality design in seconds — powered by Gemini.

Whether you are a designer prototyping ideas, a developer building mockups, or someone with no design experience at all, Stitch makes it easy to create polished UI designs.

## How to Use Stitch

1. **Go to [stitch.withgoogle.com](https://stitch.withgoogle.com)**
2. **Sign in with your Google account**
3. **Create a new project** — Click the "New project" button to get started.
4. **Enter a text prompt** — Describe the UI you want. For example: *"A modern dashboard for a fitness tracking app with a sidebar navigation, daily activity chart, step counter card, and dark theme."*
5. **Generate and iterate** — Click generate. Review the result, then refine your prompt or use Stitch's built-in editing tools to adjust the design until you are satisfied.

## Stitch Input Methods

Stitch supports multiple ways to provide design input:

| Method | Description |
|---|---|
| **Text** | Describe your UI in natural language. This is the most common input method. |
| **Image** | Upload a screenshot or reference image as design inspiration. |
| **Sketch** | Upload a hand-drawn wireframe and Stitch converts it into a polished design. |
| **URL** | Provide a website URL and use it as a design reference. |

You can combine these methods. For example, upload a rough sketch and add a text prompt to guide the style.

## Tips for Writing Good Prompts

The quality of your output depends on the quality of your input. Here is what makes a great Stitch prompt:

### Be specific about layout and components

Vague prompts produce generic results. Instead of *"a landing page"*, try:

> A SaaS landing page with a sticky top navigation, hero section containing a bold headline, subtitle, email signup form with CTA button, product screenshot, trusted-by logo bar with 5 company logos, and a 3-column feature grid with icons.

### Mention the device type

Stitch can generate for different screen sizes. Specify whether you want a **desktop**, **tablet**, or **mobile** layout.

### Reference well-known design patterns

Use established UI terminology that Stitch understands:

- "Hero section", "card grid", "sticky nav", "sidebar layout"
- "Modal dialog", "bottom sheet", "tab bar", "breadcrumb navigation"
- "Glassmorphism", "neumorphism", "flat design", "material design"

### Include interaction details

Describe states and behaviors to get more realistic designs:

- "Active tab highlighted in blue"
- "Search bar with placeholder text 'Search products...'"
- "Toggle switch in the on state"

### Provide sample content

Real text and numbers produce more realistic designs than placeholder text. Include actual headlines, menu items, product names, and data values in your prompt.

## Example Prompt

> Design a mobile fitness app home screen. Dark background with vibrant accent colors. Top greeting "Good morning, Alex" with profile avatar. Daily step counter as a large circular progress ring showing 8,432 of 10,000 steps. Three horizontal activity cards for calories burned, active minutes, and heart rate. A weekly bar chart comparing daily activity. Bottom tab navigation with icons for Home, Workouts, Nutrition, and Profile. The Home tab should be active.

## Official Resources

- [Google Stitch](https://stitch.withgoogle.com) — The official Stitch app
- [Google Labs](https://labs.google.com) — Explore other Google AI experiments
- [Stitch SDK](https://github.com/google-labs-code/stitch-sdk) — Programmatic access to Stitch
- [Stitch MCP Server](https://github.com/davideast/stitch-mcp) — Community MCP integration

## Browse the Prompt Gallery

Looking for inspiration? The [Awesome Stitch Design Gallery](https://tygwan.github.io/awesome-stitch-design/) collects community-contributed prompts across categories like marketing pages, dashboards, e-commerce, and more. Each entry includes the full prompt text and a preview of the generated design.

Want to add your own? See [CONTRIBUTING.md](https://github.com/tygwan/awesome-stitch-design/blob/main/CONTRIBUTING.md) for how to submit a prompt in just 2 steps.
