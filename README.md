# My Smarter Home LLC Website

This repository contains the marketing website for My Smarter Home Services, LLC. The site is built with Flask and Tailwind CSS and now mirrors the comprehensive `outline_docs/homepage_example.html` reference for the homepage.

## Getting Started

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the development server**
   ```bash
   flask --app app.py --debug run
   ```
3. **Open the site** at http://127.0.0.1:5000/.

## Homepage parity with the reference design

The `/` route has been rebuilt to include every section, data point, and interaction described in `outline_docs/homepage_example.html`, including:

- Split hero with credential badges, modal scheduling CTA, and quick service chips.
- Trust ribbon badges with tooltips, quote starter issue cards, and detailed service menus for electrical, plumbing, remodeling, and smart home bundles.
- Interactive elements such as bundle pricing, before/after sliders, review filtering, service-area chips, availability timeline toggles, FAQ accordion, and copy-link helpers.
- Fully sourced imagery using reliable Unsplash URLs and JSON-LD metadata that matches the reference document.

All interactive components are powered with lightweight inline JavaScript within the template so no additional build tooling is required.

## Project structure highlights

- `app/main/templates/base.html` – shared layout, navigation, and footer.
- `app/main/templates/home.html` – homepage matching the reference example.
- `outline_docs/homepage_example.html` – authoritative design reference used for parity.

## Contributing

1. Create a new branch for your change.
2. Run formatting or linting tools if applicable.
3. Open a pull request describing the update and any testing performed.
