# Airline Flights Data Ingestion Pipeline

> A production-ready Docker-based data engineering solution for ingesting and managing airline flight data into PostgreSQL with interactive database administration capabilities.

---

### 🏷️ Badges

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)]()
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2.20+-2496ED?style=flat&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-FCA121?style=flat&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Connect With Me](#connect-with-me)

---

## 🎯 Overview

This project implements a containerized data pipeline that ingests airline flight data from CSV files into a PostgreSQL database. It's designed with production principles in mind, utilizing Docker containers for consistent, reproducible deployments and includes pgAdmin for convenient database management and monitoring.

### Key Use Cases
- **Data Ingestion**: Automated batch processing of CSV flight data
- **Data Management**: Real-time database administration and monitoring
- **Development Environment**: Reproducible setup using Docker Compose
- **Production Deployment**: Container-ready for cloud platforms

---

## ✨ Features

- ✅ **Containerized Architecture**: Isolated, reproducible environment using Docker
- ✅ **Batch Processing**: Intelligent chunked data ingestion with configurable batch sizes
- ✅ **Rate Limiting**: Built-in delays between batches to prevent database overload
- ✅ **Database Admin UI**: pgAdmin dashboard for easy data exploration and management
- ✅ **Scalable Design**: Easy to extend for additional data sources
- ✅ **Error Handling**: Robust argument validation and error messaging
- ✅ **Python 3.12**: Modern Python with dependency management via UV

---

## 🏗️ Architecture

The project follows a **containerized microservices architecture** with three main components:

- 🐳 **Data Producer Service**: Python application that reads CSV data and ingests it into PostgreSQL with configurable batch processing and rate limiting
- 🗄️ **PostgreSQL Database**: Persistent data storage layer with automated volume management for data durability
- 🎨 **pgAdmin Web UI**: Interactive database management dashboard for real-time monitoring and SQL query execution

**Data Flow**: CSV Input → Python ETL → PostgreSQL Database ← pgAdmin UI

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (v24.0 or later) - [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose** (v2.20 or later) - [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python** 3.12+ (for local development only)
- **Git** - [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### System Requirements
- Minimum 2GB RAM
- 500MB available disk space
- Network access for image downloads

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd 01-docker

# Start containers
docker compose up -d

# Verify containers are running
docker compose ps

# Ingest data (example)
docker compose exec data_producer python data_producer.py \
  --pg-user root \
  --pg-pass root \
  --pg-host pgdatabase \
  --pg-port 5432 \
  --pg-db airline \
  --target-table flights

# Access pgAdmin
# Open browser → http://localhost:8085
# Login: admin@admin.com / root

# Stop containers
docker compose down
```

---

## 🔧 Installation

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd 01-docker
```

### Step 2: Verify Project Structure
```bash
ls -la
# You should see:
# - Docker-compose.yaml
# - Dockerfile
# - data_producer.py
# - airlines_flights_data.csv
# - pyproject.toml
# - README.md
```

### Step 3: Build and Start Services
```bash
# Build Docker images
docker compose build

# Start services in background
docker compose up -d

# Check service status
docker compose logs -f
```

### Step 4: Verify Database Connection
```bash
# Test PostgreSQL connection
docker compose exec pgdatabase psql -U root -d ny_taxi -c "SELECT version();"
```

---

## 📖 Usage

### Running the Data Ingestion Pipeline

#### Option 1: Using Docker Compose Exec
```bash
docker compose exec data_producer python data_producer.py \
  --pg-user root \
  --pg-pass root \
  --pg-host pgdatabase \
  --pg-port 5432 \
  --pg-db ny_taxi \
  --target-table flights_data
```

#### Option 2: Direct Python Execution (Local Development)
```bash
# Install dependencies
pip install -r requirements.txt

# Run data producer
python data_producer.py \
  --pg-user root \
  --pg-pass root \
  --pg-host localhost \
  --pg-port 5432 \
  --pg-db ny_taxi \
  --target-table flights_data
```

### Accessing pgAdmin

1. **Open Browser**: Navigate to `http://localhost:8085`
2. **Login Credentials**:
   - Email: `admin@admin.com`
   - Password: `root`
3. **Register Server**:
   - Host: `pgdatabase`
   - Port: `5432`
   - Username: `root`
   - Password: `root`
4. **Query Data**: Navigate to Servers → PostgreSQL → Databases → ny_taxi

### Example SQL Queries
```sql
-- View table structure
\dt

-- Count records
SELECT COUNT(*) FROM flights_data;

-- View first 10 records
SELECT * FROM flights_data LIMIT 10;

-- Get data summary
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'flights_data';
```

---

## ⚙️ Configuration

### Data Producer Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--pg-user` | Yes | - | PostgreSQL username |
| `--pg-pass` | Yes | - | PostgreSQL password |
| `--pg-host` | Yes | - | PostgreSQL host address |
| `--pg-port` | Yes | - | PostgreSQL port |
| `--pg-db` | Yes | - | Database name |
| `--target-table` | Yes | - | Target table name for ingestion |

### Docker Compose Configuration

**PostgreSQL Service**:
```yaml
POSTGRES_USER: root
POSTGRES_PASSWORD: root
POSTGRES_DB: ny_taxi
PORT: 5432
```

**pgAdmin Service**:
```yaml
PGADMIN_DEFAULT_EMAIL: admin@admin.com
PGADMIN_DEFAULT_PASSWORD: root
PORT: 8085
```

### Environment Variables

Create a `.env` file for sensitive credentials:
```bash
PG_USER=root
PG_PASSWORD=root
PG_HOST=pgdatabase
PG_PORT=5432
PG_DB=airline
TARGET_TABLE=flights_data
BATCH_SIZE=5
BATCH_DELAY=5
```

---

## 📁 Project Structure

Key components of the project:

- 🐳 **Dockerfile**: Container image definition for the Python data producer
- 🔄 **Docker-compose.yaml**: Multi-container orchestration configuration
- 📦 **pyproject.toml**: Project metadata and Python dependencies
- 🔧 **data_producer.py**: Main data ingestion script with batch processing
- 🚀 **main.py**: Application entry point
- 📊 **airlines_flights_data.csv**: Source data file
- 📝 **README.md**: Project documentation

---

## 🛠️ Technologies

### Core Technologies
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.12+ | Data processing and pipeline |
| **PostgreSQL** | 18 | Primary data storage |
| **pgAdmin** | Latest | Web-based database admin |
| **Docker** | 24.0+ | Containerization |
| **Docker Compose** | 2.20+ | Orchestration |

### Python Dependencies
```
pandas>=3.0.3          # Data manipulation
psycopg2-binary>=2.9.12 # PostgreSQL adapter
sqlalchemy>=2.0.50     # SQL toolkit and ORM
```

---

## 🐛 Troubleshooting

### Container Issues

**Problem**: Port already in use
```bash
# Solution: Change port in Docker-compose.yaml or stop conflicting service
docker ps  # Find what's using the port
docker stop <container_id>
```

**Problem**: Container fails to start
```bash
# View logs
docker compose logs -f pgdatabase
docker compose logs -f data_producer

# Rebuild images
docker compose down
docker compose build --no-cache
docker compose up -d
```

### Database Connection Issues

**Problem**: "Connection refused" error
```bash
# Ensure PostgreSQL is running
docker compose ps pgdatabase

# Check database logs
docker compose logs pgdatabase

# Verify credentials in Docker-compose.yaml
```

**Problem**: Data ingestion fails
```bash
# Check CSV file exists
ls -la airlines_flights_data.csv

# Verify table exists
docker compose exec pgdatabase psql -U root -d ny_taxi -c "\dt"

# Check data producer logs
docker compose logs data_producer
```

### Performance Issues

**Problem**: Slow data ingestion
```bash
# Increase batch size in data_producer.py
batch_size = 50  # default: 5

# Reduce delay between batches
delay = 1  # default: 5 seconds
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python
- Add docstrings to functions
- Test locally before pushing
- Update README for new features

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤳 Connect With Me

I'm passionate about data engineering, cloud infrastructure, and open-source development. Let's connect and collaborate!

### 🔗 Professional Networks

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vengatesh-a-3549922a2)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF6B6B?style=flat&logo=vercel&logoColor=white)](https://vengatesh.vercel.app/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:a.vengatesh123@gmail.com)

### 💼 Areas of Expertise

- 🔄 Data Engineering & ETL Pipelines
- ☁️ Cloud Infrastructure (AWS, GCP, Azure)
- 📊 Data Analytics & Business Intelligence
- 🐳 Docker & Kubernetes
- 🐘 PostgreSQL & Database Design
- 🔗 Open Source Contributions

### 🌟 Featured Projects

- **[Data Pipeline Framework](link)**: Scalable ETL solution with monitoring
- **[Cloud Migration Suite](link)**: Automated AWS migration toolkit
- **[Analytics Dashboard](link)**: Real-time BI platform with Grafana

---

## 📞 Support & Questions

If you have questions or need help, explore these resources:

📚 **Documentation**:
- [Docker Documentation](https://docs.docker.com/) - Comprehensive Docker guides
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - SQL and administration
- [pgAdmin Documentation](https://www.pgadmin.org/docs/) - Database management UI
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) - Python ORM toolkit
- [Pandas Documentation](https://pandas.pydata.org/docs/) - Data manipulation

🆘 **Getting Help**:
1. Check the [Troubleshooting Section](#-troubleshooting) above
2. Review Docker Compose logs: `docker compose logs -f`
3. Contact via [Email](mailto:a.vengatesh123@gmail.com) or [LinkedIn](https://www.linkedin.com/in/vengatesh-a-3549922a2)

💬 **Community Resources**:
- [Stack Overflow - Docker](https://stackoverflow.com/questions/tagged/docker)
- [Stack Overflow - PostgreSQL](https://stackoverflow.com/questions/tagged/postgresql)
- [Stack Overflow - Python](https://stackoverflow.com/questions/tagged/python)
- [Docker Community Forums](https://forums.docker.com/)

---

## 🙏 Acknowledgments

Special thanks to the amazing open-source communities:

- [Docker](https://www.docker.com/) - Container platform
- [PostgreSQL](https://www.postgresql.org/) - Reliable database
- [pgAdmin](https://www.pgadmin.org/) - Database administration
- [Python](https://www.python.org/) - Programming language
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit
- [Pandas](https://pandas.pydata.org/) - Data analysis library

---

<div align="center">

**Built with ❤️ VENGATESH A**

⭐ If this project helped you, please consider giving it a star! ⭐

</div>
