# Awesome Stitch Design [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![GitHub stars](https://img.shields.io/github/stars/tygwan/awesome-stitch-design?style=social)](https://github.com/tygwan/awesome-stitch-design)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A curated list of awesome design prompts, resources, tutorials, and tools for [Google Stitch](https://stitch.withgoogle.com) — the AI-powered UI design tool by Google Labs.

Google Stitch lets you generate high-fidelity UI designs from text prompts, voice input, or hand-drawn sketches, powered by Gemini. This list collects the best prompts, examples, and resources to help you master "vibe design."

## Contents

- [Official Resources](#official-resources)
- [Prompts](#prompts)
  - [Mobile App UI](#mobile-app-ui)
  - [Web App UI / Landing Page](#web-app-ui--landing-page)
  - [Dashboard / Admin](#dashboard--admin)
  - [E-commerce](#e-commerce)
  - [Social Media](#social-media)
- [Sketch to Design](#sketch-to-design)
- [Tutorials & Guides](#tutorials--guides)
- [SDK & MCP](#sdk--mcp)
- [Tools & Extensions](#tools--extensions)
- [Articles & Blog Posts](#articles--blog-posts)
- [Videos](#videos)
- [Community](#community)

## Official Resources

- [Stitch](https://stitch.withgoogle.com) - Official Stitch app by Google Labs.
- [Stitch Prompt Guide](https://discuss.ai.google.dev/t/stitch-prompt-guide/83844) - Official prompting guide on Google AI Developers Forum.
- [Introducing Stitch](https://developers.googleblog.com/stitch-a-new-way-to-design-uis/) - Original announcement blog post (May 2025).
- [Stitch AI UI Design](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/) - Major redesign announcement blog post (March 2026).
- [Stitch SDK](https://github.com/google-labs-code/stitch-sdk) - Official SDK for programmatic access (`@google/stitch-sdk`).
- [Stitch MCP Setup](https://stitch.withgoogle.com/docs/mcp/setup) - Official MCP server documentation for editor integration.
- [Design-to-Code Codelab](https://codelabs.developers.google.com/design-to-code-with-antigravity-stitch?hl=en) - Google Codelabs tutorial: Design-to-Code with Antigravity and Stitch MCP.

## Prompts

### Mobile App UI

- **Fitness Tracker Home** - `Design a modern fitness tracking app home screen with daily step count ring, heart rate monitor, weekly activity chart, and quick-start workout buttons. Use a dark theme with vibrant accent colors.` — A high-energy dark-mode dashboard with neon accents, progress rings, and real-time health stats. [Preview](https://stitch.withgoogle.com/project/3282504411478314944)
- **Recipe App** - `Design a recipe app home screen with a search bar, trending recipes carousel, meal categories with icons, and a bottom navigation bar. Use warm, appetizing colors with food photography placeholders.` — A warm, inviting food app with carousel cards and visual category browsing.
- **Travel Booking** - `Design a travel booking app screen showing destination cards with hero images, price tags, star ratings, date picker, and a floating search FAB. Use a clean white design with blue accents.` — A polished travel app with immersive destination imagery and clear booking CTAs.

### Web App UI / Landing Page

- **AI Writing Tool Landing Page** - `Design a SaaS landing page for an AI writing assistant tool. Include a hero section with headline, subheadline, CTA button, feature grid with icons, pricing comparison table, and testimonial cards. Clean, modern design with a blue and white color scheme.` — A conversion-optimized landing page with clear visual hierarchy and pricing tiers. [Preview](https://stitch.withgoogle.com/project/3282504411478314944)
- **Portfolio Website** - `Design a creative portfolio landing page for a UI/UX designer. Include a large hero with animated text, a project showcase grid with hover effects, an about section with photo, and a contact form. Use a minimal black and white theme with one accent color.` — A bold designer portfolio with editorial typography and hover-reveal project cards.

### Dashboard / Admin

- **SaaS Analytics Dashboard** - `Design a real-time analytics dashboard for a SaaS product. Include KPI cards with sparklines, a large area chart showing monthly revenue, a donut chart for user segments, a data table with sortable columns, and a sidebar navigation. Use a clean white background with subtle shadows.` — A data-rich admin panel with well-organized metrics, charts, and table views. [Preview](https://stitch.withgoogle.com/project/3282504411478314944)
- **Project Management Board** - `Design a Kanban-style project management dashboard with columns for To Do, In Progress, and Done. Each card shows task title, assignee avatar, priority tag, and due date. Include a top bar with filters and a create task button.` — A clean task board with draggable card layout and status columns.

### E-commerce

- **Sneaker Product Page** - `Design a premium e-commerce product detail page for a pair of sneakers. Include a large product image gallery with thumbnails, product title, price, color/size selectors, add to cart button, product description tabs, and customer review section. Modern minimal style.` — A high-end product page with image gallery, variant selectors, and social proof. [Preview](https://stitch.withgoogle.com/project/3282504411478314944)
- **Grocery Delivery App** - `Design a grocery delivery app home screen with a search bar, promotional banner, product categories with icons, featured deals section with discount badges, and a cart summary floating bar at the bottom. Fresh green color palette.` — A fresh, organized grocery shopping experience with deals and quick category access.

### Social Media

- **Photo-Sharing Profile** - `Design a social media profile page similar to Instagram. Include a profile header with avatar, follower/following counts, bio section, story highlights row, and a grid of photo posts. Light theme with clean typography.` — A polished profile page with stats, stories, and photo grid layout. [Preview](https://stitch.withgoogle.com/project/3282504411478314944)
- **Messaging App Chat** - `Design a messaging app chat screen with a conversation thread showing text bubbles, image messages, emoji reactions, a typing indicator, and a message input bar with attachment and voice buttons. Use a soft purple gradient header.` — A modern chat interface with rich media support and expressive interactions.

## Sketch to Design

*Stitch can transform hand-drawn sketches into polished UI designs. Upload a photo of your sketch and Stitch will generate a high-fidelity version.*

> **Tip:** For best results, draw clear wireframes with labeled elements. Stitch interprets layout structure, component types, and annotations.

## Tutorials & Guides

- [Google Stitch Tutorial: AI-Powered UI Design Tool](https://www.codecademy.com/article/google-stitch-tutorial-ai-powered-ui-design-tool) - Step-by-step guide for designing mobile app UI with Stitch (Codecademy).

## SDK & MCP

- [Stitch SDK](https://github.com/google-labs-code/stitch-sdk) - Official Node.js SDK for generating screens, editing, creating variants, and extracting HTML/screenshots.
- [Stitch MCP Server (Community)](https://github.com/davideast/stitch-mcp) - Community-built MCP server for integrating Stitch with Claude Code, Cursor, and other editors.

## Tools & Extensions

- [Stitch Figma Plugin](https://www.figma.com/community/plugin/stitch) - Import Stitch designs directly into Figma projects.
- [Antigravity](https://labs.google/antigravity) - Google Labs tool that pairs with Stitch for design-to-code workflows.

## Articles & Blog Posts

- [Google Stitch Complete Guide](https://www.nxcode.io/resources/news/google-stitch-complete-guide-vibe-design-2026) - Comprehensive guide covering all Stitch features (NxCode).
- [Google Stitch: A Product Designer's Review](https://www.bitovi.com/blog/google-stitch-a-product-designers-review) - In-depth review from a designer's perspective (Bitovi).
- [Google Stitch AI Review for UI Designers](https://www.index.dev/blog/google-stitch-ai-review-for-ui-designers) - Review focused on practical design workflows (Index.dev).
- [Google Stitch vs v0 vs Lovable](https://www.nxcode.io/resources/news/google-stitch-vs-v0-vs-lovable-ai-app-builder-2026) - Comparison of AI app builder tools (NxCode).

## Videos

- [Google Stitch: AI UI Design in Minutes](https://www.youtube.com/results?search_query=google+stitch+ui+design) - Search for the latest Stitch tutorials and demos on YouTube.

## Community

- [Google AI Developers Forum - Stitch](https://discuss.ai.google.dev/tag/stitch) - Official discussion forum for Stitch on Google AI Developers.
- [r/GoogleStitch](https://www.reddit.com/r/GoogleStitch/) - Reddit community for sharing Stitch designs and tips.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first. You can also [submit a resource via Issue](https://github.com/tygwan/awesome-stitch-design/issues/new?template=submit-resource.yml).

## License

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
