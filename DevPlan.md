# CARET Requirements & MVP Focus

## MVP: Property Investment Tracker

### Core Features (Phase 1)
- **User Authentication:** Secure login and registration.
- **Property Management:** Add, edit, and remove rental properties.
- **Investment Tracking:** 
  - Track purchase price, mortgage, expenses, income, and cash flow for each property.
  - Calculate and display key metrics (ROI, cash-on-cash return, cap rate, etc.).
- **Performance Dashboard:** 
  - Visualize property performance over time.
  - Highlight underperforming properties.
- **Rent Comparison:** 
  - Compare user’s rent to market averages (via integration or manual input).
  - Provide suggestions for rent optimization.
- **Advice & Insights:** 
  - Show actionable tips to improve property performance (e.g., raise rent, reduce expenses).

### Future Add-ons (Phase 2+)
- **Valuation Tracking:** Automated or manual property value updates.
- **Component Tracking:** Track appliances, renovations, and their depreciation.
- **Tax Write-off Advice:** Personalized tax optimization tips.
- **Premium Analytics:** Advanced reporting, AI-driven insights, benchmarking.
- **Professional Advice:** Connect with experts for personalized recommendations.

---

# CARET Development Plan & Timeline

## 1. Project Architecture & Planning
- Define core components: frontend (React), backend (Django), database (PostgreSQL), and optional services (Redis, Celery, AI microservices).
- Establish API contracts and data models.
- Set up version control and branching strategy (main, dev, feature branches).

**Duration:** 1 week

### Core Components
- **Frontend: React** – The user interface for CARET will be built using React, a modern JavaScript library for building scalable and responsive web applications. Users will interact with all features (property management, analytics, reporting, etc.) through this web-based UI, which communicates securely with the backend via REST APIs.
- **Backend: Django** – The backend will be developed with Django, a robust Python web framework. Django will handle all business logic, user authentication, API endpoints, and integration with external services (e.g., real estate APIs, payment gateways). It will serve as the central hub connecting the frontend, database, and any background services.
- **Database: PostgreSQL** – PostgreSQL will be used as the primary data store. It is an open-source, enterprise-grade relational database system that supports advanced SQL features and ensures data integrity. All persistent data—such as user accounts, property records, transactions, and analytics—will be stored here. The backend will interact with PostgreSQL using Django’s ORM, and the database will be containerized for portability and easy backup.

**How these components work together:**
- The **frontend** (React) is served to users via a web server (e.g., Nginx) and provides a seamless, interactive experience.
- When a user performs an action (e.g., logs in, adds a property, views analytics), the frontend sends a request to the **backend** (Django) via a REST API.
- The **backend** processes the request, applies business logic, interacts with the **database** (PostgreSQL) to read or write data, and returns a response to the frontend.
- All components are containerized and orchestrated together, ensuring that the system is modular, scalable, and easy to deploy both locally and in production environments.
- Optional services (such as Redis for caching, Celery for background tasks, or AI microservices for advanced analytics) can be added as separate containers and integrated with the backend as needed.

This architecture allows for:
- Independent development and scaling of each component
- Easy updates and maintenance
- Secure, reliable, and high-performance operation in both self-hosted and managed deployments

---

## 2. Containerization
- Write Dockerfiles for each component:
  - Frontend: Build and serve with Nginx.
  - Backend: Django app with Gunicorn/Uvicorn.
  - Database: Use official PostgreSQL image.
  - (Optional) Redis, Celery, AI services.
- Test each container independently.

**Duration:** 1 week

---

## 3. Local Orchestration with Docker Compose
- Create a `docker-compose.yml` to orchestrate all services.
- Set up environment variables and secrets for local development.
- Test the full stack locally: frontend ↔ backend ↔ database.

**Duration:** 1 week

---

## 4. Kubernetes (K8s) Setup
- Install Minikube or Kind for local K8s testing.
- Write K8s manifests for:
  - Deployments (frontend, backend, db, etc.)
  - Services (ClusterIP for backend/db, NodePort/Ingress for frontend)
  - PersistentVolumeClaims for database data
  - ConfigMaps and Secrets for configuration
- Test deployment locally on Minikube.

**Duration:** 2 weeks

---

## 5. CI/CD Pipeline
- Set up GitHub Actions or GitLab CI for:
  - Linting, testing, and building Docker images
  - Pushing images to a container registry
  - Deploying to K8s (staging/production) via manifests or Helm charts

**Duration:** 1 week

---

## 6. Production Deployment
- Select a cloud provider (e.g., DigitalOcean, AWS, GCP) or on-prem K8s.
- Set up managed K8s cluster or self-hosted K8s.
- Configure domain, TLS/SSL, and Ingress controller.
- Set up monitoring (Prometheus, Grafana) and logging (ELK stack or similar).
- Implement backup and disaster recovery for the database.

**Duration:** 2 weeks

---

## 7. Documentation & Support
- Write user and admin setup guides.
- Document deployment, scaling, and troubleshooting.
- Set up community support channels (e.g., GitHub Discussions, Discord).

**Duration:** Ongoing, initial draft in 1 week

---

## 8. Optional Managed Hosting & Premium Features
- Develop managed hosting automation (scripts, dashboards).
- Integrate premium features (AI analytics, professional advice, etc.).
- Set up billing and user management for hosted service.

**Duration:** 2–4 weeks (after core is stable)

---

## 9. User Interaction Flow (React ↔ Django)

### Typical Modern Flow

1. **User fills out a form in React**
   - Example: Registration, login, or CRUD action.
2. **React sends HTTP request to Django REST API**
   - Uses fetch/axios to send data to endpoints (e.g., `/api/register/`, `/api/login/`, `/api/properties/`).
3. **Django receives request and processes it**
   - Validates/authenticates input.
   - Performs business logic and interacts with the database.
4. **Django returns a JSON response**
   - Contains success, error, or requested data.
5. **React processes the response**
   - Updates UI, stores tokens (for authentication), displays errors, or redirects as needed.

#### Authentication Patterns
- **Token-based (recommended):**
  - Django issues a JWT or similar token on login.
  - React stores the token (localStorage/cookies) and sends it with each request (usually in the Authorization header).

#### CRUD Operations
- React sends GET/POST/PUT/DELETE requests to Django endpoints.
- Django checks authentication, performs DB operations, and returns results as JSON.

---

### Example: User Registration (Token-based)

```
// React (frontend)
function handleRegister(formData) {
    fetch('/api/register/', {
        method: 'POST',
        body: JSON.stringify(formData),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Redirect to login or dashboard
        } else {
            // Show error messages
        }
    });
}

// Django (backend)
@api_view(['POST'])
def register(request):
    data = request.data
    # Validate data
    # Create user
    # Return response (success/error)
```

_Repeat similar structure for login, CRUD, and logout._

---

## Timeline

| Phase                        | Duration         |
|------------------------------|------------------|
| Architecture & Planning      | 1 week           |
| Containerization             | 1 week           |
| Docker Compose Orchestration | 1 week           |
| Kubernetes Setup             | 2 weeks          |
| CI/CD Pipeline               | 1 week           |
| Production Deployment        | 2 weeks          |
| Documentation & Support      | 1 week (ongoing) |
| Managed Hosting & Premium    | 2–4 weeks        |
| **Total**                    | **10–13 weeks**  |

---
