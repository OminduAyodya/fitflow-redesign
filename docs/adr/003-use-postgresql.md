# ADR 003: Use PostgreSQL as Primary Database

**Date**: January 2025  
**Status**: Accepted  
**Decision Makers**: Omindu Ayodya

---

## Context

FitFlow requires a database for:
- User profiles and authentication data
- Workout plans and exercise libraries
- Nutrition logs
- Social challenges and leaderboards
- Health metrics (time-series data)

---

## Decision

We will use **PostgreSQL** as the primary relational database.

---

## Rationale

### Pros
- **ACID compliance**: Essential for health data integrity
- **Relational model**: Natural fit for user → workouts → exercises structure
- **Advanced JSON support**: Store flexible data (workout configurations, nutrition details)
- **Complex queries**: JOIN operations for social features (leaderboards, challenges)
- **Performance**: Excellent read/write performance for our scale
- **Indexing**: Advanced indexing for fast lookups
- **Cloud support**: AWS RDS provides managed PostgreSQL

### Cons
- Less flexible schema changes than NoSQL
- Vertical scaling more expensive than horizontal

---

## Alternatives Considered

### MongoDB
- **Rejected**: Less suited for relational data, weaker data integrity guarantees

### MySQL
- **Rejected**: PostgreSQL has better JSON support and advanced features

---

## Consequences

### Positive
- Strong data integrity for health records
- Efficient complex queries (user stats, challenge rankings)
- JSON columns provide flexibility where needed

### Negative
- Schema migrations required for changes
- Need to design schema carefully upfront

---

## Implementation

- AWS RDS PostgreSQL 15+ (Multi-AZ for HA)
- Prisma ORM for type-safe queries
- Connection pooling via PgBouncer
- Daily automated backups

---

**Author**: Omindu Ayodya
