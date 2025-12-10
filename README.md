# DevOpsCA3 - Calorie Counter Application

## Overview
A Python-based calorie tracking application with both CLI and web interfaces, featuring a complete CI/CD pipeline with automated testing, security scanning, and multi-environment deployment.

## Technologies Used
- **Backend**: Python 3.12, Flask
- **Testing**: pytest, Selenium WebDriver, coverage
- **Security**: Bandit (SAST), Safety (dependency scanning)
- **CI/CD**: Azure DevOps Pipelines
- **Code Quality**: pylint, code coverage (95% minimum)

## Local Development Setup
```bash
# Clone repository
git clone <repository-url>
cd DevOpsCA3

# Install dependencies
pip install -r requirements.txt

# Run CLI application
python -m calorie_counter.app

# Run web application
python web_app.py
# Access at http://localhost:8000
```

## Application Features
- Add food items with calorie counts
- View daily total calories
- Reset daily tracking
- Web interface for remote access
- Input validation and error handling

## CI Pipeline Implementation
### Multi-Stage Pipeline
1. **Build Stage**: Unit tests, coverage, static analysis, security scanning
2. **Test Environment**: Deployment and UAT testing
3. **Production Stage**: Production deployment (main branch only)

### Branch Policies and Protection
- Triggers on `main` and `dev` branches
- Production deployment restricted to `main` branch
- All tests must pass before deployment
- **Note**: GitHub branch protection requires paid account for private repos
- **Alternative**: Azure DevOps environment approval gates provide equivalent protection

## Testing Strategy
### Unit Testing
- pytest framework with 95% code coverage requirement
- Tests for core calculator functionality
- Input validation and error handling tests

### Security Testing
- **Bandit**: Static Application Security Testing (SAST)
- **Safety**: Dependency vulnerability scanning
- Input validation tests for XSS and injection protection

### Performance Testing
- Load testing for large datasets (1000+ food items)
- Response time validation (<1 second for operations)
- Memory usage optimization tests

### UAT Testing with Selenium
- Automated browser testing of web interface
- End-to-end user workflow validation
- Cross-browser compatibility testing

## Environment Setup and Configuration

### Azure DevOps Environment Setup
**To enable deployment stages, create environments in Azure DevOps:**

1. Go to Azure DevOps → Pipelines → Environments
2. Create new environment named `test`
3. Create new environment named `production`
4. For production environment:
   - Add approval gate: Settings → Approvals → Add your user
   - Set required approvers before deployment
5. Switch to `azure-pipeline-with-environments.yml` when ready

### Test Environment
- Automated deployment after successful build
- UAT test execution
- Health check validation

### Production Environment
- Manual approval gate (configured in Azure DevOps)
- Blue-green deployment strategy
- Rollback capabilities

## Deployment Process
1. Code commit triggers pipeline
2. Build stage: Tests, security scans, artifact creation
3. Test deployment: Automated UAT execution
4. Production approval: Manual gate for production deployment
5. Production deployment: Artifact deployment with health checks

## Pipeline Approval Gates
- **Test to Production**: Manual approval required
- **Environment Protection**: Configured in Azure DevOps environments
- **Branch Protection**: Production deploys only from main branch

## Troubleshooting Guide
### Common Issues
- **Coverage Failure**: Ensure all code paths are tested (95% minimum)
- **Security Scan Failures**: Review Bandit and Safety reports
- **UAT Test Failures**: Check Selenium WebDriver configuration
- **Deployment Issues**: Verify environment configurations and secrets

### Debug Commands
```bash
# Run specific test suites
python -m pytest tests/test_calculator.py -v
python -m pytest tests/test_security.py -v
python -m pytest tests/test_performance.py -v

# Security scanning
bandit -r calorie_counter/
safety check

# Coverage report
coverage run -m pytest
coverage report
```
