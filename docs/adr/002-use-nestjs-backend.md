# ADR 002: Use Node.js + NestJS for Backend API

**Date**: January 2025  
**Status**: Accepted  
**Decision Makers**: Omindu Ayodya

---

## Context

FitFlow backend needs to handle:
- RESTful API for CRUD operations
- Real-time features (WebSocket for challenges)
- Integration with AI microservice
- High I/O throughput for mobile clients

---

## Decision

We will use **Node.js with NestJS framework** for the main backend API.

---

## Rationale

### Pros
- **TypeScript**: Full type safety across frontend and backend
- **Real-time support**: Excellent WebSocket integration (Socket.io)
- **Modular architecture**: NestJS provides clean module structure
- **Scalability**: Event-driven, non-blocking I/O for concurrent users
- **Ecosystem**: npm has extensive packages for all features
- **Testing**: Built-in testing tools (Jest)
- **Team alignment**: Shared JavaScript knowledge with frontend

### Cons
- Lower CPU-bound performance than Go
- Single-threaded (mitigated by clustering)

---

## Alternatives Considered

### Python + FastAPI
- **Partially adopted**: Used for AI microservice only
- **Reason**: Better for ML, but slower for real-time features

### Go + Gin
- **Rejected**: Steeper learning curve, smaller ecosystem

---

## Consequences

### Positive
- Code sharing between frontend/backend (utilities, types)
- Faster development with familiar language
- Strong real-time capabilities

### Negative
- Need to handle CPU-intensive tasks in separate workers

---

## Implementation

- NestJS 10+ with TypeScript
- Prisma ORM for database
- Socket.io for WebSocket
- Redis for caching

---

**Author**: Omindu Ayodya
