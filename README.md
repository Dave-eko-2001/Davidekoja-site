# David Ekoja Portfolio Site

A modern, full-stack portfolio website for David Ekoja, showcasing skills, experience, and selected projects. Built with HTML, CSS, JavaScript, and Python (Flask backend).

## Features
- Responsive, visually appealing design
- Animated hero section and smooth scrolling
- Skills, experience, and project showcase
- Contact form with backend integration
- Social media links
- Modular structure for easy customization

## Technologies Used
- **Frontend:** HTML5, CSS3, JavaScript (with Typed.js, Particles.js, AOS)
- **Backend:** Python (Flask, flask-cors)
- **Other:** Font Awesome, Google Fonts

## File Structure
```
Portfolio-site/
├── main.js           # Custom JS (placeholder)
├── style.css         # Custom CSS (placeholder)
├── test.html         # Main HTML file (all UI/logic)
├── server.py         # Flask backend for contact form
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
```

## Getting Started
### 1. Frontend
Open `test.html` in your browser to view the site. All styles and scripts are included inline or via CDN.

### 2. Backend (Contact Form)
1. Install Python 3.13+ and create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python server.py
   ```
4. Update the contact form in `test.html` to POST to `/contact` if backend integration is needed.

## Customization
- Update content in `test.html` for your own profile, skills, and projects.
- Add custom styles to `style.css` and scripts to `main.js` as needed.
- Extend `server.py` for advanced backend features (e.g., email, database).

## Deployment
- Host the frontend on any static site provider (Vercel, Netlify, GitHub Pages).
- Deploy the backend (Flask) on platforms like Heroku, Render, or your own server.

## License
This project is open source and available for personal and professional use.

---
**Built with passion and clean code by David Ekoja.**