---
marp: false
---

# DHUM25A43 Course Slides

This directory contains Marp-based slides for the "Investigating with AI" course.

## Setup

1. Install Node.js and npm
2. Install dependencies:
   ```bash
   npm install
   ```

## Building Slides

### Generate HTML and PDF
```bash
npm run build
```

### Watch mode (auto-rebuild on changes)
```bash
npm run watch
```

### Serve slides locally
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
slides/
├── 01-welcome/           # Session 1: Welcome & Introduction
│   └── 01-welcome.md     # Main slide deck
├── themes/               # Custom Marp themes
│   └── sciencespo.css    # Course theme
├── exports/              # Generated HTML/PDF files
└── README.md            # This file
```

## Theme Features

The `sciencespo.css` theme includes:
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
```markdown
![w:400 center](../../img/image.png)
```

## Course Information

- **Course**: DHUM25A43 - Investigating with AI
- **Institution**: Sciences Po
- **Instructors**: Alexis Perrier, Andreï Mogoutov
- **Discord**: https://discord.gg/DDbh5AyHYH