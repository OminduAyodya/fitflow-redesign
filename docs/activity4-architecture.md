# Activity 4: System Architecture Design

**Student**: Omindu Ayodya  
**Module**: IT3060 – Human Computer Interaction  
**Lab**: Lab Exercise 05

---

## 🏗️ FitFlow System Architecture

This document outlines the complete system architecture for the FitFlow fitness application, including component diagrams, data flows, and architectural decision records (ADR).

---

## Table of Contents

1. [High-Level Architecture](#high-level-architecture)
2. [Component Architecture](#component-architecture)
3. [Data Flow Diagrams](#data-flow-diagrams)
4. [Database Schema](#database-schema)
5. [API Architecture](#api-architecture)
6. [Security Architecture](#security-architecture)
7. [Deployment Architecture](#deployment-architecture)
8. [Architecture Decision Records](#architecture-decision-records)

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     CLIENT LAYER                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │          React Native Mobile App (Expo)              │   │
│  │  iOS (Swift native modules) | Android (Kotlin)      │   │
│  └──────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS / WSS
                         │
┌────────────────────────▼────────────────────────────────────┐
│                   AUTHENTICATION LAYER                      │
│  ┌────────────────────────────────────────────────────┐    │
│  │            Firebase Authentication                  │    │
│  │  (OAuth 2.0, JWT, Biometric, Social Login)        │    │
│  └────────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                     API GATEWAY LAYER                       │
│  ┌────────────────────────────────────────────────────┐    │
│  │        AWS API Gateway / Load Balancer             │    │
│  │  (Rate Limiting, Request Routing, SSL/TLS)        │    │
│  └────────────────────────────────────────────────────┘    │
└───────────────────┬────────────────┬────────────────────────┘
                    │                │
        ┌───────────▼─────┐    ┌────▼──────────────┐
        │   Main API      │    │  AI Microservice   │
        │  Node.js        │    │   Python           │
        │  NestJS         │    │   FastAPI          │
        │  (TypeScript)   │    │                    │
        │                 │    │  - ML Models       │
        │  - REST API     │    │  - TensorFlow      │
        │  - WebSocket    │    │  - PyTorch         │
        │  - Business     │    │  - OpenCV          │
        │    Logic        │    │                    │
        └────────┬────────┘    └──────┬─────────────┘
                 │                    │
                 │                    │
    ┌────────────▼────────────────────▼──────────┐
    │           DATA LAYER                       │
    │  ┌──────────────┐      ┌────────────────┐ │
    │  │  PostgreSQL  │      │  Redis Cache   │ │
    │  │   (AWS RDS)  │      │  (ElastiCache) │ │
    │  │              │      │                │ │
    │  │ - User Data  │      │ - Sessions     │ │
    │  │ - Workouts   │      │ - Leaderboards │ │
    │  │ - Nutrition  │      │ - Rate Limits  │ │
    │  │ - Social     │      │ - Cache        │ │
    │  └──────────────┘      └────────────────┘ │
    │                                            │
    │  ┌──────────────┐      ┌────────────────┐ │
    │  │   AWS S3     │      │  Firebase RTDB │ │
    │  │              │      │                │ │
    │  │ - Images     │      │ - Live Updates │ │
    │  │ - Videos     │      │ - Notifications│ │
    │  │ - ML Models  │      │ - Real-time    │ │
    │  └──────────────┘      └────────────────┘ │
    └────────────────────────────────────────────┘
```

---

## Component Architecture

### 1. Frontend Components (React Native)

```
frontend/
├── Screens Layer
│   ├── HomeScreen          → Dashboard, daily stats
│   ├── WorkoutScreen       → Workout plans, exercise tracking
│   ├── NutritionScreen     → Food logging, camera scan
│   ├── ChallengesScreen    → Social challenges
│   ├── ProfileScreen       → User settings, progress
│   └── AuthScreen          → Login, signup
│
├── Components Layer
│   ├── WorkoutCard         → Display workout info
│   ├── ExerciseList        → Exercise items
│   ├── NutritionTracker    → Food entry, macros
│   ├── ProgressChart       → Data visualization
│   ├── ChallengeCard       → Challenge display
│   └── NotificationBanner  → In-app alerts
│
├── Services Layer
│   ├── api.ts              → API client (axios)
│   ├── auth.ts             → Firebase auth
│   ├── storage.ts          → AsyncStorage
│   └── push.ts             → Push notifications
│
├── State Management
│   ├── userStore           → User profile state
│   ├── workoutStore        → Workout data
│   └── nutritionStore      → Nutrition logs
│
└── Navigation
    └── AppNavigator        → Tab & stack navigation
```

### 2. Backend Components (Node.js + NestJS)

```
backend/
├── Modules
│   ├── UsersModule
│   │   ├── Controller      → User CRUD endpoints
│   │   ├── Service         → Business logic
│   │   ├── Repository      → Data access
│   │   └── DTOs            → Data transfer objects
│   │
│   ├── WorkoutsModule
│   │   ├── Controller      → Workout endpoints
│   │   ├── Service         → Workout logic
│   │   ├── Repository      → DB operations
│   │   └── AI Client       → Call AI service
│   │
│   ├── NutritionModule
│   │   ├── Controller      → Nutrition endpoints
│   │   ├── Service         → Food logging
│   │   └── AI Client       → Image recognition
│   │
│   ├── ChallengesModule
│   │   ├── Controller      → Challenge endpoints
│   │   ├── Service         → Challenge logic
│   │   └── Gateway         → WebSocket events
│   │
│   └── AnalyticsModule
│       ├── Controller      → Stats endpoints
│       └── Service         → Data aggregation
│
├── Common
│   ├── Guards
│   │   └── JwtAuthGuard    → JWT verification
│   ├── Interceptors
│   │   └── LoggingInterceptor
│   ├── Filters
│   │   └── HttpExceptionFilter
│   └── Decorators
│       └── CurrentUser
│
└── Config
    ├── database.config.ts
    ├── redis.config.ts
    └── firebase.config.ts
```

### 3. AI Microservice Components (Python + FastAPI)

```
ai-service/
├── Routers
│   ├── workout_router.py   → /workouts/generate
│   └── nutrition_router.py → /nutrition/recognize
│
├── Services
│   ├── workout_generator.py
│   │   └── generate_plan()  → ML-based workout creation
│   └── food_recognizer.py
│       └── recognize_food() → CNN image classification
│
├── Models
│   ├── workout_model.pkl    → Trained workout model
│   └── food_cnn.h5          → Food recognition CNN
│
└── Utils
    ├── preprocessing.py     → Image preprocessing
    └── model_loader.py      → Load ML models
```

---

## Data Flow Diagrams

### 1. User Authentication Flow

```
┌──────┐         ┌──────────┐        ┌─────────┐       ┌──────────┐
│ User │         │ React    │        │Firebase │       │ Backend  │
│      │         │ Native   │        │  Auth   │       │   API    │
└───┬──┘         └────┬─────┘        └────┬────┘       └────┬─────┘
    │                 │                   │                  │
    │  1. Login       │                   │                  │
    ├────────────────>│                   │                  │
    │                 │  2. Authenticate  │                  │
    │                 ├──────────────────>│                  │
    │                 │                   │                  │
    │                 │  3. JWT Token     │                  │
    │                 │<──────────────────┤                  │
    │                 │                   │                  │
    │                 │  4. API Request + Token             │
    │                 ├─────────────────────────────────────>│
    │                 │                   │                  │
    │                 │                   │  5. Verify Token │
    │                 │                   │<─────────────────┤
    │                 │                   │                  │
    │                 │                   │  6. Token Valid  │
    │                 │                   ├─────────────────>│
    │                 │                   │                  │
    │                 │  7. Response Data                    │
    │                 │<─────────────────────────────────────┤
    │  8. Show Data   │                   │                  │
    │<────────────────┤                   │                  │
```

### 2. AI Workout Generation Flow

```
┌──────┐    ┌────────┐    ┌─────────┐    ┌──────────┐    ┌──────────┐
│ User │    │ Mobile │    │Backend  │    │   AI     │    │PostgreSQL│
│      │    │  App   │    │   API   │    │ Service  │    │          │
└───┬──┘    └───┬────┘    └────┬────┘    └────┬─────┘    └────┬─────┘
    │           │              │               │               │
    │ 1. Request│              │               │               │
    │  Workout  │              │               │               │
    ├──────────>│              │               │               │
    │           │              │               │               │
    │           │ 2. POST /workouts/generate   │               │
    │           ├─────────────>│               │               │
    │           │              │               │               │
    │           │              │ 3. Get User   │               │
    │           │              │    Profile    │               │
    │           │              ├──────────────────────────────>│
    │           │              │               │               │
    │           │              │ 4. User Data  │               │
    │           │              │<──────────────────────────────┤
    │           │              │               │               │
    │           │              │ 5. Generate   │               │
    │           │              │    Workout    │               │
    │           │              ├──────────────>│               │
    │           │              │               │               │
    │           │              │               │ (ML Model     │
    │           │              │               │  Processing)  │
    │           │              │               │               │
    │           │              │ 6. Workout    │               │
    │           │              │    Plan       │               │
    │           │              │<──────────────┤               │
    │           │              │               │               │
    │           │              │ 7. Save Plan  │               │
    │           │              ├──────────────────────────────>│
    │           │              │               │               │
    │           │ 8. Workout   │               │               │
    │           │    Data      │               │               │
    │           │<─────────────┤               │               │
    │           │              │               │               │
    │ 9. Display│              │               │               │
    │   Workout │              │               │               │
    │<──────────┤              │               │               │
```

### 3. Nutrition Tracking (Camera) Flow

```
┌──────┐    ┌────────┐    ┌─────────┐    ┌──────────┐    ┌──────┐
│ User │    │ Mobile │    │Backend  │    │   AI     │    │  S3  │
│      │    │  App   │    │   API   │    │ Service  │    │      │
└───┬──┘    └───┬────┘    └────┬────┘    └────┬─────┘    └───┬──┘
    │           │              │               │              │
    │ 1. Take   │              │               │              │
    │  Photo    │              │               │              │
    ├──────────>│              │               │              │
    │           │              │               │              │
    │           │ 2. Upload    │               │              │
    │           │    Image     │               │              │
    │           ├─────────────>│               │              │
    │           │              │               │              │
    │           │              │ 3. Store      │              │
    │           │              │    Image      │              │
    │           │              ├─────────────────────────────>│
    │           │              │               │              │
    │           │              │ 4. Recognize  │              │
    │           │              │    Food       │              │
    │           │              ├──────────────>│              │
    │           │              │               │              │
    │           │              │               │ (CNN Model   │
    │           │              │               │  Inference)  │
    │           │              │               │              │
    │           │              │ 5. Food +     │              │
    │           │              │    Nutrition  │              │
    │           │              │<──────────────┤              │
    │           │              │               │              │
    │           │ 6. Nutrition │               │              │
    │           │    Data      │               │              │
    │           │<─────────────┤               │              │
    │           │              │               │              │
    │ 7. Show   │              │               │              │
    │  Results  │              │               │              │
    │<──────────┤              │               │              │
```

---

## Database Schema

### Entity Relationship Diagram

```
┌─────────────┐         ┌─────────────────┐         ┌───────────────┐
│    users    │         │    workouts     │         │   exercises   │
├─────────────┤         ├─────────────────┤         ├───────────────┤
│ id (PK)     │────────<│ user_id (FK)    │         │ id (PK)       │
│ email       │         │ id (PK)         │>───────<│ name          │
│ name        │         │ title           │         │ muscle_group  │
│ password    │         │ duration        │         │ equipment     │
│ fitness_lvl │         │ calories        │         │ difficulty    │
│ created_at  │         │ created_at      │         │ instructions  │
└─────────────┘         └─────────────────┘         └───────────────┘
       │                                                     │
       │                ┌─────────────────┐                 │
       │                │ workout_exercises│                │
       │                ├─────────────────┤                 │
       └───────────────<│ workout_id (FK) │>────────────────┘
                        │ exercise_id (FK)│
                        │ sets            │
                        │ reps            │
                        │ rest_seconds    │
                        └─────────────────┘

┌─────────────┐         ┌──────────────────┐
│    users    │         │  nutrition_logs  │
├─────────────┤         ├──────────────────┤
│ id (PK)     │────────<│ user_id (FK)     │
└─────────────┘         │ id (PK)          │
                        │ meal_type        │
                        │ food_name        │
                        │ calories         │
                        │ protein_g        │
                        │ carbs_g          │
                        │ fat_g            │
                        │ image_url        │
                        │ logged_at        │
                        └──────────────────┘

┌─────────────┐         ┌──────────────────┐         ┌─────────────┐
│    users    │         │   challenges     │         │participants │
├─────────────┤         ├──────────────────┤         ├─────────────┤
│ id (PK)     │        │ id (PK)          │>───────<│ user_id (FK)│
└─────────────┘        │ title            │         │challenge_id │
                       │ description      │         │ progress    │
                       │ start_date       │         │ rank        │
                       │ end_date         │         │ joined_at   │
                       │ goal_type        │         └─────────────┘
                       │ goal_value       │
                       └──────────────────┘
```

### Key Tables

#### users
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  firebase_uid VARCHAR(255) UNIQUE,
  fitness_level VARCHAR(50),
  height_cm DECIMAL(5,2),
  weight_kg DECIMAL(5,2),
  date_of_birth DATE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

#### workouts
```sql
CREATE TABLE workouts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  duration_minutes INT,
  estimated_calories INT,
  difficulty VARCHAR(50),
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### nutrition_logs
```sql
CREATE TABLE nutrition_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  meal_type VARCHAR(50),
  food_name VARCHAR(255),
  calories INT,
  protein_g DECIMAL(6,2),
  carbs_g DECIMAL(6,2),
  fat_g DECIMAL(6,2),
  fiber_g DECIMAL(6,2),
  image_url TEXT,
  logged_at TIMESTAMP DEFAULT NOW()
);
```

---

## API Architecture

### REST API Endpoints

#### Authentication
```
POST   /api/v1/auth/register       → Register new user
POST   /api/v1/auth/login          → Login user
POST   /api/v1/auth/refresh        → Refresh JWT token
POST   /api/v1/auth/logout         → Logout user
```

#### Users
```
GET    /api/v1/users/me            → Get current user profile
PUT    /api/v1/users/me            → Update profile
GET    /api/v1/users/me/stats      → Get user statistics
DELETE /api/v1/users/me            → Delete account
```

#### Workouts
```
GET    /api/v1/workouts            → List user workouts
POST   /api/v1/workouts            → Create workout
GET    /api/v1/workouts/:id        → Get workout details
PUT    /api/v1/workouts/:id        → Update workout
DELETE /api/v1/workouts/:id        → Delete workout
POST   /api/v1/workouts/generate   → Generate AI workout
POST   /api/v1/workouts/:id/complete → Mark workout complete
```

#### Nutrition
```
GET    /api/v1/nutrition/logs      → Get nutrition logs
POST   /api/v1/nutrition/logs      → Add nutrition entry
POST   /api/v1/nutrition/scan      → Scan food image
GET    /api/v1/nutrition/summary   → Daily/weekly summary
```

#### Challenges
```
GET    /api/v1/challenges          → List active challenges
POST   /api/v1/challenges          → Create challenge
GET    /api/v1/challenges/:id      → Get challenge details
POST   /api/v1/challenges/:id/join → Join challenge
GET    /api/v1/challenges/:id/leaderboard → Get leaderboard
```

### WebSocket Events

```javascript
// Client → Server
socket.emit('workout:start', { workoutId })
socket.emit('challenge:update', { challengeId, progress })

// Server → Client
socket.on('challenge:update', (data) => {})
socket.on('notification', (data) => {})
socket.on('leaderboard:update', (data) => {})
```

---

## Security Architecture

### 1. Authentication & Authorization

```
┌────────────────────────────────────────────────┐
│            Security Layers                     │
├────────────────────────────────────────────────┤
│  Layer 1: Firebase Authentication             │
│  - OAuth 2.0 (Google, Apple, Facebook)        │
│  - Email/Password with bcrypt                  │
│  - JWT token generation                        │
│  - Biometric authentication (mobile)           │
├────────────────────────────────────────────────┤
│  Layer 2: API Gateway                          │
│  - Rate limiting (100 req/min per user)        │
│  - IP whitelisting/blacklisting                │
│  - DDoS protection                             │
│  - SSL/TLS encryption                          │
├────────────────────────────────────────────────┤
│  Layer 3: Backend API Guards                   │
│  - JWT verification                            │
│  - Role-based access control (RBAC)            │
│  - Request validation (DTOs)                   │
│  - SQL injection prevention (Prisma ORM)       │
├────────────────────────────────────────────────┤
│  Layer 4: Data Layer                           │
│  - Database encryption at rest                 │
│  - Encrypted backups                           │
│  - VPC isolation (AWS)                         │
│  - Access logging & monitoring                 │
└────────────────────────────────────────────────┘
```

### 2. Data Privacy

- **GDPR Compliance**: User data deletion, export capabilities
- **HIPAA Considerations**: Health data encryption
- **PII Protection**: Sensitive data hashing
- **Data Retention**: 90-day inactive user data retention

### 3. Security Best Practices

- ✅ HTTPS only (TLS 1.3)
- ✅ JWT with short expiration (15 min access, 7 day refresh)
- ✅ Password hashing (bcrypt, salt rounds: 12)
- ✅ Input validation and sanitization
- ✅ SQL injection prevention (parameterized queries)
- ✅ XSS protection (CSP headers)
- ✅ CORS configuration (whitelist origins)
- ✅ Rate limiting per user/IP
- ✅ Security headers (helmet.js)

---

## Deployment Architecture

### AWS Infrastructure

```
┌─────────────────────────────────────────────────────────────┐
│                     AWS Cloud (us-east-1)                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │               Route 53 (DNS)                       │    │
│  └─────────────────────┬──────────────────────────────┘    │
│                        │                                     │
│  ┌─────────────────────▼──────────────────────────────┐    │
│  │         CloudFront (CDN) + WAF                     │    │
│  └─────────────────────┬──────────────────────────────┘    │
│                        │                                     │
│  ┌─────────────────────▼──────────────────────────────┐    │
│  │     Application Load Balancer (ALB)                │    │
│  │     (SSL Termination, Health Checks)               │    │
│  └───────────┬──────────────────┬─────────────────────┘    │
│              │                  │                            │
│   ┌──────────▼──────┐  ┌────────▼─────────┐               │
│   │   ECS Fargate   │  │   ECS Fargate    │               │
│   │  (Node.js API)  │  │  (Python AI)     │               │
│   │  Auto-scaling   │  │  Auto-scaling    │               │
│   │  2-10 tasks     │  │  1-5 tasks       │               │
│   └──────────┬──────┘  └────────┬─────────┘               │
│              │                   │                           │
│   ┌──────────▼───────────────────▼─────────┐               │
│   │         VPC (Private Subnet)           │               │
│   │  ┌──────────────┐   ┌───────────────┐ │               │
│   │  │   RDS        │   │  ElastiCache  │ │               │
│   │  │ PostgreSQL   │   │    Redis      │ │               │
│   │  │ Multi-AZ     │   │  (Cluster)    │ │               │
│   │  └──────────────┘   └───────────────┘ │               │
│   └────────────────────────────────────────┘               │
│                                                              │
│   ┌──────────────────────────────────────────┐             │
│   │              S3 Buckets                  │             │
│   │  - fitflow-images (user uploads)         │             │
│   │  - fitflow-ml-models (AI models)         │             │
│   │  - fitflow-backups (DB backups)          │             │
│   └──────────────────────────────────────────┘             │
│                                                              │
│   ┌──────────────────────────────────────────┐             │
│   │         CloudWatch Logs & Metrics        │             │
│   └──────────────────────────────────────────┘             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Container Images

```dockerfile
# Node.js API Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["node", "dist/main.js"]

# Python AI Service Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Architecture Decision Records

### ADR Directory Structure
```
docs/adr/
├── 001-use-react-native.md
├── 002-use-nestjs-backend.md
├── 003-use-postgresql.md
├── 004-use-microservices.md
└── 005-use-aws-infrastructure.md
```

### Example ADR Format

See: [docs/adr/001-use-react-native.md](adr/001-use-react-native.md)

---

## Performance Metrics

### Target SLAs

| Metric | Target | Monitoring |
|---|---|---|
| API Response Time (p95) | < 200ms | CloudWatch |
| API Response Time (p99) | < 500ms | CloudWatch |
| App Load Time | < 2s | Firebase Performance |
| Database Query Time | < 50ms | Prisma metrics |
| Image Upload Time | < 3s | S3 metrics |
| AI Inference Time | < 2s | Custom logs |
| Uptime | > 99.5% | AWS health dashboard |

---

## Monitoring & Observability

### Logging Strategy
- **Application Logs**: CloudWatch Logs
- **Access Logs**: ALB logs to S3
- **Error Tracking**: Sentry / CloudWatch Insights
- **Performance Monitoring**: New Relic / Datadog

### Metrics Tracked
- Request rate (RPM)
- Error rate (%)
- Response time (ms)
- CPU/Memory usage (%)
- Database connections
- Cache hit rate (%)

---

## Conclusion

This architecture provides:
- ✅ **Scalability**: Auto-scaling ECS tasks, load balancing
- ✅ **Reliability**: Multi-AZ deployment, health checks
- ✅ **Security**: Multi-layer security, encryption
- ✅ **Performance**: CDN, caching, optimized queries
- ✅ **Maintainability**: Microservices, clear separation
- ✅ **Observability**: Comprehensive logging & monitoring

---

**Document Version**: 1.0  
**Last Updated**: January 2025  
**Author**: Omindu Ayodya  
**Reviewed By**: [Instructor Name]
