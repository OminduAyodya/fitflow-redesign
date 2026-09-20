# Contributing to FitFlow

Thank you for your interest in contributing to FitFlow! This document provides guidelines for contributing to the project.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## 🚀 Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/Chenuka01/fitflow-redesign.git
   cd fitflow-redesign
   ```

2. **Install dependencies**
   ```bash
   # Frontend
   cd frontend && npm install

   # Backend
   cd ../backend && npm install

   # AI Service
   cd ../ai-service && pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy example files
   cp backend/.env.example backend/.env
   cp ai-service/.env.example ai-service/.env
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🔄 Development Workflow

### Branch Naming Convention
- `feature/feature-name` - New features
- `bugfix/bug-description` - Bug fixes
- `hotfix/critical-fix` - Critical production fixes
- `docs/documentation-update` - Documentation changes

### Commit Message Format
```
type(scope): subject

body (optional)

footer (optional)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Build/config changes

**Example:**
```
feat(workout): add AI workout generation endpoint

Implement POST /api/v1/workouts/generate endpoint that uses
ML model to create personalized workout plans.

Closes #123
```

## 📝 Code Standards

### TypeScript/JavaScript (Frontend & Backend)
- Use TypeScript for type safety
- Follow ESLint configuration
- Use Prettier for formatting
- Write unit tests for new features
- Minimum 80% code coverage

### Python (AI Service)
- Follow PEP 8 style guide
- Use type hints
- Write docstrings for functions
- Use pytest for testing
- Format code with Black

### General Guidelines
- Keep functions small and focused
- Write self-documenting code
- Add comments for complex logic
- Update documentation with code changes

## 🔍 Testing

### Frontend
```bash
cd frontend
npm test
npm run test:coverage
```

### Backend
```bash
cd backend
npm test
npm run test:e2e
```

### AI Service
```bash
cd ai-service
pytest tests/
pytest --cov=./ tests/
```

## 📤 Pull Request Process

1. **Update your branch**
   ```bash
   git checkout main
   git pull origin main
   git checkout feature/your-feature
   git rebase main
   ```

2. **Run tests**
   - Ensure all tests pass
   - Add new tests for your changes
   - Verify code coverage

3. **Create Pull Request**
   - Use descriptive title
   - Reference related issues
   - Describe changes made
   - Include screenshots for UI changes

4. **PR Template**
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Unit tests pass
   - [ ] E2E tests pass
   - [ ] Manual testing completed

   ## Screenshots (if applicable)

   ## Related Issues
   Closes #issue_number
   ```

5. **Review Process**
   - Address review comments
   - Update PR as needed
   - Ensure CI/CD passes

## 🐛 Reporting Issues

### Bug Reports
Include:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots/error messages
- Environment details (OS, versions)

### Feature Requests
Include:
- Clear use case
- Proposed solution
- Alternative solutions considered
- Impact on existing features

## 📚 Documentation

- Update README.md for feature changes
- Update API documentation
- Add inline code comments
- Create ADRs for architectural decisions

## 💬 Code Review Guidelines

### As a Reviewer
- Be respectful and constructive
- Explain the "why" behind suggestions
- Approve when satisfied
- Request changes when needed

### As an Author
- Respond to all comments
- Ask questions if unclear
- Make requested changes
- Keep PR scope focused

## 🎯 Best Practices

1. **Write Clean Code**
   - DRY (Don't Repeat Yourself)
   - SOLID principles
   - Clear naming conventions

2. **Security**
   - Never commit secrets/credentials
   - Validate all inputs
   - Use parameterized queries
   - Follow OWASP guidelines

3. **Performance**
   - Optimize database queries
   - Minimize API calls
   - Cache when appropriate
   - Profile before optimizing

4. **Accessibility**
   - Follow WCAG 2.1 guidelines
   - Test with screen readers
   - Use semantic HTML
   - Provide alt text

## 📞 Getting Help

- Open an issue for bugs/features
- Tag maintainer for urgent matters
- Join discussions on GitHub

## 📄 License

By contributing, you agree that your contributions will be licensed under the project's license.

---

**Thank you for contributing to FitFlow!** 🏋️

**Project Maintainer**: Omindu Ayodya  
**Module**: IT3060 – Human Computer Interaction
