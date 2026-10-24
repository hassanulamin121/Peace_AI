🌌 Peace AI - Your Mindset & Focus Companion

Welcome to Peace AI! This isn't just another ChatGPT wrapper. I built Peace AI to be a fast, distraction-free, and visually calming AI companion. Whether I need to debug a complex block of code, brainstorm ideas, or just get some mental clarity after a long day, Peace AI provides a serene space to think and converse.

✨ What Does It Do? (Use Cases)

Distraction-Free Productivity: A minimalist, "glassmorphism" UI that doesn't overwhelm the eyes, keeping you entirely focused on the conversation.

Lightning-Fast Responses: Powered by Google's Gemini 2.5 Flash model, ensuring you get smart, context-aware answers instantly.

Seamless Local/Cloud Deployment: 100% containerized. You can spin this up on your local machine or deploy it to a cloud server with a single command.

🛠️ The Tech Stack

Frontend: Vanilla HTML, CSS (Glassmorphism), JavaScript, hosted on a standalone Nginx container.

Backend: Python, FastAPI, Uvicorn.

AI Engine: Google GenAI SDK (Gemini 2.5 Flash).

DevOps: Docker & Docker Compose for seamless orchestration.

🧗‍♂️ My Development Journey & Challenges Faced

I believe the best way to learn software engineering is by breaking things and fixing them. Here is a look into the hurdles I faced while building this project and how I overcame them:

1. Breaking Free from Framework Constraints

Initially, I thought about using Streamlit or Gradio to build the UI quickly. However, I found them too rigid. They created a "boxed-in" feel that ruined the calming aesthetic I wanted.
The Solution: I dropped the frameworks and built a custom frontend from scratch using pure HTML/CSS and Vanilla JS. This introduced CORS issues when connecting my local frontend to the FastAPI backend, which I successfully resolved by configuring precise CORS middleware in FastAPI.

2. The Docker Orchestration Puzzle

Moving from "it works on my machine" to a fully containerized architecture was the biggest challenge. I wanted to split the frontend and backend into true microservices.
The Fix: I wrote separate Dockerfiles for the FastAPI backend and an Nginx server for the frontend. The real headache came when wiring them together with docker-compose.yml. I ran into hidden bugs, such as Docker failing to locate the requirements.txt because of wrong build contexts, and environment variables (API keys) not passing correctly to the container. By meticulously debugging my volume mappings, setting up a proper .dockerignore, and configuring an internal network with depends_on, I got both containers talking to each other flawlessly.

3. Securing API Keys in a Containerized World

Keeping my Google Gemini API key secure while pushing code to GitHub and building Docker images was tricky.
The Solution: I structured the project to keep the .env file isolated inside the backend directory, explicitly added it to .gitignore, and used Docker Compose's env_file directive to inject the secrets only at runtime.

🚀 How to Run This Locally

If you want to spin up Peace AI on your own machine, you just need Docker installed.

Clone the repository:

git clone https://github.com/hassanulamin121/Peace_AI.git
cd Peace_AI


Add your API Key:
Create a .env file inside the /backend folder and add your Google Gemini API key:

GEMINI_API_KEY=your_api_key_here


Build and Run with Docker Compose:

docker-compose up --build


Experience the Peace:
Open your browser and navigate to http://localhost:8080.

Built with ❤️ and a lot of late-night tea.
