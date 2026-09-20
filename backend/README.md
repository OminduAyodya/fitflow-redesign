# 🔧 FitFlow Backend – Node.js + NestJS

## Overview

The FitFlow backend API is built with Node.js and NestJS framework, providing a scalable REST API for the mobile application.

## 🛠️ Tech Stack

- **Framework**: NestJS 10.x
- **Runtime**: Node.js 18+
- **Language**: TypeScript
- **Database**: PostgreSQL 15+
- **ORM**: Prisma / TypeORM
- **Cache**: Redis
- **Authentication**: JWT + Firebase Auth
- **API Documentation**: Swagger/OpenAPI

## 📁 Project Structure

```
backend/
├── src/
│   ├── modules/
│   │   ├── users/          # User management
│   │   ├── workouts/       # Workout plans & exercises
│   │   ├── nutrition/      # Meal tracking & nutrition
│   │   ├── challenges/     # Social challenges
│   │   └── analytics/      # Health metrics & reports
│   ├── common/
│   │   ├── guards/         # Auth guards
│   │   ├── interceptors/   # Request/response interceptors
│   │   ├── filters/        # Exception filters
│   │   └── decorators/     # Custom decorators
│   ├── config/             # Configuration files
│   ├── main.ts             # Application entry point
│   └── app.module.ts       # Root module
├── prisma/
│   └── schema.prisma       # Database schema
├── test/                   # E2E tests
├── .env.example
├── package.json
└── tsconfig.json
```

## 🚀 Getting Started

### Prerequisites

- Node.js >= 18.x
- PostgreSQL >= 15
- Redis >= 7.x
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Run database migrations
npx prisma migrate dev

# Start development server
npm run start:dev
```

## 🔧 Environment Variables

```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/fitflow"

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# JWT
JWT_SECRET=your-secret-key
JWT_EXPIRATION=7d

# Firebase
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_CLIENT_EMAIL=your-client-email
FIREBASE_PRIVATE_KEY=your-private-key

# AI Service
AI_SERVICE_URL=http://localhost:8000

# AWS
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
S3_BUCKET=fitflow-uploads
```

## 📦 Key Dependencies

```json
{
  "@nestjs/core": "^10.0.0",
  "@nestjs/common": "^10.0.0",
  "@nestjs/config": "^3.1.1",
  "@nestjs/jwt": "^10.2.0",
  "@prisma/client": "^5.7.0",
  "redis": "^4.6.11",
  "axios": "^1.6.2"
}
```

## 🛣️ API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - User login
- `POST /auth/refresh` - Refresh token

### Users
- `GET /users/profile` - Get user profile
- `PUT /users/profile` - Update profile
- `GET /users/stats` - Get user statistics

### Workouts
- `GET /workouts` - List workouts
- `POST /workouts/generate` - Generate AI workout plan
- `GET /workouts/:id` - Get workout details
- `POST /workouts/:id/complete` - Mark workout complete

### Nutrition
- `POST /nutrition/scan` - Scan food image
- `GET /nutrition/log` - Get nutrition log
- `POST /nutrition/log` - Add nutrition entry

### Challenges
- `GET /challenges` - List active challenges
- `POST /challenges/:id/join` - Join challenge
- `GET /challenges/:id/leaderboard` - Get leaderboard

## 🧪 Testing

```bash
# Unit tests
npm run test

# E2E tests
npm run test:e2e

# Test coverage
npm run test:cov
```

## 📊 Database Schema

The database uses PostgreSQL with Prisma ORM. Key tables include:

- `users` - User accounts and profiles
- `workouts` - Workout plans and templates
- `exercises` - Exercise library
- `nutrition_logs` - Food intake tracking
- `challenges` - Social challenges
- `progress` - Health metrics and progress tracking

## 👨‍💻 Developer

**Omindu Ayodya**  
IT3060 – Human Computer Interaction
