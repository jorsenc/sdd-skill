# Changelog

All notable changes to the SDD Skill project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-06-25

### ✅ Added
- **EARS Validator** - Complete implementation with 5 patterns
  - Ubiquitous, Event-Driven, State-Driven, Unwanted, Optional
  - Ambiguous term detection (timely, efficient, user-friendly, etc.)
  - Modal verb validation (SHALL vs should/must/will)
  - Keyword capitalization checking
  
- **Phase 0: Constitution** - Complete implementation
  - Interactive questionnaire for project rules
  - Constitution.md generation
  - Professional template

- **Phase 1: Specify** - Basic implementation
  - EARS requirement collection
  - Spec.md generation
  - Interactive interface

- **Core Models**
  - SDDProject - Project state management
  - Specification - EARS requirement modeling
  - RequirementStatement - Individual requirements

- **CLI Orchestrator** (main.py)
  - Conversational mode (full workflow)
  - Phase-specific mode (refine individual phases)
  - Validation mode (`--validate`)
  - GitHub integration mode (`--github` - stub)

- **Documentation**
  - SKILL.md (28KB) - Complete guide to all 7 phases
  - README.md (8KB) - Quick start guide
  - STATUS.md (10KB) - Current status and roadmap
  - examples/simple_api.md - End-to-end example (Todo API)
  - CONTRIBUTING.md - Contribution guidelines
  - CHANGELOG.md - This file

- **Project Artifacts**
  - README.md - Main project overview
  - .gitignore - Proper exclusions
  - requirements.txt - Python dependencies
  - GitHub repository integration

### 🚧 Planned (v0.2)

- **Phases 2-6** - Full implementation
  - Phase 2: Clarify (ambiguity resolution)
  - Phase 3: Plan (OpenAPI/AsyncAPI generation)
  - Phase 4: Tasks (atomic task decomposition)
  - Phase 5: Implement (Claude API code generation)
  - Phase 6: Validate (automated testing and verification)

- **GitHub Integration**
  - Repository creation
  - Issue generation from tasks.md
  - PR creation with generated code
  - Workflow automation

- **Claude API Integration**
  - Code generation from specifications
  - Streaming responses
  - Token optimization
  - Model selection (Sonnet/Opus)

- **Multi-Agent Orchestration**
  - Coordinator agent
  - Implementor agent
  - Verifier agent (adversarial validation)

- **Testing**
  - Unit tests for all modules
  - Integration tests
  - Edge case coverage
  - pytest fixtures

### 🛠️ Technical Details

#### Architecture
- **Language:** Python 3.11+
- **Framework:** CLI with argparse
- **Persistence:** Markdown files + JSON metadata
- **Validation:** Regex-based EARS pattern matching
- **Models:** Dataclass-based with typing

#### File Statistics
- **Python LOC:** ~1,500 lines
- **Documentation:** ~50KB
- **Code Files:** 15 modules
- **Examples:** 1 (Todo API)

#### Dependencies
- pyyaml - OpenAPI/AsyncAPI parsing
- pydantic - Data validation
- requests - HTTP client
- PyGithub - GitHub API
- pytest - Testing framework

## [Unreleased]

### 🚀 Planned for v1.0

- Complete workflow automation (Constitution → Production Code)
- Multi-language code generation support
- Advanced validation (property-based testing, mutation testing)
- CI/CD pipeline integration
- Contract testing (Pact, OpenAPI)
- GraphQL support (alongside REST)
- Database migration generation
- Microservices architecture support

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** - Breaking changes
- **MINOR** - New features (backwards compatible)
- **PATCH** - Bug fixes

## Release Timeline

- **v0.1** (Current) - MVP with Phases 0-1, EARS validator
- **v0.2** - Phases 2-6 implementation
- **v0.3** - Multi-agent orchestration
- **v1.0** - Production-ready complete workflow

## Migration Guide

### From v0.1 to v0.2 (When Released)
- No breaking changes expected
- New phases will be opt-in
- Existing `.specify/` structures remain compatible

## How to Update

```bash
git fetch origin
git pull origin master
pip install -r sdd-skill/requirements.txt --upgrade
```

## Reporting Issues

Found a bug? Check [GitHub Issues](https://github.com/jorsenc/sdd-skill/issues) and create a new one if needed.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to contribute.

---

**Last Updated:** 2026-06-25
