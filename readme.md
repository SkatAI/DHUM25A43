# sciencespo-dhum-slides

> Investigating with AI - Course slides using Marp

This repository contains Marp-based slides for the "Investigating with AI" course (DHUM25A43) at Sciences Po.

## Setup

1. Install Node.js and npm.
2. Install dependencies:
   ```bash
   npm install
   ```

## Building Slides

The main slide decks are located in the `slides/` directory.

### Generate HTML and PDF
Builds the slides for `01-welcome`.
```bash
npm run build
```

### Watch mode (auto-rebuild on changes)
```bash
npm run watch
```

### Serve all slides locally
This command starts a live-preview server for all slide decks in the `slides/` directory.
```bash
npm run serve
```

### Generate only HTML
```bash
npm run build:html
```

### Generate only PDF
```bash
npm run build:pdf
```

## Directory Structure

```
.
├── slides/
│   ├── 01-welcome/           # Session 1: Welcome & Introduction
│   │   └── 01-welcome.md     # Main slide deck
│   ├── themes/               # Custom Marp themes
│   │   └── sciencespo.css    # Course theme
│   └── exports/              # Generated HTML/PDF files
├── package.json          # Project configuration
└── readme.md             # This file
```

## Theme Features

The `sciencespo.css` theme used for the slides includes:
- Sciences Po color scheme
- Custom layouts for title slides
- Two-column layout support (`.columns` class)
- Highlight boxes (`.highlight` class)
- Note boxes (`.note` class)
- Centered content (`.center` class)
- Large text emphasis (`.large` class)

## Slide Syntax Examples

### Title Slide
```markdown
<!--
_class: title
_paginate: false
-->

# Course Title
## Subtitle
Date
```

### Two-Column Layout
```markdown
<div class="columns">
<div>
Left column content
</div>
<div>
Right column content
</div>
</div>
```

### Highlight Box
```markdown
<div class="highlight">
Important content here
</div>
```

### Images
To insert an image from the `img/` directory:
```markdown
![w:400 center](../img/image.png)
```

## Course Information

- **Course**: DHUM25A43 - Investigating with AI
- **Institution**: Sciences Po
- **Instructors**: Alexis Perrier, Andreï Mogoutov
- **Discord**: https://discord.gg/DDbh5AyHYH
