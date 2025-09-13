# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Ascend Creatives is a Mumbai-Goa based design boutique's static website showcasing their services in branding, packaging, and graphic design. The site features motion graphics, social media content, digital/print design, and website design services.

## Development Setup

This is a static HTML/CSS/JavaScript website with SCSS compilation. The project follows a traditional web structure without modern build tools or package managers.

### Key Technologies
- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **Styling**: SCSS/Sass for CSS preprocessing
- **JavaScript Libraries**: jQuery, Bootstrap, Owl Carousel, Magnific Popup, Masonry, Mixitup
- **Fonts**: Google Fonts (Play, Josefin Sans)

## File Structure and Architecture

```
/
├── index.html              # Homepage
├── about.html              # About page
├── portfolio.html          # Portfolio showcase
├── services.html           # Services page
├── contact.html            # Contact page
├── blog.html               # Blog listing
├── blog-details.html       # Blog detail page
├── somesh.html             # Custom page
├── css/                    # Compiled CSS files
│   ├── style.css           # Main compiled stylesheet
│   └── [vendor libraries]  # Bootstrap, FontAwesome, etc.
├── sass/                   # SCSS source files
│   ├── style.scss          # Main SCSS entry point
│   ├── _variable.scss      # Color and font variables
│   ├── _base.scss          # Base styles
│   ├── _header.scss        # Header component styles
│   ├── _home-page.scss     # Homepage specific styles
│   ├── _about.scss         # About page styles
│   ├── _services.scss      # Services page styles
│   ├── _portfolio.scss     # Portfolio page styles
│   ├── _contact.scss       # Contact page styles
│   ├── _blog.scss          # Blog styles
│   ├── _footer.scss        # Footer styles
│   └── _responsive.scss    # Media queries
├── js/                     # JavaScript files
│   ├── main.js             # Custom JavaScript functionality
│   └── [vendor libraries]  # jQuery, Bootstrap, plugins
├── img/                    # Images organized by page/component
└── fonts/                  # Web fonts
```

## Development Commands

### SCSS Compilation
Since there's no build system configured, SCSS files need manual compilation:

```bash
# Watch for SCSS changes and compile automatically
sass --watch sass:css

# Compile SCSS to CSS (one-time)
sass sass/style.scss css/style.css

# Compile with compressed output for production
sass sass/style.scss css/style.css --style compressed
```

### Local Development Server
```bash
# Python 3 simple server
python -m http.server 8000

# Python 2 alternative
python -m SimpleHTTPServer 8000

# Node.js alternative (if available)
npx http-server -p 8000
```

## Code Architecture

### SCSS Structure
- **Modular approach**: Separate SCSS files for each page/component
- **Variable system**: Centralized colors and typography in `_variable.scss`
- **Import hierarchy**: `style.scss` imports all partials in logical order

### JavaScript Architecture
- **jQuery-based**: All interactivity uses jQuery
- **Component organization**: `main.js` contains initialization for:
  - Preloader animations
  - Portfolio filtering (Mixitup)
  - Image gallery (Masonry)
  - Carousel sliders (Owl Carousel)
  - Mobile navigation (SlickNav)
  - Video popups (Magnific Popup)
  - Counter animations

### HTML Structure
- **Consistent layout**: All pages follow same header/footer structure
- **Bootstrap grid**: Uses Bootstrap 4 grid system for responsive layouts
- **Component reuse**: Common sections like testimonials, services repeated across pages

## Key Features and Functionality

### Interactive Elements
- **Hero slider**: Owl Carousel with custom dot numbering
- **Portfolio filter**: Mixitup for category-based filtering
- **Masonry gallery**: Pinterest-style image layout
- **Video popups**: YouTube video integration
- **Counter animations**: Animated number counters
- **Mobile navigation**: Responsive hamburger menu

### Styling System
- **Color scheme**: Primary blue (#00bfe7), secondary navy (#0c2b4b)
- **Typography**: Play and Josefin Sans from Google Fonts
- **Responsive design**: Mobile-first approach with breakpoints

## Content Management

### Adding New Work/Portfolio Items
1. Add images to appropriate `img/` subdirectories
2. Update portfolio filtering in `portfolio.html`
3. Ensure Mixitup categories match new items

### Modifying Styles
1. Edit SCSS files in `sass/` directory, not compiled CSS
2. Compile SCSS after changes using sass command
3. Test responsive behavior across breakpoints

### Image Management
- Organize images by page/section in `img/` subdirectories
- Use consistent naming conventions
- Optimize images for web before adding

## Browser Compatibility

The site uses modern web standards but maintains compatibility with:
- All modern browsers (Chrome, Firefox, Safari, Edge)
- IE11 support through polyfills and fallbacks
- Mobile browsers on iOS and Android

## Performance Considerations

- Images should be optimized for web delivery
- Consider lazy loading for gallery images
- Minify CSS and JavaScript for production
- Enable gzip compression on server