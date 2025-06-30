# TAPRE Requirements & MVP Focus

## MVP: Property Investment Tracker

### Core Features (Phase 1)
- **User Authentication:** Secure login and registration.
  - Uses JWT authentication.
- **Property Management:** Add, edit, and remove rental properties.
  - CRUD operations for properties with details like address, purchase price, mortgage info, etc.
- **Investment Tracking:** 
  - Track purchase price, mortgage, expenses, income, and cash flow for each property.
  - Calculate and display key metrics (ROI, cash-on-cash return, cap rate, etc.).
- **Performance Dashboard:** 
  - Visualize property performance over time.
  - Highlight underperforming properties.
- **Rent Comparison:** 
  - Compare user’s rent to market averages (via integration or manual input).
  - Provide suggestions for rent optimization.
  - Calculate profit margin and compare it to market standards.
- **Advice & Insights:** 
  - Show actionable tips to improve property performance (e.g., raise rent, reduce expenses).

### Future Add-ons (Phase 2+)
- **Valuation Tracking:** Automated or manual property value updates.
- **Component Tracking:** Track appliances, renovations, and their depreciation.
- **Tax Write-off Advice:** Personalized tax optimization tips.
- **Premium Analytics:** Advanced reporting, AI-driven insights, benchmarking.
- **Professional Advice:** Connect with experts for personalized recommendations.

---

# TAPRE Development Plan & Timeline

## 1. Project Architecture & Planning ✅
- Define core components: frontend (Vue.js), backend (Go/Gin), database (PostgreSQL), and optional services (AI microservices).
- Establish API contracts and data models.
- Set up version control and branching strategy (main, dev, feature branches).

**Duration:** 1 week

### Core Components
- **Frontend: Vue.js** – The user interface for TAPRE will be built using Vue.js, a modern JavaScript framework for building scalable and responsive web applications. Users will interact with all features (property management, analytics, reporting, etc.) through this web-based UI, which communicates securely with the backend via REST APIs.
- **Backend: Go (Gin)** – The backend will be developed with Go using the Gin framework. Gin will handle all business logic, user authentication, API endpoints, and integration with external services (e.g., real estate APIs, payment gateways). It will serve as the central hub connecting the frontend, database, and any background services. The framework will be as follows:
  - Finances: `Account`, `Transaction`, `Expense`, `Income`, `Mortgage`
  - Properties: `BuildDate`, `Address`, `City`, `State`, `Zip`, `Country`, `Type`, `Size`, `PurchasePrice`, `CurrentValue`
  - Tenants: `Name`, `Email`, `Phone`, `LeaseStart`, `LeaseEnd`, `Property`, `Deposit`, `RentAmount`
  - Receipts: `Date`, `Amount`, `Category`, `Property`, `Tenant`
  - Users: `Username`, `Email`, `Password`, `Role`
  - Documents: `FileName`, `FileType`, `UploadDate`, `Property`, `Tenant`
- **Database: PostgreSQL** – PostgreSQL will be used as the primary data store. All persistent data—such as user accounts, property records, transactions, and analytics—will be stored here. The backend will interact with PostgreSQL using Go database drivers and ORM libraries. The database will be containerized for portability and easy backup.

**How these components work together:**
- The **frontend** (Vue.js) is served to users via a web server (e.g., Nginx) and provides a seamless, interactive experience.
- When a user performs an action (e.g., logs in, adds a property, views analytics), the frontend sends a request to the **backend** (Go/Gin) via a REST API.
- The **backend** processes the request, applies business logic, interacts with the **database** (PostgreSQL) to read or write data, and returns a response to the frontend.
- All components are containerized and orchestrated together, ensuring that the system is modular, scalable, and easy to deploy both locally and in production environments.
- Optional services (such as AI microservices for advanced analytics) can be added as separate containers and integrated with the backend as needed.

This architecture allows for:
- Independent development and scaling of each component
- Easy updates and maintenance
- Secure, reliable, and high-performance operation in both self-hosted and managed deployments

---

## 2. MVP Implementation
- Develop core features: authentication, property management, investment tracking, dashboard, rent comparison, advice/insights.
- Build RESTful API endpoints in Go (Gin).
- Build Vue.js UI for all MVP features.
- Integrate frontend and backend.
- Write unit and integration tests.

**Duration:** 6-8 weeks

---

## 3. Deployment & Containerization
- Write Dockerfiles for each component:
  - Frontend: Build and serve with Nginx.
  - Backend: Go (Gin) app.
  - Database: Use official PostgreSQL image.
- Test each container independently.
- Create a `docker-compose.yml` to orchestrate all services.
- Set up environment variables and secrets for local development.
- Test the full stack locally: frontend ↔ backend ↔ database.

**Duration:** 2 weeks

---

## 4. Financial Optimization Tools
- Implement tax optimization, deduction suggestions, and tax software integration.
- Add landlord tax guides and related UI/UX.

**Duration:** 2-3 weeks

---

## 5. Mobile App
- Develop a React Native app for on-the-go management.
- Integrate with backend REST API.
- Focus on core features: property management, notifications, and dashboard.

**Duration:** 3-4 weeks

---

## 6. AI-Driven Insights
- Implement portfolio analytics, ROI/cash flow advice, predictive trends, and advanced analytics.
- Integrate AI microservices as needed.

**Duration:** 2-3 weeks

---

## 7. Local Service Marketplace
- Build provider listings, booking interface, and commission system.
- Integrate with core platform and user accounts.

**Duration:** 2-3 weeks

---

## 8. Documentation & Support
- Write user and admin setup guides.
- Document deployment, scaling, and troubleshooting.
- Set up community support channels (e.g., GitHub Discussions, Discord).

**Duration:** Ongoing, initial draft in 1 week

---

## 9. Optional Managed Hosting & Premium Features
- Develop managed hosting automation (scripts, dashboards).
- Integrate premium features (AI analytics, professional advice, etc.).
- Set up billing and user management for hosted service.

**Duration:** 2–4 weeks (after core is stable)

---

## 10. User Interaction Flow (Vue.js ↔ Go/Gin)

### Typical Modern Flow

1. **User fills out a form in Vue.js**
   - Example: Registration, login, or CRUD action.
2. **Vue.js sends HTTP request to Go/Gin REST API**
   - Uses fetch/axios to send data to endpoints (e.g., `/api/register`, `/api/login`, `/api/properties`).
3. **Go/Gin receives request and processes it**
   - Validates/authenticates input.
   - Performs business logic and interacts with the database.
4. **Go/Gin returns a JSON response**
   - Contains success, error, or requested data.
5. **Vue.js processes the response**
   - Updates UI, stores tokens (for authentication), displays errors, or redirects as needed.

#### Authentication Patterns
- **Token-based (recommended):**
  - Go/Gin issues a JWT or similar token on login.
  - Vue.js stores the token (localStorage/cookies) and sends it with each request (usually in the Authorization header).

#### CRUD Operations
- Vue.js sends GET/POST/PUT/DELETE requests to Go/Gin endpoints.
- Go/Gin checks authentication, performs DB operations, and returns results as JSON.

---

### Example: User Registration (Token-based)

```js
// Vue.js (frontend)
function handleRegister(formData) {
    fetch('/api/register', {
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

// Go (Gin) (backend)
r.POST("/api/register", func(c *gin.Context) {
    var data RegisterRequest
    if err := c.ShouldBindJSON(&data); err != nil {
        c.JSON(400, gin.H{"error": "Invalid input"})
        return
    }
    // Validate data, create user, return response
})
```

_Repeat similar structure for login, CRUD, and logout._

---

## Timeline

| Phase                        | Duration         |
|------------------------------|------------------|
| Architecture & Planning      | 1 week           |
| MVP Implementation           | 6-8 weeks        |
| Deployment & Containerization| 2 weeks          |
| Financial Optimization Tools | 2-3 weeks        |
| Mobile App                   | 3-4 weeks        |
| AI-Driven Insights           | 2-3 weeks        |
| Local Service Marketplace    | 2-3 weeks        |
| Documentation & Support      | 1 week (ongoing) |
| Managed Hosting & Premium    | 2–4 weeks        |
| **Total**                    | **20–30 weeks**  |

---
