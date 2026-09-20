# 🏋️ FitFlow – AI-Powered Fitness App Redesign

> **IT3060 – Human Computer Interaction | Lab Exercise 05**  
> **Technology Stack Selection, Architecture Design & GitHub Repository Setup**

---

## 📱 Project Overview

**FitFlow** is an AI-powered fitness application that addresses critical UX issues identified through user research. This repository documents the complete technology stack evaluation, system architecture, and implementation framework for the redesigned FitFlow application.

### Core Features

- 🤖 **AI-Personalized Workout Generation** – Adaptive plans based on user behavior
- 📸 **Camera-based Nutrition Tracking** – Real-time food recognition via computer vision
- 🏆 **Social Challenges & Sharing** – Community engagement features
- 📊 **Health Metrics Dashboard** – Progress tracking & analytics
- 🔔 **Smart Notifications** – Context-aware reminders

---

## 🛠️ Selected Technology Stack

| Layer | Technology | Reason |
|---|---|---|
| **Mobile Frontend** | React Native (Expo) | Cross-platform, rich ecosystem, fast dev |
| **Main Backend API** | Node.js + NestJS | Scalable, real-time I/O, TypeScript |
| **AI/ML Microservice** | Python + FastAPI | ML libraries (TensorFlow, PyTorch) |
| **Primary Database** | PostgreSQL | Relational health data, ACID compliance |
| **Cache / Realtime** | Redis + Firebase RTDB | Live social feeds, session management |
| **Authentication** | Firebase Auth | OAuth 2.0, biometric, social login |
| **Cloud Platform** | AWS (ECS + RDS + S3) | Scalability, managed services |
| **CI/CD** | GitHub Actions | Automated testing & deployment |

---

## 📁 Repository Structure

```
fitflow-redesign/
├── frontend/           # React Native mobile application
│   ├── src/
│   │   ├── screens/    # App screens
│   │   ├── components/ # Reusable UI components
│   │   ├── navigation/ # React Navigation setup
│   │   ├── services/   # API calls & auth
│   │   └── store/      # Redux / Zustand state management
│   ├── assets/         # Images, fonts, icons
│   └── README.md
│
├── backend/            # Node.js + NestJS REST API
│   ├── src/
│   │   ├── modules/    # Feature modules (users, workouts, nutrition)
│   │   ├── common/     # Shared utilities, guards, interceptors
│   │   └── config/     # Environment configuration
│   └── README.md
│
├── ai-service/         # Python + FastAPI AI Microservice
│   ├── models/         # ML model files
│   ├── routers/        # API endpoints (workout gen, food recognition)
│   ├── services/       # Business logic
│   └── README.md
│
├── docs/               # Documentation & diagrams
│   ├── activity1-frontend-comparison.md
│   ├── activity2-backend-comparison.md
│   ├── activity3-decision-matrix.md
│   ├── activity4-architecture.md
│   └── adr/            # Architecture Decision Records
│
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI pipeline
│
├── .gitignore
└── README.md           # ← You are here
```

---

## 🚀 Quick Start

### Prerequisites

- Node.js >= 18.x
- Python >= 3.11
- PostgreSQL >= 15
- Redis >= 7.x
- Expo CLI (`npm install -g expo-cli`)

### 1. Clone the Repository

```bash
git clone https://github.com/Chenuka01/fitflow-redesign.git
cd fitflow-redesign
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npx expo start
```

### 3. Backend Setup

```bash
cd backend
npm install
cp .env.example .env   # Configure your environment variables
npm run start:dev
```

### 4. AI Service Setup

```bash
cd ai-service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│              React Native Mobile App                │
│         (iOS + Android via Expo)                    │
└────────────────────┬────────────────────────────────┘
                     │ HTTPS / WebSocket
          ┌─────────▼──────────┐
          │   API Gateway /    │
          │   Load Balancer    │
          └──────┬──────┬──────┘
                 │      │
    ┌────────────▼─┐  ┌─▼──────────────┐
    │  Node.js API │  │  Python FastAPI  │
    │  (NestJS)    │  │  (AI Service)   │
    └──────┬───────┘  └────────┬────────┘
           │                   │
    ┌──────▼───────────────────▼──────┐
    │     PostgreSQL  │  Redis Cache  │
    └──────────────────────────────────┘
```

> 📄 See [docs/activity4-architecture.md](docs/activity4-architecture.md) for full architecture details.

---

## 📋 Lab Activities Documentation

| Activity | Document | Description |
|---|---|---|
| Activity 1 | [Frontend Comparison](docs/activity1-frontend-comparison.md) | Flutter vs React Native vs KMP vs Swift |
| Activity 2 | [Backend Comparison](docs/activity2-backend-comparison.md) | Node.js vs FastAPI vs Go + DB & Auth |
| Activity 3 | [Decision Matrix](docs/activity3-decision-matrix.md) | Weighted scoring & final recommendation |
| Activity 4 | [Architecture Design](docs/activity4-architecture.md) | System architecture, data flows & ADR |
| Activity 5 | This README + Repository | GitHub setup & project structure |

---

## 👨‍💻 Student Information

| Field | Details |
|---|---|
| **Student Name** | Omindu Ayodya |
| **Module** | IT3060 – Human Computer Interaction |
| **Lab** | Lab Exercise 05 |
| **Topic** | Technology Stack Evaluation & System Architecture |
| **GitHub** | [@Chenuka01](https://github.com/Chenuka01) |

---

## 📄 License

This project is created for academic purposes as part of IT3060 HCI coursework.
