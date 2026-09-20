# 🚀 FitFlow Quick Start Guide

**Student**: Omindu Ayodya  
**Module**: IT3060 – HCI Lab 05

---

## 📤 Push to GitHub (IMPORTANT - Do This First!)

Your repository has diverged from the remote. Follow these steps:

```bash
# Navigate to project directory
cd fitflow-redesign

# Option 1: Force push (recommended for initial setup)
git push origin main --force

# Option 2: Pull and merge first (if you want to keep remote changes)
git pull origin main --rebase
git push origin main
```

**Recommended**: Use Option 1 (force push) since this is your initial project setup.

---

## 🎯 What's Been Completed

✅ **Complete folder structure** for frontend, backend, and ai-service  
✅ **38 files created** with comprehensive documentation  
✅ **All Lab 05 activities** documented (Activities 1-4)  
✅ **3 Architecture Decision Records** (ADRs)  
✅ **CI/CD pipeline** configured with GitHub Actions  
✅ **Database schema** designed with Prisma  
✅ **2 Git commits** made locally  

---

## 📁 Project Structure Overview

```
fitflow-redesign/
├── frontend/          # React Native + Expo mobile app
├── backend/           # Node.js + NestJS API
├── ai-service/        # Python + FastAPI ML service
├── docs/              # All documentation & activities
│   ├── activity1-frontend-comparison.md
│   ├── activity2-backend-comparison.md
│   ├── activity3-decision-matrix.md
│   ├── activity4-architecture.md
│   ├── TECH_STACK_SUMMARY.md
│   └── adr/           # Architecture Decision Records
├── .github/workflows/ # CI/CD configuration
├── README.md          # Main project documentation
├── CONTRIBUTING.md    # Development guidelines
└── PROJECT_SETUP_COMPLETE.md  # Setup summary
```

---

## 💻 Local Development Setup

### 1. Install Prerequisites

```bash
# Node.js (v18+)
node --version

# Python (v3.11+)
python --version

# Expo CLI
npm install -g expo-cli
```

### 2. Install Dependencies

```bash
# Frontend
cd frontend
npm install

# Backend
cd ../backend
npm install

# AI Service
cd ../ai-service
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Backend
cp backend/.env.example backend/.env
# Edit backend/.env with your database credentials

# AI Service
cp ai-service/.env.example ai-service/.env
# Edit ai-service/.env with your configuration
```

### 4. Setup Database

```bash
cd backend
npx prisma migrate dev --name init
npx prisma generate
```

### 5. Start Development Servers

**Terminal 1 - Frontend:**
```bash
cd frontend
npx expo start
```

**Terminal 2 - Backend:**
```bash
cd backend
npm run start:dev
```

**Terminal 3 - AI Service:**
```bash
cd ai-service
uvicorn main:app --reload
```

---

## 🌐 Access Points

Once running:
- **Mobile App**: Use Expo Go app and scan QR code
- **Backend API**: http://localhost:3000
- **API Docs**: http://localhost:3000/api (Swagger)
- **AI Service**: http://localhost:8000
- **AI Docs**: http://localhost:8000/docs (Swagger)

---

## 📋 Key Files to Review

### For Submission
1. `README.md` - Main project overview
2. `docs/activity1-frontend-comparison.md` - Frontend evaluation
3. `docs/activity2-backend-comparison.md` - Backend evaluation
4. `docs/activity3-decision-matrix.md` - Decision matrix
5. `docs/activity4-architecture.md` - System architecture
6. `docs/TECH_STACK_SUMMARY.md` - Technology summary
7. `PROJECT_SETUP_COMPLETE.md` - Setup completion checklist

### For Development
1. `frontend/README.md` - Frontend setup guide
2. `backend/README.md` - Backend setup guide
3. `ai-service/README.md` - AI service guide
4. `CONTRIBUTING.md` - Development guidelines

---

## 🎓 Submission Checklist

- [ ] Push repository to GitHub: `git push origin main --force`
- [ ] Verify all files are visible on GitHub
- [ ] Ensure README displays correctly
- [ ] Check documentation is accessible
- [ ] Confirm folder structure matches requirements
- [ ] Submit GitHub repository link to instructor

---

## 📊 Repository Statistics

- **Total Commits**: 2
- **Total Files**: 39
- **Documentation Lines**: ~3,800+
- **Tech Stack Score**: 8.86/10
- **Activities Completed**: 5/5

---

## 🔗 Important Links

- **GitHub Repo**: https://github.com/Chenuka01/fitflow-redesign
- **React Native Docs**: https://reactnative.dev/
- **NestJS Docs**: https://docs.nestjs.com/
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Expo Docs**: https://docs.expo.dev/

---

## 🐛 Common Issues & Solutions

### Issue: Git divergence error
**Solution**: Use `git push origin main --force` for initial setup

### Issue: Port already in use
**Solution**: Kill process or change port in configuration

### Issue: Database connection error
**Solution**: Check PostgreSQL is running and .env is configured

### Issue: Expo not loading
**Solution**: Clear cache: `npx expo start -c`

### Issue: Python dependencies fail
**Solution**: Create virtual environment first: `python -m venv venv`

---

## 💡 Tips

- Use VS Code for best development experience
- Install recommended extensions (ESLint, Prettier, Prisma)
- Keep environment variables secure (never commit .env)
- Run tests before committing: `npm test`
- Use feature branches for development
- Follow commit message conventions

---

## 🎉 You're All Set!

Your FitFlow project is fully configured and ready for development or submission.

**Next Step**: Push to GitHub using the command above!

---

**Created By**: Omindu Ayodya  
**Module**: IT3060 – Human Computer Interaction  
**Lab**: Lab Exercise 05  
**Date**: January 2025
