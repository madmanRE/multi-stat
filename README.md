# Multi-Stat Analytics Service

Multi-Stat is a multi-channel analytics application built with Django, designed to fetch data from a remote server utilizing FastAPI. The application aggregates data on expenditures and revenues, along with additional parameters from various traffic sources. It provides comprehensive tables for effectively monitoring the performance of different traffic channels over various periods.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3
- pip (Python package installer)

### Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/madmanRE/multi-stat.git
   ```
2. Navigate to the project directory:
   ```
   cd multi-stat
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```
   uvicorn main:app &
   ```
5. In a new terminal window, start the Django server:
   ```
   python manage.py runserver
   ```

Now the application should be running and accessible via `http://localhost:8000` for the Django app and `http://localhost:8000/docs` for the FastAPI server's automatic interactive API documentation.

## Usage

After starting both the Django and FastAPI servers, you can navigate to the Django application to access the analytics dashboard. The FastAPI server will be serving as the remote server fetching the necessary data.

To interact with the application, use the provided endpoints to send and retrieve data. The dashboard will display the aggregated information in various tables, allowing you to analyze the traffic sources' performance.
