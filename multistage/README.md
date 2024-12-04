# Docker Best Practices Demo

## Overview
This project demonstrates best practices for creating a Docker container with a Python Flask application.

## Prerequisites
- Docker
- Docker Compose (optional)

## Project Structure
```
python-flask-app/
├── .dockerignore       # Excludes unnecessary files from Docker context
├── .env.example        # Example environment configuration
├── Dockerfile          # Docker image build instructions
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── src/                # Application source code
    ├── app.py          # Main Flask application
    └── templates/      # HTML templates
```

## Docker Build and Run

### Build the Docker Image
```bash
docker build -t flask-best-practices .
```

### Run the Docker Container
```bash
docker run -p 5000:5000 flask-best-practices
```

## Best Practices Demonstrated
- Multi-stage build
- Non-root user
- Minimal base image
- Layer caching optimization
- Environment variable management
- Health check implementation
- Dependency management
- Security considerations

## Environment Configuration
Copy `.env.example` to `.env` and modify as needed.

## Notes
- Uses Python 3.9 slim Debian-based image
- Implements a simple Flask web application
- Includes a health check endpoint
