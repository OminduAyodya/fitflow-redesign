# 📱 FitFlow Frontend – React Native (Expo)

## Overview

The FitFlow mobile application is built with React Native using Expo for cross-platform development (iOS & Android).

## 🛠️ Tech Stack

- **Framework**: React Native 0.73+
- **Build Tool**: Expo SDK 50+
- **Navigation**: React Navigation 6.x
- **State Management**: Zustand / Redux Toolkit
- **UI Components**: React Native Paper / NativeBase
- **API Client**: Axios
- **Authentication**: Firebase Auth

## 📁 Project Structure

```
frontend/
├── src/
│   ├── screens/          # Screen components
│   │   ├── HomeScreen.tsx
│   │   ├── WorkoutScreen.tsx
│   │   ├── NutritionScreen.tsx
│   │   └── ProfileScreen.tsx
│   ├── components/       # Reusable UI components
│   │   ├── WorkoutCard.tsx
│   │   ├── NutritionTracker.tsx
│   │   └── ProgressChart.tsx
│   ├── navigation/       # Navigation configuration
│   │   └── AppNavigator.tsx
│   ├── services/         # API services
│   │   ├── api.ts
│   │   └── auth.ts
│   ├── store/            # State management
│   │   └── index.ts
│   └── utils/            # Utility functions
├── assets/               # Images, fonts, icons
├── app.json              # Expo configuration
├── package.json
└── tsconfig.json
```

## 🚀 Getting Started

### Prerequisites

- Node.js >= 18.x
- npm or yarn
- Expo CLI: `npm install -g expo-cli`
- Expo Go app (for testing on physical device)

### Installation

```bash
# Install dependencies
npm install

# Start development server
npx expo start

# Run on specific platform
npx expo start --ios
npx expo start --android
```

## 📦 Key Dependencies

```json
{
  "expo": "~50.0.0",
  "react": "18.2.0",
  "react-native": "0.73.0",
  "react-navigation": "^6.0.0",
  "axios": "^1.6.0",
  "firebase": "^10.7.0"
}
```

## 🧪 Testing

```bash
# Run tests
npm test

# Run with coverage
npm run test:coverage
```

## 📱 Features

- ✅ Cross-platform mobile app (iOS & Android)
- ✅ AI-powered workout recommendations
- ✅ Camera-based nutrition tracking
- ✅ Social challenges and leaderboards
- ✅ Real-time progress tracking
- ✅ Push notifications

## 👨‍💻 Developer

**Omindu Ayodya**  
IT3060 – Human Computer Interaction
