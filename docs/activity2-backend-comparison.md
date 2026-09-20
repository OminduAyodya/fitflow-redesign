# Activity 2: Backend Technology Comparison

**Student**: Omindu Ayodya  
**Module**: IT3060 – Human Computer Interaction  
**Lab**: Lab Exercise 05

---

## 🔧 Backend Framework Evaluation

This document compares backend technologies, databases, and authentication services for the FitFlow application.

---

## Part 1: Backend Frameworks

### Frameworks Under Evaluation

1. **Node.js + NestJS** (TypeScript)
2. **Python + FastAPI**
3. **Go + Gin**

### Comparison Matrix

| Criteria | Node.js + NestJS | Python + FastAPI | Go + Gin |
|---|---|---|---|
| **Language** | TypeScript/JavaScript | Python | Go |
| **Performance** | Good (async I/O) | Good | Excellent |
| **Scalability** | Excellent | Good | Excellent |
| **Developer Productivity** | High | High | Medium |
| **Community** | Very Large | Large | Growing |
| **Learning Curve** | Low | Low | Medium |
| **Real-time Support** | Excellent (Socket.io) | Good (WebSockets) | Good |
| **Async/Await** | ✅ Native | ✅ Native | ✅ Goroutines |
| **Type Safety** | ✅ TypeScript | ⚠️ Optional | ✅ Built-in |
| **Microservices** | Excellent | Excellent | Excellent |
| **Testing Tools** | Excellent | Excellent | Good |
| **Package Ecosystem** | Very Large (npm) | Large (pip) | Growing |

---

### 1. Node.js + NestJS ✅ SELECTED

**Pros:**
- TypeScript provides type safety
- NestJS modular architecture perfect for scaling
- Excellent for real-time features (WebSocket, Socket.io)
- Massive npm ecosystem
- Shared language with frontend (JavaScript/TypeScript)
- Great for I/O-heavy operations
- Built-in dependency injection
- Strong ORM support (Prisma, TypeORM)

**Cons:**
- Less CPU-intensive performance than Go
- Callback complexity (mitigated with async/await)
- Single-threaded (can spawn workers)

**Best For:** Real-time applications with I/O operations

---

### 2. Python + FastAPI

**Pros:**
- Fast development with Python's simplicity
- Excellent for ML/AI integration
- Auto-generated API documentation
- Type hints with Pydantic
- Great async support
- Perfect for data science workflows

**Cons:**
- Slower performance than Node.js for I/O
- GIL limits true parallelism
- Smaller ecosystem for web compared to Node

**Best For:** AI/ML-heavy applications, data processing

**Note:** We'll use FastAPI for the **AI microservice** specifically for ML workloads.

---

### 3. Go + Gin

**Pros:**
- Excellent performance and concurrency
- Compiled language - fast execution
- Low memory footprint
- Great for microservices
- Built-in concurrency primitives

**Cons:**
- More verbose code
- Smaller ecosystem than Node/Python
- Steeper learning curve
- Less real-time tooling

**Best For:** High-performance microservices, systems programming

---

## Part 2: Database Selection

### Databases Under Evaluation

1. **PostgreSQL** (Relational)
2. **MongoDB** (NoSQL Document)
3. **MySQL** (Relational)

### Comparison Matrix

| Criteria | PostgreSQL | MongoDB | MySQL |
|---|---|---|---|
| **Type** | Relational (SQL) | NoSQL (Document) | Relational (SQL) |
| **ACID Compliance** | ✅ Full | ⚠️ Partial | ✅ Full |
| **Scalability** | Vertical + Horizontal | Horizontal | Vertical + Horizontal |
| **Performance** | Excellent | Excellent (reads) | Excellent |
| **Complex Queries** | Excellent (JOIN) | Limited | Excellent (JOIN) |
| **JSON Support** | ✅ Native | ✅ Native | ⚠️ Limited |
| **Full-text Search** | ✅ Built-in | ✅ Built-in | ⚠️ Basic |
| **Data Integrity** | Excellent | Good | Excellent |
| **Community** | Large | Large | Very Large |
| **Cloud Support** | Excellent | Excellent | Excellent |

---

### PostgreSQL ✅ SELECTED

**Why Selected:**
- **Relational data model** fits fitness app (users → workouts → exercises)
- **ACID compliance** ensures data integrity for health metrics
- **Advanced JSON support** for flexible data (workout plans, nutrition logs)
- **Strong joins** for complex queries (social features, leaderboards)
- **Mature ecosystem** with excellent ORM support (Prisma)
- **AWS RDS support** for managed hosting

**Data Structure Example:**
```sql
users → workouts → exercises
users → nutrition_logs → meals
users → challenges → participants
```

**Trade-off:** Requires schema design upfront (acceptable for structured health data)

---

## Part 3: Authentication Service

### Options Under Evaluation

1. **Firebase Authentication** ✅
2. **Auth0**
3. **Custom JWT**

### Comparison Matrix

| Criteria | Firebase Auth | Auth0 | Custom JWT |
|---|---|---|---|
| **Setup Time** | Very Fast | Fast | Slow |
| **Social Login** | ✅ Built-in | ✅ Built-in | ❌ Manual |
| **Biometric** | ✅ Built-in | ✅ Built-in | ❌ Manual |
| **Free Tier** | Generous | Limited | N/A |
| **Customization** | Limited | High | Complete |
| **Security** | Enterprise | Enterprise | DIY |
| **Documentation** | Excellent | Excellent | N/A |
| **Mobile SDKs** | ✅ Native | ✅ Native | ❌ Manual |

---

### Firebase Authentication ✅ SELECTED

**Why Selected:**
- **Quick integration** with React Native (Firebase SDK)
- **Multiple auth methods**: Email, Google, Apple, Facebook
- **Biometric support** out of the box
- **Session management** handled automatically
- **Free tier** sufficient for development and initial launch
- **Real-time database** bonus for live features
- **Token verification** easy with backend

**Features Used:**
- Email/password authentication
- Google Sign-In
- Apple Sign-In (iOS requirement)
- Phone number verification (optional)
- Password reset flows

---

## Part 4: Additional Services

### Caching & Real-time

**Redis** ✅ SELECTED
- Session storage
- Real-time leaderboards
- Cache frequent queries (workout plans, user stats)
- Rate limiting

**Firebase Realtime Database**
- Live challenge updates
- Real-time notifications
- Social feed updates

---

## Final Backend Architecture

### Main API: Node.js + NestJS
**Handles:**
- User management
- Workout CRUD operations
- Nutrition logging
- Social features (challenges, sharing)
- Progress tracking

### AI Microservice: Python + FastAPI
**Handles:**
- Workout plan generation (ML models)
- Food image recognition (CNN models)
- Nutrition estimation
- Personalization algorithms

### Database: PostgreSQL
**Stores:**
- User profiles
- Workout plans
- Nutrition logs
- Social data
- Progress metrics

### Cache: Redis
**Caches:**
- Session tokens
- Leaderboards
- Frequent queries
- API rate limits

### Authentication: Firebase Auth
**Manages:**
- User sign-up/sign-in
- OAuth providers
- Token generation
- Password reset

---

## Architecture Diagram

```
┌─────────────────┐
│  React Native   │
│   Mobile App    │
└────────┬────────┘
         │
    ┌────▼────┐
    │ Firebase│
    │  Auth   │
    └────┬────┘
         │
┌────────▼─────────────┐
│   Load Balancer /    │
│    API Gateway       │
└──────┬───────┬───────┘
       │       │
   ┌───▼───┐ ┌▼────────┐
   │ Node  │ │ Python  │
   │NestJS │ │ FastAPI │
   │  API  │ │   AI    │
   └───┬───┘ └─────┬───┘
       │           │
   ┌───▼───────────▼───┐
   │   PostgreSQL      │
   │   + Redis Cache   │
   └───────────────────┘
```

---

## Decision Summary

| Layer | Technology | Primary Reason |
|---|---|---|
| Main API | Node.js + NestJS | Real-time support, TypeScript, large ecosystem |
| AI Service | Python + FastAPI | ML library support, async performance |
| Database | PostgreSQL | Relational integrity, complex queries, JSON support |
| Cache | Redis | Fast in-memory, real-time leaderboards |
| Auth | Firebase Auth | Quick setup, social login, biometric support |

---

## References

- [NestJS Documentation](https://docs.nestjs.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PostgreSQL vs MongoDB](https://www.postgresql.org/about/)
- [Firebase Auth Guide](https://firebase.google.com/docs/auth)

---

**Document Version**: 1.0  
**Last Updated**: January 2025  
**Author**: Omindu Ayodya
