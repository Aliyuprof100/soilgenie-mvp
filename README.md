🌱 Soilgenie: Cultivating Smarter Farms, Bountiful Futures in Nigeria
✨ Project Overview
Soilgenie is an innovative agricultural intelligence platform designed to empower Nigerian farmers with data-driven insights. By leveraging cutting-edge technology like AI and satellite imagery, Soilgenie aims to optimize crop yields, promote sustainable practices, and bridge the digital divide in rural farming communities. Our unique agent-assisted model ensures that even farmers with limited digital access can benefit from personalized recommendations and real-time farm monitoring.

🚀 Features
Soilgenie offers a comprehensive suite of features tailored for both farmers and dedicated agents:

For Farmers 🧑‍🌾
Intuitive Dashboard: A central hub to view key farm metrics and alerts.

My Farm Map (Powered by Google Maps): Visualize your farmland with an interactive map, providing geographical context for your operations.

Farmland Mapping: Easily submit details about your farm for precise monitoring and analysis.

Personalized Recommendations: Receive timely, AI-driven advice on fertilizer application, irrigation, pest management, and more.

Hyper-Local Weather Trends: Access accurate 7-day weather forecasts specific to your farm's location.

SMS Notifications: Get critical alerts and recommendations directly to your phone, ensuring accessibility even without internet.

Soilgenie AI Assistant: Ask agricultural questions and receive instant, expert advice from our AI chatbot.

My Tasks & Reports: Track your farming activities and access farm-specific reports.

For Agents 👨‍💼
Agent Dashboard: An overview of assigned farmers, pending tasks, and messages.

Farmer Management: View and manage profiles for all assigned farmers.

Map New Farmland: Assist farmers in accurately mapping their land and inputting crop details.

Task Management: Keep track of pending field visits, soil tests, and other responsibilities.

Messaging: Communicate directly with farmers to provide support and gather information.

Weather Insights: Access detailed regional weather trends and critical alerts to better advise farmers.

AI Insights Tool: Generate specific AI-driven recommendations for farmers based on their data.

Recommendations Overview: Monitor the status of all recommendations issued to farmers.

Enhanced Reporting: Generate comprehensive reports on farmer progress, yield trends, and agent impact.

Knowledge Base: Access a rich library of agricultural articles and best practices.

Appointment Scheduler: Efficiently manage and schedule field visits with farmers.

Field Reports: Document observations and actions from farm visits.

💻 Technology Stack
This project is built with a powerful combination of frontend and backend technologies:

Frontend
HTML5: Structure of the web application.

Tailwind CSS: For rapid and responsive UI development.

JavaScript: Powers interactive elements and API communication.

Google Maps JavaScript API: For interactive mapping and geographical visualization.

Font Awesome: Iconography for a visually rich user interface.

Gemini API: Powers the AI Assistant functionality.

Backend (Django)
Python: The core programming language.

Django: High-level Python web framework for robust backend development.

Django REST Framework (DRF): For building powerful and flexible APIs.

SQLite3: Default database for development (easily scalable to PostgreSQL, MySQL, etc.).

Django CORS Headers: Manages Cross-Origin Resource Sharing for secure frontend-backend communication.

Session-based Authentication: Handles user login and session management.

🛠️ Getting Started
Follow these steps to set up and run Soilgenie locally for development.

Prerequisites
Python 3.8+

pip (Python package installer)

Git

A Google Maps API Key (for full map functionality in farmer_dashboard.html and pitch deck)

1. Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/soilgenie-frontend.git # Replace with your actual repo
cd soilgenie-frontend

(Assuming you have a monorepo structure or you'll manually manage backend/frontend folders)

Let's assume a project structure like this for the setup instructions:

soilgenie_project/
├── backend/ # Django project
│   ├── soilgenie_backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── users/
│   ├── farms/
│   ├── recommendations/
│   ├── agents/
│   └── manage.py
└── frontend/ # Your HTML, CSS, JS files
    ├── index.html
    ├── farmer_dashboard.html
    ├── agent_dashboard.html
    ├── farmer_login.html
    ├── agent_login.html
    ├── ...
    └── images/

2. Backend Setup (Django)
Navigate into the backend directory:

cd soilgenie_project/backend

Create a Virtual Environment:

python -m venv venv

Activate Virtual Environment:

Windows: .\venv\Scripts\activate

macOS/Linux: source venv/bin/activate

Install Dependencies:

pip install Django djangorestframework django-cors-headers

Apply Migrations:

python manage.py makemigrations
python manage.py migrate

Create a Superuser (for Admin access):

python manage.py createsuperuser

Follow the prompts to create your admin user.

Run the Django Development Server:

python manage.py runserver

The backend API will now be running at http://127.0.0.1:8000/.

3. Frontend Setup
The frontend consists of static HTML, CSS (Tailwind), and JavaScript files.

Navigate to the Frontend Directory:
Ensure you are in the frontend directory:

cd soilgenie_project/frontend # From the project root

Open HTML Files: You can directly open index.html, farmer_login.html, agent_login.html, farmer_dashboard.html, agent_dashboard.html in your web browser.

Recommended: Use a live server extension (e.g., Live Server for VS Code) or Python's simple HTTP server to serve these files:

# In the 'frontend' directory
python -m http.server 8000 # Or any other port like 5500

Then access http://localhost:8000/index.html (or http://localhost:5500/index.html).

Configure Google Maps API Key:

Open farmer_dashboard.html in your text editor.

Locate the script tag for Google Maps:

<script async defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"></script>

Replace YOUR_API_KEY with your actual Google Maps API key (obtained from Google Cloud Console). This is crucial for the map to display.

🚀 Usage
Access the Application: Open http://127.0.0.1:8000/index.html (or your chosen frontend URL).

Registration:

Use the signup links (signup_selection.html) to register as a new Farmer or Agent.

Important: When registering a Farmer, ensure you fill in the optional farm details as well.

Login: Use the login links (login_selection.html) to log in using the credentials you created.

Explore Dashboards:

Farmer Dashboard: See your farm metrics, map, recommendations, and interact with the AI assistant.

Agent Dashboard: Manage farmers, map new lands, view tasks, and generate insights.

Interact with APIs:

The frontend is configured to communicate with the Django backend at http://127.0.0.1:8000/api/.

Test functionalities like mapping new farmland, fetching recommendations, and interacting with the AI assistant.

🤝 Contributing
We welcome contributions to the Soilgenie project!

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes and commit them (git commit -m 'Add new feature X').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
For questions, feedback, or collaborations, please reach out:

[Your Name] - [Your Email Address]

Project Link: [Link to your GitHub repository]