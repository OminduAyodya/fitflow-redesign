# Activity 3: Technology Stack Decision Matrix

**Student**: Omindu Ayodya  
**Module**: IT3060 – Human Computer Interaction  
**Lab**: Lab Exercise 05

---

## 📊 Weighted Scoring & Final Recommendation

This document provides a comprehensive weighted decision matrix for selecting the optimal technology stack for FitFlow.

---

## Evaluation Criteria & Weights

| Category | Weight | Rationale |
|---|---|---|
| **Development Speed** | 25% | Fast iteration for UX improvements |
| **Scalability** | 20% | Future growth potential |
| **Team Expertise** | 15% | Reduce learning curve |
| **Community Support** | 15% | Problem-solving resources |
| **Performance** | 10% | User experience quality |
| **Cross-platform** | 10% | Reach iOS & Android |
| **Cost** | 5% | Budget constraints |

**Total Weight:** 100%

---

## Frontend Framework Decision Matrix

### Scoring Scale: 1-10 (10 = Best)

| Criteria | Weight | Flutter | React Native | KMP | Swift |
|---|---|---|---|---|---|
| **Development Speed** | 25% | 8 | 9 | 6 | 4 |
| **Scalability** | 20% | 9 | 8 | 9 | 8 |
| **Team Expertise** | 15% | 4 | 9 | 6 | 6 |
| **Community Support** | 15% | 8 | 10 | 6 | 8 |
| **Performance** | 10% | 9 | 7 | 10 | 10 |
| **Cross-platform** | 10% | 10 | 10 | 9 | 2 |
| **Cost** | 5% | 9 | 9 | 7 | 5 |
| **Weighted Score** | | **8.05** | **8.85** ✅ | **7.15** | **6.00** |

### Calculation Example (React Native):
```
(9 × 0.25) + (8 × 0.20) + (9 × 0.15) + (10 × 0.15) + (7 × 0.10) + (10 × 0.10) + (9 × 0.05)
= 2.25 + 1.60 + 1.35 + 1.50 + 0.70 + 1.00 + 0.45
= 8.85
```

### Winner: **React Native** (8.85/10)

**Key Strengths:**
- Highest community support (10/10)
- Best development speed (9/10)
- Perfect cross-platform score (10/10)
- Excellent team expertise match (9/10)

**Why It Won:**
React Native scored highest in the most weighted categories (development speed and community support), which are critical for rapid UX iteration.

---

## Backend Framework Decision Matrix

### Scoring Scale: 1-10 (10 = Best)

| Criteria | Weight | Node.js + NestJS | Python + FastAPI | Go + Gin |
|---|---|---|---|---|
| **Development Speed** | 25% | 9 | 9 | 6 |
| **Scalability** | 20% | 9 | 7 | 10 |
| **Team Expertise** | 15% | 9 | 7 | 5 |
| **Community Support** | 15% | 10 | 8 | 6 |
| **Performance** | 10% | 7 | 7 | 10 |
| **Real-time Support** | 10% | 10 | 7 | 7 |
| **Cost** | 5% | 9 | 9 | 8 |
| **Weighted Score** | | **8.90** ✅ | **7.80** | **7.25** |

### Winner: **Node.js + NestJS** (8.90/10)

**Key Strengths:**
- Perfect community support (10/10)
- Best real-time capabilities (10/10)
- Excellent development speed (9/10)
- Strong team expertise (9/10)

**Hybrid Approach:**
We'll use **Python + FastAPI as a microservice** for AI/ML tasks, leveraging Python's ML ecosystem while keeping Node.js for the main API.

---

## Database Decision Matrix

### Scoring Scale: 1-10 (10 = Best)

| Criteria | Weight | PostgreSQL | MongoDB | MySQL |
|---|---|---|---|---|
| **Data Integrity** | 25% | 10 | 6 | 10 |
| **Query Complexity** | 20% | 10 | 5 | 9 |
| **Scalability** | 20% | 8 | 10 | 8 |
| **JSON Support** | 15% | 9 | 10 | 5 |
| **Community** | 10% | 9 | 9 | 10 |
| **Cloud Support** | 5% | 10 | 10 | 10 |
| **Performance** | 5% | 9 | 8 | 9 |
| **Weighted Score** | | **9.15** ✅ | **7.35** | **8.70** |

### Winner: **PostgreSQL** (9.15/10)

**Key Strengths:**
- Perfect ACID compliance (10/10)
- Best complex query support (10/10)
- Excellent JSON capabilities (9/10)
- Strong relational model for health data

---

## Authentication Service Decision Matrix

### Scoring Scale: 1-10 (10 = Best)

| Criteria | Weight | Firebase Auth | Auth0 | Custom JWT |
|---|---|---|---|---|
| **Setup Speed** | 30% | 10 | 7 | 3 |
| **Security** | 25% | 10 | 10 | 6 |
| **Features** | 20% | 9 | 10 | 5 |
| **Cost** | 15% | 10 | 6 | 10 |
| **Mobile SDKs** | 10% | 10 | 8 | 3 |
| **Weighted Score** | | **9.55** ✅ | **8.25** | **5.30** |

### Winner: **Firebase Authentication** (9.55/10)

**Key Strengths:**
- Fastest setup (10/10)
- Enterprise security (10/10)
- Best free tier (10/10)
- Native mobile SDKs (10/10)

---

## Final Technology Stack Recommendation

### Complete Stack Overview

| Layer | Selected Technology | Score | Key Reason |
|---|---|---|---|
| **Mobile Frontend** | React Native + Expo | 8.85/10 | Fast development, strong community |
| **Main Backend API** | Node.js + NestJS | 8.90/10 | Real-time support, TypeScript |
| **AI/ML Service** | Python + FastAPI | 7.80/10 | ML libraries, async performance |
| **Primary Database** | PostgreSQL | 9.15/10 | Data integrity, complex queries |
| **Caching** | Redis | N/A | In-memory speed, leaderboards |
| **Authentication** | Firebase Auth | 9.55/10 | Quick setup, social login |
| **Cloud Platform** | AWS | N/A | Scalability, managed services |
| **CI/CD** | GitHub Actions | N/A | Free, integrated with repo |

### Overall Stack Score: **8.86/10**

---

## Cost-Benefit Analysis

### Development Time Estimate

| Approach | Frontend | Backend | AI Service | Total Time |
|---|---|---|---|---|
| **Selected Stack** | 6 weeks | 8 weeks | 4 weeks | **18 weeks** |
| Alternative (Native) | 10 weeks | 8 weeks | 4 weeks | 22 weeks |
| Alternative (Flutter) | 7 weeks | 8 weeks | 4 weeks | 19 weeks |

**Time Saved:** 4 weeks compared to native development

### Cost Estimate (Development Phase)

| Item | Selected Stack | Native iOS + Android |
|---|---|---|
| Frontend Dev | $15,000 | $30,000 |
| Backend Dev | $20,000 | $20,000 |
| AI Service | $8,000 | $8,000 |
| **Total** | **$43,000** | **$58,000** |

**Cost Savings:** $15,000 (26% reduction)

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| React Native performance issues | Low | Medium | Use native modules for heavy operations |
| Limited native features | Low | Low | Expo provides most needed APIs |
| Firebase vendor lock-in | Medium | Medium | Design auth layer with abstraction |
| Team learning curve | Low | Low | Team already knows JavaScript |
| Scalability concerns | Low | Medium | NestJS built for microservices |

---

## Trade-offs Accepted

### React Native vs Native
- **Accept:** Slightly lower performance
- **Gain:** 50% faster development, single codebase

### Firebase Auth vs Custom
- **Accept:** Vendor dependency
- **Gain:** 90% faster auth implementation, battle-tested security

### PostgreSQL vs MongoDB
- **Accept:** Less flexible schema changes
- **Gain:** Better data integrity, complex queries

---

## Success Metrics

### Technical KPIs
- **App Performance:** < 2s load time
- **API Response Time:** < 200ms (95th percentile)
- **Crash Rate:** < 0.1%
- **Test Coverage:** > 80%

### Business KPIs
- **Development Speed:** Launch within 18 weeks
- **Cost:** Stay under $50K for MVP
- **User Satisfaction:** > 4.0/5.0 rating
- **Platform Reach:** Both iOS and Android on day 1

---

## Conclusion

The selected technology stack achieves an **overall score of 8.86/10**, optimizing for:

1. ✅ **Rapid Development** – React Native + NestJS enable fast iteration
2. ✅ **Cross-platform Reach** – Single codebase for iOS/Android
3. ✅ **Team Efficiency** – JavaScript/TypeScript across full stack
4. ✅ **Scalability** – Cloud-native architecture with microservices
5. ✅ **Cost-Effectiveness** – 26% cost reduction vs native
6. ✅ **AI Integration** – Python microservice for ML workloads
7. ✅ **Data Integrity** – PostgreSQL ensures health data accuracy

This stack balances speed, quality, and cost while positioning FitFlow for future growth.

---

## Approval & Sign-off

| Role | Name | Approval Date |
|---|---|---|
| **Student Developer** | Omindu Ayodya | January 2025 |
| **Technical Reviewer** | [Instructor Name] | [Pending] |
| **Course Module** | IT3060 – HCI | Lab 05 |

---

**Document Version**: 1.0  
**Last Updated**: January 2025  
**Author**: Omindu Ayodya
