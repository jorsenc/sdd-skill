# Ejemplo: Simple Todo API con SDD

Este documento muestra un ejemplo end-to-end de cómo usar el SDD Skill para crear una API simple de gestión de tareas.

## Phase 0: Constitution

```
Lenguaje: TypeScript
Framework: Express.js
Database: PostgreSQL
Testing: Jest
Min Coverage: 80%
Password Hash: bcrypt cost 12
Session: JWT tokens
Architecture: Clean (controllers/services/models)
```

## Phase 1: Specification (EARS)

```
# Todo API Specification

## Ubiquitous Requirements
The system SHALL hash passwords using bcrypt with cost factor 12.
The system SHALL store all timestamps in UTC timezone.
The system SHALL validate email format using RFC 5322 regex.

## Event-Driven Requirements
WHEN a user submits the registration form, THE system SHALL:
  1. Validate email uniqueness
  2. Hash password
  3. Create user record
  4. Return JWT token

WHEN a user clicks "Create Todo", THE system SHALL:
  1. Validate todo title (1-500 chars)
  2. Create record with created_at timestamp
  3. Return todo object

WHEN user fetches todos, THE system SHALL return paginated list (limit 50).

## State-Driven Requirements
WHILE user has active JWT, THE system SHALL:
  1. Accept authenticated requests
  2. Attach user_id to request context

WHILE JWT is expired, THE system SHALL reject request with HTTP 401.

## Unwanted Behavior
IF registration email already exists, THEN return HTTP 400 with message.
IF password < 8 characters, THEN return HTTP 400.
IF JWT token invalid, THEN return HTTP 401.
IF todo title empty, THEN return HTTP 400.
IF user tries to update someone else's todo, THEN return HTTP 403.

## Optional Requirements
WHERE multi-language support enabled, THE system SHALL translate API responses.
```

## Phase 2: Clarify

Questions resolved:
1. **Pagination**: Use offset/limit (cursor-based optional for v2)
2. **Soft delete**: Keep todos with deleted_at timestamp
3. **Rate limiting**: 100 requests/minute per user
4. **CORS**: Allow localhost:3000 and example.com

## Phase 3: Technical Plan

**Database Schema:**
```
users
  - id (UUID primary key)
  - email (unique)
  - password_hash (bcrypt)
  - created_at (UTC timestamp)
  - updated_at (UTC timestamp)

todos
  - id (UUID primary key)
  - user_id (FK to users)
  - title (varchar 500)
  - description (text, nullable)
  - completed (boolean, default false)
  - deleted_at (nullable, for soft delete)
  - created_at (UTC timestamp)
  - updated_at (UTC timestamp)
```

**API Endpoints (OpenAPI):**
```yaml
POST /auth/register
  Request: { email, password }
  Response: { token, user_id }
  Errors: 400 (email exists), 400 (invalid email/password)

POST /auth/login
  Request: { email, password }
  Response: { token }
  Errors: 401 (invalid credentials)

POST /todos (auth required)
  Request: { title, description }
  Response: { id, title, completed, created_at }
  Errors: 400 (invalid), 401 (unauthorized)

GET /todos (auth required)
  Query: ?limit=50&offset=0
  Response: { todos: [], total_count }
  Errors: 401 (unauthorized)

PUT /todos/{id} (auth required)
  Request: { title, completed }
  Response: { id, title, completed, updated_at }
  Errors: 400, 401, 403 (not owner), 404 (not found)

DELETE /todos/{id} (auth required)
  Response: { deleted: true }
  Errors: 401, 403 (not owner), 404
```

## Phase 4: Task Decomposition

```
Task 1: Create project structure
  - Create directories: src/{models,services,controllers,middleware}
  - Create package.json with dependencies
  - Setup TypeScript config
  - Files: package.json, tsconfig.json
  - Success: npm install works

Task 2: Create User model and database migration
  - Implement users table schema
  - Create User TypeScript interface
  - Create UserRepository (database access)
  - Files: src/models/User.ts, migrations/001_create_users.sql
  - Success: Migration runs without errors

Task 3: Implement password hashing utility
  - Create bcrypt wrapper with cost 12
  - Implement hash() and verify() functions
  - Add unit tests
  - Files: src/utils/password.ts, src/utils/password.test.ts
  - Success: All tests pass, coverage 100%

Task 4: Create authentication service
  - Implement register(email, password) → JWT
  - Implement login(email, password) → JWT
  - Add JWT validation
  - Files: src/services/AuthService.ts, src/services/AuthService.test.ts
  - Success: All unit tests pass

Task 5: Create authentication endpoints
  - POST /auth/register
  - POST /auth/login
  - Implement error handling
  - Files: src/controllers/AuthController.ts
  - Success: E2E tests pass

Task 6: Create Todo model
  - Implement todos table schema
  - Create Todo interface
  - Create TodoRepository
  - Files: src/models/Todo.ts, migrations/002_create_todos.sql
  - Success: Migration runs without errors

Task 7: Create Todo service
  - Implement CRUD operations
  - Implement pagination
  - Implement soft delete
  - Files: src/services/TodoService.ts
  - Success: Unit tests pass, 100% coverage

Task 8: Create Todo endpoints
  - POST/GET/PUT/DELETE /todos
  - Implement authorization checks
  - Files: src/controllers/TodoController.ts
  - Success: E2E tests pass

Task 9: Add middleware for auth validation
  - Implement JWT verification middleware
  - Add error handling
  - Files: src/middleware/auth.ts
  - Success: Middleware prevents unauthorized access

Task 10: Setup complete API
  - Wire all controllers to Express app
  - Setup error handling
  - Setup CORS
  - Files: src/app.ts, src/server.ts
  - Success: Server starts, health check works

Task 11: Add comprehensive tests
  - Unit tests for all services
  - Integration tests for API endpoints
  - Property-based tests for edge cases
  - Files: src/**/*.test.ts
  - Success: Coverage 80%+

Task 12: Setup CI/CD
  - GitHub Actions for tests
  - Setup linting
  - Setup type checking
  - Files: .github/workflows/ci.yml
  - Success: All checks pass
```

## Phase 5: Implementation

El skill orquesta Coordinator + Implementor + Verifier para generar código:

1. **Coordinator** lee constitution, spec, plan
2. **Implementor** genera código TypeScript según plan
3. **Verifier** audita código contra constitution

Output: Código completo en src/, tests en src/**/*.test.ts

## Phase 6: Validation

```
✅ All tests pass (coverage 80%+)
✅ Code respects OpenAPI contracts
✅ No EARS syntax violations
✅ TypeScript strict mode passes
✅ ESLint passes
✅ No hardcoded secrets
✅ Database migrations reversible
```

## Resultado Final

Un repositorio Git listo para producción:

```
todo-api/
├── .specify/
│   ├── constitution.md
│   └── features/001-main/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
├── src/
│   ├── models/
│   ├── services/
│   ├── controllers/
│   ├── middleware/
│   ├── utils/
│   ├── app.ts
│   ├── server.ts
│   └── **/*.test.ts
├── migrations/
│   ├── 001_create_users.sql
│   └── 002_create_todos.sql
├── .github/workflows/ci.yml
├── package.json
├── tsconfig.json
├── .env.example
└── README.md
```

Todos los artefactos SDD (spec, plan, tasks) versionados junto al código. Listos para auditoría, compliance, mantenimiento.
