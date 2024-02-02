# VPN Service

VPN Service is a robust and secure virtual private network (VPN) solution built using Flask, a lightweight and flexible web framework for Python.

## Features:
1. User Registration.
2. Account Management.
3. Statistics Section.
4. Website Creation.
5. Internal Routing and Proxy Server.
6. Dynamic Content Replacement.
7. Statistics Tracking.

## Getting Started
Follow these steps to set up and run the project locally using Docker Compose.

### Prerequisites
- Docker
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sakhaline/vpn-service.git
2. Navigate to the project directory:
    ```bash
    cd app
3. Copy the environment file:
    ```bash
    cp .env-sample .env
4. Edit the ``.env`` file and set the necessary values.

5. Build and run with Docker Compose:
    ```bash
    docker-compose up --build
6. Access the Application.

Go to the ``http://localhost:5000`` in your web browser to access the VPN Service.

### Usage
- Register on the website.
- Login into your account.
- Explore VPN service features.
- Manage URLs for secure browsing.
- Keep track of your statistics.
