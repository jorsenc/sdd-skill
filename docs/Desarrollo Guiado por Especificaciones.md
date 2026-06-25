# **Spec-Driven Development: Architectural Governance and Contractual Engineering in the Age of Autonomous Agents**

## **The Evolution of Developmental Discipline: From Waterfall to Agentic Workflows**

The historical trajectory of software engineering methodologies reflects a continuous struggle to balance operational velocity with system predictability1. During the classical Software Development Life Cycle (SDLC) era, predictability was enforced through highly structured, sequential phases where business requirements were codified in exhaustive, static Product Requirement Documents (PRDs)2. While this front-loaded discipline mitigated ambiguity, its inherent rigidity slowed innovation, leaving little room for iterative feedback and rapid deployment2.  
To reconcile these tensions, the industry pivoted toward Agile methodologies and developer-centric verification models2. Test-Driven Development (TDD) introduced an executable verification loop by requiring engineers to author failing test cases before implementing functional code1. Behavior-Driven Development (BDD) subsequently abstracted this concept into human-readable, behavior-focused "Given-When-Then" scenarios, aiming to bridge the communication gap between business analysts and technical implementers2.  
However, both TDD and BDD were designed under the fundamental assumption that human engineers would remain the sole authors of software code2. The rapid mainstreaming of generative artificial intelligence, agentic IDEs, and autonomous coding agents has shattered this paradigm1. In modern, AI-assisted workflows, code generation has ceased to be the operational bottleneck; instead, the limiting factor has shifted entirely to the precise capture, communication, and validation of intent across the software lifecycle4.

| Methodology | Primary Artifact | Intended Reader | Core Value | Major Limitation |
| :---- | :---- | :---- | :---- | :---- |
| **Traditional SDLC (Waterfall)** | Static PRD & Architecture Diagrams1 | Humans only7 | Structured, predictable planning2 | Severe rigidity; documentation quickly drifts and rots2 |
| **Test-Driven Development (TDD)** | Executable Unit Tests1 | Human developers and CI/CD runners2 | Code correctness and modular design10 | Does not inherently capture high-level product intent11 |
| **Behavior-Driven Development (BDD)** | Gherkin / Given-When-Then Scenarios12 | Cross-functional human teams & automated test suites10 | Shared understanding and behavioral alignment11 | Can leave technical constraints and architecture open-ended11 |
| **Spec-Driven Development (SDD)** | Executable, Versioned Specifications5 | Humans and AI coding agents12 | Contractual constraints that eliminate non-deterministic drift11 | High upfront cognitive overhead and review fatigue10 |

Without structured guidance, ad-hoc interactions with AI coding models—frequently termed "vibe coding"—rely on loose natural-language prompts6. This approach introduces extreme non-determinism, as models are forced to guess critical implementation details, including data schemas, security boundaries, validation rules, and error-handling behaviors6. The resulting outputs often contain subtle architectural violations, redundant implementations, and security vulnerabilities14.  
Spec-Driven Development (SDD) emerges as the disciplined counterweight to this systemic unpredictability4. By establishing a structured, machine-readable specification as the primary source of truth, SDD ensures that both human supervisors and AI agents operate under a unified, executable contract4. Under this framework, code is no longer treated as the definitive state of the system; instead, it is treated as a secondary, compiled, and continuously regenerable asset derived from upstream intent5.

## **Economic and Theoretical Foundations of SDD**

While SDD has gained rapid traction as a practical countermeasure to AI non-determinism, its underlying principles are deeply rooted in established software engineering and economic theories9.

### **Contractual Governance and Transaction Cost Economics**

The emergence of SDD can be formally theorized using Oliver Williamson’s framework of Transaction Cost Economics (TCE)19. In traditional software engineering, custom source code represents an asset of high specificity, while the execution of non-deterministic LLM generators introduces high behavioral uncertainty20. In an unstructured "vibe coding" environment, the transaction costs of using AI assistants—manifested as prompt churn, regression debugging, and code-review overhead—rapidly exceed the savings of accelerated code generation1.  
![][image1]  
SDD operates as a formal contractual governance mechanism20. By forcing the creation of machine-readable specifications prior to generation, SDD establishes a deterministic, legalistic framework that curtails behavioral uncertainty14. The specification serves as a binding contract, shifting the transaction from an unstructured search space to a constrained transformation, thereby rendering the use of autonomous agents economically rational for complex enterprises8.

### **The Academic Lineage of Executable Contracts**

The paradigm of treating specifications as executable assets builds directly on the Design by Contract (DbC) principles pioneered by Bertrand Meyer9. In DbC, software components govern their interactions through explicit preconditions, postconditions, and invariants13. In 2004, Ostroff, Makalsky, and Paige integrated these concepts with agile development, framing tests and contracts as complementary specifications that must run in unison to verify system safety9.  
SDD generalizes this research by scaling the contractual layer upstream3. In the agentic era, tests are no longer authored as independent artifacts; instead, they are generated directly as executable outputs of the specification itself9. By writing precise, EARS-compliant behavioral requirements, human designers establish the semantic assertions that both guide AI implementation and populate the automated test suites used by CI/CD pipelines to verify output compliance3.

## **The Maturity Spectrum of Spec-Driven Development**

Adopting Spec-Driven Development is not a binary choice; rather, it exists along a spectrum of operational rigor and automation2. Organizations calibrate their commitment based on codebase maturity, safety requirements, and the sophistication of their underlying toolchain2.

### **Level 1: Spec-First Development**

The entry point to SDD focuses primarily on establishing upfront clarity2. Before a developer prompts an AI assistant to write code, they construct a concise document outlining goals, constraints, and success criteria, typically in the form of a Markdown PRD2. While this significantly improves the first-pass success rate of the generator by providing vital context, the lack of ongoing synchronization means the spec is allowed to drift as the codebase evolves2. This approach carries a lower maintenance burden, making it highly practical for greenfield prototyping, experimental spikes, and throwaway applications where long-term architectural integrity is not a priority24.

### **Level 2: Spec-Anchored Development**

Regarded as the optimal operational model for most enterprise production systems, the spec-anchored approach treats the specification as a permanent, version-controlled asset living directly alongside the code in the repository5. Alignment is enforced through automated contract testing (utilizing tools like Pact or Specmatic) and Behavior-Driven Development suites13. If an engineer or an agent attempts to modify the implementation in a manner that violates the living spec, the automated checks in the CI/CD pipeline fail, immediately flagging the divergence13. This model ensures that the system's documentation and implementation evolve together as equal partners13.

### **Level 3: Spec-as-Source Development**

This represents the most radical interpretation of the paradigm14. Human developers author and refine specifications using highly structured, declarative markdown formats or specialized domain-specific languages5. Coding agents translate these specifications into working implementations, and manual editing of the generated source code is strictly prohibited8. Code files generated under this model typically contain strict headers warning that manual changes will be overwritten during the next synchronization pass14. Although it eliminates architectural drift by design, this model demands absolute trust in the consistency of the underlying code-generation pipeline, which remains challenging due to the non-deterministic nature of modern LLMs2.

## **Spec Persistence and Lifecycle Models in Repository Gardening**

To maintain specifications over time, organizations using tools like GitHub Spec Kit must adopt structured persistence models27. The choice of model determines how requirements change, how conflicts are resolved, and how historical context is preserved as the software evolves28.

| Persistence Model | Core Mutation Rule | Developer Workflow | Primary Strength | Structural Risk |
| :---- | :---- | :---- | :---- | :---- |
| **Flow-Back Spec** | Edit any artifact (spec, plan, tasks, or code), then reconcile manually17. | Bidirectional modification; developers edit files freely and run reconciliation scripts to resolve drift17. | High developer flexibility and rapid iteration17. | High risk of silent drift and conflicting parallel changes17. |
| **Flow-Forward Spec** | Create a new, isolated feature directory for every change request17. | Completed spec directories are treated as immutable historical records; new requirements spawn new directories7. | Impeccable audit trails, clear provenance, and zero risk of overwriting working features17. | Severe context fragmentation; duplication of schemas across historical directories17. |
| **Living Spec** | Edit the main specification file first, then regenerate downstream plans and tasks5. | Programmatic derivation; plans and task lists are treated as disposable compilations of the living spec4. | Maintains a single, enduring source of truth in the repository4. | High computational/token cost; demands mature tooling capable of incremental generation2. |

Choosing an appropriate persistence model requires engineering teams to balance the need for speed with the requirements of auditability17. In unregulated, fast-moving SaaS startups, the Flow-Back model is often selected to allow rapid human intervention during implementation, with periodic manual reconciliation to keep documents aligned17. Conversely, in highly regulated industries such as aerospace, medical device software, or fintech, the Flow-Forward model provides the immutable lineage required to satisfy strict compliance audits, linking every production binary back to a specific, unmutated requirement directory17.

## **The Canonical SDD Workflow: A Phased Gated Model**

To execute Spec-Driven Development predictably, mature workflows reject single-shot prompts in favor of a phased, highly structured lifecycle5. Every phase produces distinct, version-controlled markdown artifacts, which are subjected to human inspection before triggering downstream execution22. This gated approach prevents minor misunderstandings in the specification phase from compounding into catastrophic architectural errors during code generation4.  
\+------------------+ \+------------------+ \+------------------+  
| Constitution | \--\> | Specify | \--\> | Clarify |  
| (Invariants) | | (What & Why) | | (Ambiguities) |  
\+------------------+ \+------------------+ \+------------------+  
|  
\+------------------+ \+------------------+ v  
| Implement | \<-- | Tasks | \<-- | Plan |  
| (Task-by-Task) | | (Decomposition) | | (Architecture) |  
\+------------------+ \+------------------+ \+------------------+  
|  
v  
\+------------------+  
| Validate/Analyze |  
| (CI/CD Gate) |  
\+------------------+

### **Phase 0: The Constitution**

Before defining feature-specific requirements, the engineering team establishes a project "Constitution"4. This file (often documented as constitution.md or AGENTS.md) outlines the immutable boundaries, style guides, testing requirements, security policies, and architectural conventions that must govern all subsequent automated operations4.  
For example, the constitution might mandate strict adherence to TypeScript's strict mode, restrict external dependencies to a predefined list, or enforce clean architecture folder structures7. Spec Kit's memory bank serves as a repository for these high-level, immutable principles15. The coding agent ingests the constitution at the start of every session, ensuring it remains structurally aligned with organizational standards4.

### **Phase 1: Specify**

In the specification phase, the developer or product manager prioritizes articulating the functional behavior, user scenarios, and scope boundaries of the intended feature4. Crucially, this step focuses purely on the "what" and "why" of the capability, remaining completely technology-agnostic24. By decoupling business intent from implementation details, the team creates a highly modular representation of requirements that can be seamlessly reviewed by product owners, QA specialists, and system designers alike4.

### **Phase 2: Clarify**

Once the initial specification is captured, specialized evaluation tools or AI agents audit the document for logical inconsistencies, undefined edge cases, and linguistic ambiguity8. The agent enters an interactive interview mode, prompting the human developer to resolve marked uncertainties8. For instance, if a photo organizing application spec states that "albums are grouped by date," the clarification phase will force a decision on whether this refers to the photo upload date, the original file creation date, or a custom user metadata field31.

### **Phase 3: Plan**

With a concrete, unambiguous specification established, the workflow transitions to technical planning4. Here, the technical "how" is defined6. The developer and the planning agent collaborate to document the technology stack, data schemas, database migration strategies, state transitions, integration contracts (such as OpenAPI or AsyncAPI specifications), and non-functional targets like latency budgets6. This phase maps the functional requirements directly onto the architectural guardrails defined in the project constitution4.

### **Phase 4: Tasks**

To prevent context window saturation and instruction fatigue, the technical plan is decomposed into a series of atomic, independent, and sequential implementation tasks6. Each task is formatted with specific inputs, expected file modifications, and deterministic validation tests3. Rather than issuing a vague directive to "implement user authentication," the task list is broken down into precise, reviewable increments, such as "create a password hashing utility using bcrypt with a cost factor of 12"27.

### **Phase 5: Implement**

During the implementation phase, the coding agent acts as an execution engine, checking out the generated task list and tackling each item sequentially14. The agent is confined strictly to the files and boundaries allocated to the current task9. Human developers observe the execution in real-time, reviewing precise diffs and verifying code changes incrementally rather than coping with massive, opaque code dumps at the end of the development cycle22.

### **Phase 6: Validate and Analyze**

The finalized implementation is subjected to a rigorous validation loop7. The system runs compiled test suites, verifies that the generated code strictly honors the designated API contracts, and executes static analysis checks14. To resolve the non-deterministic nature of LLM outputs, advanced implementations employ Property-Based Testing (PBT) to verify that defined specification invariants hold true across a wide spectrum of randomized inputs6.

## **Standardizing Precision: The EARS Syntax in Spec Writing**

The effectiveness of any Spec-Driven Development workflow is directly constrained by the linguistic precision of its input specifications24. Natural language is inherently ambiguous, filled with qualitative terms that LLMs interpret inconsistently16. To bridge this gap, SDD has adopted the **Easy Approach to Requirements Syntax (EARS)** as its de facto formatting standard4. Developed originally in systems engineering for safety-critical domains, EARS uses a highly structured, formulaic grammar that turns fuzzy requirements into testable, machine-parseable statements5.

| Pattern Name | Grammatical Template | Practical Application | Concrete System Example |
| :---- | :---- | :---- | :---- |
| **Ubiquitous** | The \[system\] **shall** \[response\]7. | For universal invariants and persistent system behaviors that operate without external triggers34. | The system **shall** hash passwords using bcrypt with a cost factor of 1230. |
| **Event-Driven** | **WHEN** \[trigger\], **THE system SHALL** \[response\]12. | For reactive behaviors initiated by user inputs, API requests, or external state changes30. | **WHEN** a payment webhook is received, **THE system SHALL** verify the HMAC signature30. |
| **State-Driven** | **WHILE** \[state\], **THE system SHALL** \[response\]12. | For continuous or periodic actions that must execute exclusively during a specific operating mode30. | **WHILE** the system is in maintenance mode, **THE system SHALL** return HTTP 50330. |
| **Unwanted Behavior** | **IF** \[unwanted condition\], **THEN** \[response\]12. | For handling system errors, validation failures, edge cases, and security boundary violations30. | **IF** validation fails 3×, **THEN** lock the account for 15 minutes12. |
| **Optional** | **WHERE** \[feature active\], **THE system SHALL** \[response\]12. | For executing conditional logic tied to specific modules, permissions levels, or localized configurations30. | **WHERE** the enterprise SSO module is enabled, **THE system SHALL** validate tokens against SAML IdP30. |

By adhering to EARS, teams enforce strict grammar rules that dramatically improve model comprehension34:

* The modal verb **SHALL** is used exclusively to denote mandatory system responses; ambiguous alternatives such as "should," "will," or "must" are strictly prohibited30.  
* Keywords such as **WHEN**, **WHILE**, **WHERE**, and **THE SYSTEM SHALL** must be fully capitalized to act as explicit syntactic markers for the parsing engine30.  
* Qualitative, non-verifiable terms—including "timely," "efficient," "user-friendly," "properly," "appropriate," and "various"—are banned from the vocabulary30.

By transforming natural language requirements into deterministic grammatical logic, EARS allows specifications to map almost 1:1 onto executable test cases12. This enables static validation tools to automatically scan requirements for logical conflicts, circular dependencies, and missing exception handlers before code generation begins30.

## **The Productivity-Reliability Paradox (PRP)**

The rapid integration of AI assistants into software development has revealed a striking empirical contradiction known as the **Productivity-Reliability Paradox (PRP)**19.

### **The Empirical Contradiction**

Controlled individual-level studies and laboratory experiments consistently report localized developer productivity gains ranging from **20% to 56%** when implementing well-scoped, low-abstraction tasks20. Conversely, the most rigorous randomized controlled trials (RCTs) examining experienced open-source developers operating in naturalistic, complex environments document an average **19% slowdown** when utilizing AI assistance20.  
La asimetría entre la generación y la revisión de código crea cuellos de botella severos, donde el tiempo ahorrado en escribir sintaxis se pierde depurando inconsistencias arquitectónicas21:  
Traditional Code Review Bottleneck (Unstructured AI Generation):  
\[Fast Code Generation (AI)\] \===\> \[Massive Unverified PR Output\] \===\> \[Review & Debug Bottleneck (Human)\] \===\> \[Overall Slowdown\]  
SDD Contract-Driven Flow:  
\[Upfront Spec & Planning (Human/AI)\] \===\> \[Constrained Execution (AI)\] \===\> \[Automated Integration Verification\] \===\> \[Fast Path to Production\]  
To model this tension, let ![][image2] represent net engineering throughput, ![][image3] represent the time spent generating code, and ![][image4] represent the time required to review, test, and debug implementation outputs:  
![][image5]  
In unstructured "vibe coding" workflows, ![][image3] approaches zero as models synthesize thousands of lines of code in seconds29. However, because the generated code is unconstrained by a formal contract, ![][image4] escalates non-linearly22. The human developer is forced to spend hours hunting for hidden regressions, logical contradictions, and subtle architectural violations16. This code review bottleneck entirely consumes the upstream speed gains, creating a productivity-reliability bottleneck22.

### **Strategic Moderating Variables**

The resolution of the paradox is governed by three primary moderating variables20:

1. **Task Abstraction Level (![][image6]):** AI generators excel at low-abstraction syntactic operations (e.g., writing boilerplate, generating regular expressions) but struggle with high-abstraction architectural decision-making, where requirements are complex and highly interdependent20.  
2. **Codebase Maturity (![][image7]):** Greenfield projects exhibit massive acceleration under raw generation workflows because they lack existing structural constraints19. Mature "brownfield" environments possess years of undocumented decisions and implicit context, which act as a severe friction point for context-blind models19.  
3. **Developer Experience (![][image8]):** Novice programmers leverage AI for rapid learning and syntax synthesis, whereas highly experienced engineers encounter significant cognitive friction when forced to review and debug complex, hallucinated code structures they did not write19.

### **Cognitive Biases and Skills Decay**

At the cognitive level, the PRP is exacerbated by well-documented human biases in automation interaction41:

* **Automation Bias:** The tendency of human supervisors to accept AI-generated outputs as correct without performing rigorous, manual verification, often driven by a false perception of the model's fluency41.  
* **Automation-Induced Complacency:** A significant reduction in developer vigilance during code monitoring, leading to a failure to detect critical system defects and structural drift43.  
* **Cognitive Skills Decay:** The gradual erosion of a developer's deep system visualization and manual debugging capabilities due to continuous disuse, reducing their capacity to intervene effectively when AI generation fails43.

Spec-Driven Development acts as a formal governance framework to resolve the PRP20. By forcing intent clarification upfront, SDD shifts the engineering focus from reactive, high-overhead code reviews to proactive, low-overhead contract design4. The specification functions as a deterministic constraint that narrows the model's search space, dramatically reducing the probability of architectural deviations5. This significantly lowers ![][image4] and stabilizes net throughput across complex, brownfield applications19.

## **The Collaborative Shift: Managing Role Blur and the "Bitter Lesson"**

As Spec-Driven Development establishes specifications as the primary engineering artifacts, it fundamentally restructures the collaborative dynamics between product, architecture, engineering, and quality assurance stakeholders4.

### **The Blurring Boundaries of Product and Engineering**

In traditional software environments, product managers own the "what" and "why" of requirements, while engineers own the "how" of implementation37. SDD accelerates a profound role blur44. Because the specification directly drives code generation, the acts of requirements definition and software programming begin to merge8.  
Product managers increasingly author highly structured, EARS-compliant specifications directly within repository-linked environments, expanding their operational reach into territories historically guarded by developers7. Conversely, software engineers spend less time writing functional logic and more time acting as high-level systems architects, refining specifications, and establishing strict technical guardrails to constrain autonomous code-generation agents7.  
Traditional Pipeline:  
\[Product Manager: Loose Requirements\] \=== (Translation Loss) \===\> \[Developer: Manual Syntax Code\]  
SDD Agentic Pipeline:  
\[PM & Architect: Structured Spec & Constitution\] \<== (Shared Ownership) \==\> \[Executable Code Generation & Verification Agents\]

### **The QA-Left Movement: Continuous Verification Planning**

Under SDD, quality assurance shifts to the absolute beginning of the development lifecycle15. Since EARS-compliant specifications map 1:1 onto testable outcomes, test cases and validation strategies are generated concurrently with the requirements3.  
QA specialists collaborate with product owners to define the boundary conditions, edge cases, and compliance constraints directly inside the specification files4. Consequently, when the AI agent receives the implementation mandate, it is simultaneously bound by a suite of deterministic behavioral tests4. Verification is no longer a downstream gate; it is an integrated, continuous constraint that shapes the code as it is generated8.

### **Confronting the "Bitter Lesson" of AI Governance**

In November 2025, Thoughtworks placed Spec-Driven Development in its "Assess" ring, issuing a measured warning against over-engineering25. Engineering teams must navigate what the AI community calls the "bitter lesson": the empirical reality that handcrafting increasingly detailed, human-engineered rules and templates for AI eventually fails to scale when compared to leveraging raw, general-purpose computation and improved model reasoning capabilities25.  
If an organization spends weeks debating JSON schema keys or establishing massive, multi-file markdown frameworks for simple feature sets, the ceremonial overhead of SDD can quickly neutralize the productivity advantages of AI-assisted engineering2. The optimal path forward requires lean, highly flexible specifications that prioritize capturing core architectural boundaries and logical invariants over scripting every pixel or line of business logic2.

## **Comprehensive Tooling Architecture: Spec Kit Commands and Extensions**

To establish a uniform SDD process, tools like GitHub Spec Kit utilize standardized CLI command hierarchies and extensible plugin architectures27. Operating Spec Kit requires engineers to leverage the specify CLI tool—installed using fast package managers like uv—to orchestrate agent workflows directly within the repository27.

### **Core Spec Kit Command Scaffolding**

Every step of the Spec Kit workflow produces specific file-system modifications, creating a traceable audit trail of architectural planning and execution27.

| Command Name | Workflow Phase | File-System Output | Operational Purpose and Agent Prompts |
| :---- | :---- | :---- | :---- |
| **/speckit.constitution** | Core Governance27 | .specify/memory/constitution.md \[cite: 30, 36\] | Sets the immutable system invariants, architectural boundaries, coding standards, and testing policies15. |
| **/speckit.specify** | Functional Specification23 | .specify/features/NNN-name/spec.md \[cite: 12, 17\] | Ingests vague natural language goals to generate structured user stories and EARS-compliant criteria4. |
| **/speckit.clarify** | Ambiguity Resolution23 | Updates spec.md with resolved criteria27 | Prompts the human developer to resolve marked uncertainties, undefined edge cases, and logical conflicts7. |
| **/speckit.plan** | Technical Architecture23 | .specify/features/NNN-name/plan.md \[cite: 12, 17\] | Formulates the technology stack, database schemas, API contracts, state diagrams, and infrastructural limits7. |
| **/speckit.tasks** | Task Decomposition23 | .specify/features/NNN-name/tasks.md \[cite: 12, 17\] | Breaks the plan into atomic, sequenced, and independently verifiable implementation directives6. |
| **/speckit.taskstoissues** | Tracker Integration23 | Programmatically updates GitHub Issues27 | Translates local markdown task lists into enterprise backlog tracking tickets, maintaining bidirectional sync23. |
| **/speckit.implement** | Automated Coding23 | Updates target application source code6 | Instructs the implementation agent to execute the task list sequentially, writing strict spec-compliant code27. |
| **/speckit.converge** | Execution Alignment31 | Verifies and commits codebase edits34 | Executes automated validation passes, ensuring implementation artifacts fully align with target expectations34. |

### **Extensibility through Spec Kit Plugins**

Spec Kit features an extensible integration model, enabling teams to attach domain-specific validators and third-party platform orchestrators through structured hooks23.

* **spec-kit-github-issues:** Programmatically parses the generated tasks.md file, imports requirements, and establishes bidirectional traceability between local repository specs and the team's enterprise issue tracker46.  
* **spec-kit-improve:** Conducts automated architectural audits of brownfield systems, acting as a virtual senior advisor to construct prioritized, self-contained spec templates for subsequent execution cycles45.  
* **spec-kit-preview:** Evaluates plan and task markdown files to generate interactive, self-contained HTML wireframes and functional frontend prototypes, giving designers early visibility45.  
* **spec-kit-orchestrator:** Enables cross-catalog agent discovery, routing complex implementation steps to specialized sub-agents based on the architectural constraints in the specification45.  
* **spec-kit-iterate:** Implements a strict "define-and-apply" loop, allowing developers to safely refine specifications mid-implementation and propagate changes downstream45.

## **Detailed Comparative Case Studies**

The performance gains and structural trade-offs of Spec-Driven Development are illustrated through two detailed enterprise case studies3.

### **Case Study 1: Microsoft Global Platform Modernization (Brownfield Architecture)**

A major greenfield-turned-brownfield initiative within Microsoft focused on constructing a globally distributed operations platform with thousands of active integrations spanning scheduling, physical security, vendor logistics, compliance, and attendee access15.

* **The Challenge:** Multiple cross-functional teams were experiencing extreme execution churn15. Standard ad-hoc prompting workflows with AI assistants repeatedly violated strict service boundaries, invented non-existent component patterns, and introduced incompatible API payloads14.  
* **The SDD Intervention:** The engineering group initialized a shared repository constitution and adopted GitHub Spec Kit15. High-level domain analysis was integrated with Domain-Driven Design (DDD) to construct modular, bounded contexts20. All integration payloads were restricted to strict OpenAPI and AsyncAPI schemas before writing backend logic14.  
* **The Empirical Results:** The unified vocabulary and automated contract validation reduced developer onboarding times from **three weeks to a few days**15. By shifting the development team's cognitive focus to upstream contract design, the organization eliminated integration failures in production6. The structural changes drastically cut execution churn, enabling multiple teams to scale and implement code in parallel with confidence6.

### **Case Study 2: Multi-Agent Parallel Front-End Development (Figma Integration)**

An enterprise software team initiated a project to deliver a complex, responsive web-portal frontend within a tight, multi-week deadline11.

* **The Core Pattern:** The project employed a high-leverage multi-agent pattern consisting of a **Coordinator**, multiple parallel **Implementors**, and an independent **Verifier**14.

\+-------------------+  
| FIGMA DESIGN SYS |  
\+-------------------+  
|  
v  
\+-------------------+ \+-------------------+ \+-------------------+  
| IMPLEMENTOR A | \<-- | COORDINATOR | \--\> | IMPLEMENTOR B |  
| (Page A Sub-Spec) | | (Specification) | | (Page B Sub-Spec) |  
\+-------------------+ \+-------------------+ \+-------------------+  
\\ | /  
\\ v /  
\------------\> \+-------------------+ \<----------/  
| VERIFIER |  
| (Opposition Target)|  
\+-------------------+

* **The Mechanics:**  
  1. **Figma MCP Context Pull:** The Coordinator agent used the Model Context Protocol (MCP) to read the project’s Figma design system directly14. It ingested exact layout parameters, design tokens, responsive grid breakpoints, component variants, and brand spacing values, writing these directly into the specification14.  
  2. **Decomposition:** The Coordinator decomposed the high-level specification by page, producing self-contained sub-specs for parallel execution14. Crucially, the coordinator assigned shared components (navigation headers, footers) to an isolated, early implementation task, establishing a stable, common library before page-level development commenced14.  
  3. **Parallel Implementation:** Multiple parallel Implementor agents were initialized, each receiving a precise page sub-spec with clear boundary constraints, preventing them from overwriting shared files or inventing custom component spacing14.  
  4. **Adversarial Verification:** An independent Verifier agent—operating with goals directly opposed to those of the Implementors—was assigned to test each compiled component against the design specifications, blocking the task if layout drift, accessibility violations, or unapproved styling patterns were detected14.  
* **The Operational Impact:** By pulling the design system directly into the specification before generating code, the team eliminated visual and structural drift across parallel development streams14. Component spacing remained perfectly consistent across pages, and the adversarial verification loop ensured that the generated frontend was production-ready without requiring manual UI alignment passes14.

## **Technical Appendix: Multi-Agent Specification and Prompt Engineering**

The implementation of Spec-Driven Development can be fully automated using multi-agent orchestrations, where specialized LLM agents execute the structured SDD phases under adversarial verification11. Below is a complete, production-ready specification framework demonstrating how to orchestrate a **Coordinator**, **Implementor**, and **Verifier** team to deliver a contract-compliant billing calculation engine11.

### **1\. The Project Constitution: Global Architectural Guardrails**

This file represents the immutable project DNA. It is placed at the root of the workspace to constrain all downstream generation15.

# **AGENTS.md \- Billing Service Constitution**

## **Article I: Architectural Mandates**

* All calculations must follow the immutable mathematical domain pattern.  
* Data persistence must utilize PostgreSQL via strict raw SQL migrations; ORM abstraction layers are prohibited.  
* The API layer must strictly conform to the schemas defined in .specify/contracts/billing-api.yaml.

## **Article II: Testing and Quality Gates**

* Unit test coverage must maintain a 100% threshold on all computational paths.  
* Property-based testing (via fast-check or equivalent) must validate all pricing boundaries.  
* Silent failures are prohibited; any runtime validation error must raise an explicit DomainException.

## **Article III: Security and Compliance**

* Financial values must utilize the absolute integer-based cents representation to prevent IEEE 754 float precision issues.  
* Direct manipulation of database transaction states inside business service handlers is prohibited.

### **2\. The OpenAPI Contract: Deterministic Interface Schema**

The interface contract is designed and validated before writing server-side logic, eliminating communication drift5.

YAML  
\# .specify/contracts/billing-api.yaml  
openapi: 3.0.3  
info:  
  title: Enterprise Billing Calculation API  
  version: 1.0.0  
paths:  
  /calculate-tier:  
    post:  
      summary: Computes tier-based pricing for active platform tenants  
      operationId: calculateTierPricing  
      requestBody:  
        required: true  
        content:  
          application/json:  
            schema:  
              type: object  
              required:  
                \- tenantId  
                \- activeUsers  
                \- usageUnits  
              properties:  
                tenantId:  
                  type: string  
                  format: uuid  
                activeUsers:  
                  type: integer  
                  minimum: 1  
                usageUnits:  
                  type: integer  
                  minimum: 0  
      responses:  
        '200':  
          description: Computational output of tier pricing in cents  
          content:  
            application/json:  
              schema:  
                type: object  
                required:  
                  \- tenantId  
                  \- baseCostCents  
                  \- variableCostCents  
                  \- totalCostCents  
                properties:  
                  tenantId:  
                    type: string  
                    format: uuid  
                  baseCostCents:  
                    type: integer  
                  variableCostCents:  
                    type: integer  
                  totalCostCents:  
                    type: integer  
        '400':  
          description: Invalid input parameters or schema violation

### **3\. The Functional Specification: EARS Notation Requirements**

The feature spec captures functional behavior using strict EARS patterns, removing qualitative ambiguity4. We can represent this file as follows to map raw operational metrics into deterministic financial metrics33:

### **.specify/features/001-tier-calculation/spec.md**

## **Context and System Goals**

This feature computes the dynamic pricing matrix for platform customers. It maps raw operational metrics into deterministic financial metrics.

## **Functional Requirements in EARS Format**

* **Ubiquitous:** The billing engine shall execute computations utilizing strict integer cents to prevent rounding drift.  
* **Event-Driven:** WHEN a billing computation request is submitted, THE system SHALL validate the payload against the OpenAPI 3.0.3 contract.  
* **State-Driven:** WHILE the tenant is configured on standard tier subscription, THE system SHALL apply a base fee of 15000 cents and a usage rate of 5 cents per unit.  
* **State-Driven:** WHILE the tenant is configured on enterprise tier subscription, THE system SHALL apply a base fee of 50000 cents and a usage rate of 3 cents per unit.  
* **Unwanted Behavior:** IF the validation of activeUsers or usageUnits fails, THEN the system SHALL return HTTP 400 Bad Request and abort execution.  
* **Optional:** WHERE custom volume discounting is active, THE system SHALL reduce tier rate by 15% for usage volume exceeding 10000 units.

### **4\. Agent Prompting: The Implementor vs. Verifier Instruction Set**

To scale work parallelization, the Coordinator initializes specialized agents with opposing mandates, driving code quality14. Below are the precise instruction files for both the Implementor and Verifier agents, designed to prevent any ambiguity:

# **Implementor Instruction Set**

Persona: Elite Computational Implementor Agent  
Objective: Generate functional TypeScript code that realizes the specification contract.  
Execution Directives:

1. Ingest .specify/contracts/billing-api.yaml and .specify/features/001-tier-calculation/spec.md.  
2. Respect the invariants defined in AGENTS.md (specifically raw SQL migrations, integer-cents calculations, and unit coverage).  
3. Generate the core tier pricing calculations. Ensure all errors are explicit.  
4. Output cleanly separated module logic. Do not write premature optimizations or speculative features.

# **Verifier Instruction Set**

Persona: Adversarial Contract Verification Agent  
Objective: Expose defects, contract violations, and regression failures in the Implementor's outputs.  
Verification Directives:

1. Audit the generated source code against AGENTS.md and .specify/contracts/billing-api.yaml.  
2. Identify code anomalies, specifically:  
   * Any usage of floating-point arithmetic for monetary values.  
   * Silent error suppression or try-catch blocks lacking clear domain exception escalation.  
   * Direct transaction handling inside standard service handlers.  
3. Generate property-based test assertions simulating extreme values (e.g., millions of activeUsers, boundary pricing values) to force integer overflow or calculation drift.  
4. If a single violation is discovered, reject the PR and output a structured markdown error report referencing the constitutional infraction.

## **Strategic Recommendations for Enterprise Adoption**

Transitioning from unstructured coding workflows to Spec-Driven Development requires systematic changes in organizational habits7. Rather than imposing a heavy, monolithic process overnight, engineering leaders should deploy the following calibrated adoption framework5.

### **Target Spec-Anchored as the Enterprise Balance Point**

Except in highly localized, extremely simple API domains where standard code generators already execute perfectly, organizations should avoid jumping directly to the radical "Spec-as-Source" model7.  
Instead, engineering teams should establish **Spec-Anchored development** as their standard7. By storing living specifications and plans alongside the code in Git, and verifying synchronization through automated test suites in the CI/CD pipeline, organizations achieve the ideal balance of speed, human control, and architectural protection2.

### **Calibrate Workflow Ceremony to Task Complexity**

Applying the full Spec Kit command hierarchy to a simple, localized bug fix adds excessive friction, creating "work about work" that frustrates senior developers15. Teams should calibrate operational gates to task scope21:

* **Sub-Feature Changes (Local, Low-Risk):** Allow developers to operate with lightweight, informal AI assistance15. The primary focus is code execution without extensive planning gates48.  
* **System-Level Changes (High-Risk, High-Complexity):** Mandate the full, gated SDD workflow (Specify ![][image9] Clarify ![][image9] Plan ![][image9] Tasks ![][image9] Implement ![][image9] Validate)7. Any schema alteration, core business logic modification, or boundary contract change requires an approved spec and design file prior to generation20.

### **Implement Proactive Spec Drift Guardrails**

To protect the integrity of the repository, teams must treat the specification as an active compilation constraint1. The CI/CD validation pipeline must include automated pre-merge gates that check the alignment between code behavior and specification documents1.  
If an engineer or an agent updates an application endpoint without updating the corresponding OpenAPI YAML contract, the build must fail5. Treating specification alignment as a non-negotiable definition of done prevents the silent accumulation of "spec debt," keeping documentation accurate over time10.

#### **Obras citadas**

1. Spec-Driven Development: Designing Before You Code (Again) | by Dave Patten | Medium, [https://medium.com/@dave-patten/spec-driven-development-designing-before-you-code-again-21023ac91180](https://medium.com/@dave-patten/spec-driven-development-designing-before-you-code-again-21023ac91180)  
2. What is Spec-Driven Development? \- IBM, [https://www.ibm.com/think/topics/spec-driven-development](https://www.ibm.com/think/topics/spec-driven-development)  
3. One Developer Is All You Need: A Case Study of an AI-Augmented One-Person Squad in a Brownfield Enterprise \- arXiv, [https://arxiv.org/html/2605.18461v1](https://arxiv.org/html/2605.18461v1)  
4. Spec-Driven Development: A Spec-First Approach to AI-Native Engineering, [https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering](https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering)  
5. Spec-Driven Development (SDD): The Definitive 2026 Guide, [https://thebcms.com/blog/spec-driven-development](https://thebcms.com/blog/spec-driven-development)  
6. Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants \- arXiv, [https://arxiv.org/html/2602.00180v1](https://arxiv.org/html/2602.00180v1)  
7. Spec-Driven Development in 2026: What It Is, the Tooling, and How Teams Actually Use It, [https://dev.to/krlz/spec-driven-development-in-2026-what-it-is-the-tooling-and-how-teams-actually-use-it-2fk2](https://dev.to/krlz/spec-driven-development-in-2026-what-it-is-the-tooling-and-how-teams-actually-use-it-2fk2)  
8. spec-kit/spec-driven.md at main \- GitHub, [https://github.com/github/spec-kit/blob/main/spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md)  
9. Specification-driven development \- Wikipedia, [https://en.wikipedia.org/wiki/Specification-driven\_development](https://en.wikipedia.org/wiki/Specification-driven_development)  
10. Spec Driven Development: The Future of Building with AI \- Beam AI, [https://beam.ai/agentic-insights/spec-driven-development-build-what-you-mean-not-what-you-guess](https://beam.ai/agentic-insights/spec-driven-development-build-what-you-mean-not-what-you-guess)  
11. What Is Spec-Driven Development? A Complete Guide \- Augment Code, [https://www.augmentcode.com/guides/what-is-spec-driven-development](https://www.augmentcode.com/guides/what-is-spec-driven-development)  
12. [https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering\#:\~:text=Spec%2DDriven%20Development%20(SDD)%20is%20a%20spec%2Dfirst,artifacts%20from%20that%20shared%20context.](https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering#:~:text=Spec%2DDriven%20Development%20\(SDD\)%20is%20a%20spec%2Dfirst,artifacts%20from%20that%20shared%20context.)  
13. Spec-Driven Development:From Code to Contract in the Age of AI Coding Assistants \- arXiv, [https://arxiv.org/pdf/2602.00180](https://arxiv.org/pdf/2602.00180)  
14. From Vibes to Specs: Examining the Shift to Spec-Driven Development \- Itential, [https://www.itential.com/resource/blog/vibes-to-specs-development/](https://www.itential.com/resource/blog/vibes-to-specs-development/)  
15. Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl \- Martin Fowler, [https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)  
16. From Vibe Coding to Spec-Driven Development \- Test Collab, [https://testcollab.com/blog/from-vibe-coding-to-spec-driven-development](https://testcollab.com/blog/from-vibe-coding-to-spec-driven-development)  
17. Spec-Driven Development (SDD) for AI-Powered Engineering \- Jama Software, [https://www.jamasoftware.com/blog/what-is-spec-driven-development-sdd-for-ai-powered-engineering/](https://www.jamasoftware.com/blog/what-is-spec-driven-development-sdd-for-ai-powered-engineering/)  
18. Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity, [https://www.semanticscholar.org/paper/Measuring-the-Impact-of-Early-2025-AI-on-Developer-Becker-Rush/9008680aac5a92b3a089aa1487eea76b8565f0d3](https://www.semanticscholar.org/paper/Measuring-the-Impact-of-Early-2025-AI-on-Developer-Becker-Rush/9008680aac5a92b3a089aa1487eea76b8565f0d3)  
19. The Productivity-Reliability Paradox: Specification-Driven Governance for AI-Augmented Software Development \- arXiv, [https://arxiv.org/html/2605.01160v1](https://arxiv.org/html/2605.01160v1)  
20. Spec-Driven Development for AI-Enabled Enterprise Systems \- Microsoft Community Hub, [https://techcommunity.microsoft.com/blog/educatordeveloperblog/spec-driven-development-for-ai-enabled-enterprise-systems/4520807](https://techcommunity.microsoft.com/blog/educatordeveloperblog/spec-driven-development-for-ai-enabled-enterprise-systems/4520807)  
21. Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains \- arXiv, [https://arxiv.org/html/2606.22484v1](https://arxiv.org/html/2606.22484v1)  
22. Spec-Driven Development: GitHub Spec Kit & OpenSpec in Real Projects, [https://wearecommunity.io/communities/datazencommunity/articles/8061](https://wearecommunity.io/communities/datazencommunity/articles/8061)  
23. Spec-Driven Development:From Code to Contract in the Age of AI Coding Assistants, [https://www.semanticscholar.org/paper/Spec-Driven-Development%3AFrom-Code-to-Contract-in-of-Piskala/f2d164abe42a4f626b6ddb860551f247c639b827](https://www.semanticscholar.org/paper/Spec-Driven-Development%3AFrom-Code-to-Contract-in-of-Piskala/f2d164abe42a4f626b6ddb860551f247c639b827)  
24. Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants \- arXiv, [https://arxiv.org/html/2602.00180](https://arxiv.org/html/2602.00180)  
25. What Is Spec-Driven Development? (And Why It Fixes Vibe Coding) \- VibeReady Blog, [https://vibeready.sh/blog/what-is-spec-driven-development/](https://vibeready.sh/blog/what-is-spec-driven-development/)  
26. Spec-Driven Development:From Code to Contract in the Age of AI Coding Assistants, [https://www.researchgate.net/publication/400370399\_Spec-Driven\_DevelopmentFrom\_Code\_to\_Contract\_in\_the\_Age\_of\_AI\_Coding\_Assistants](https://www.researchgate.net/publication/400370399_Spec-Driven_DevelopmentFrom_Code_to_Contract_in_the_Age_of_AI_Coding_Assistants)  
27. GitHub Spec Kit | Ry Walker Research, [https://rywalker.com/research/github-spec-kit](https://rywalker.com/research/github-spec-kit)  
28. spec-kit/docs/concepts/spec-persistence.md at main \- GitHub, [https://github.com/github/spec-kit/blob/main/docs/concepts/spec-persistence.md](https://github.com/github/spec-kit/blob/main/docs/concepts/spec-persistence.md)  
29. Por qué Spec-driven Development es el futuro de la ingeniería con IA. \- Raona, [https://raona.com/spec-driven-development-ingenieria-ia/](https://raona.com/spec-driven-development-ingenieria-ia/)  
30. GitHub Spec Kit \- Peter Miľovčík \- Obsidian Publish, [https://publish.obsidian.md/petermilovcik/1+Notes/GitHub+Spec+Kit](https://publish.obsidian.md/petermilovcik/1+Notes/GitHub+Spec+Kit)  
31. GitHub \- github/spec-kit: Toolkit to help you get started with Spec-Driven Development, [https://github.com/github/spec-kit](https://github.com/github/spec-kit)  
32. GitHub Spec-Kit: From Vibe Coding to Spec-Driven Development \- DEV Community, [https://dev.to/petersaktor/github-spec-kit-from-vibe-coding-to-spec-driven-development-1pgd](https://dev.to/petersaktor/github-spec-kit-from-vibe-coding-to-spec-driven-development-1pgd)  
33. The Benefits of Spec-Driven Development With Claude Code | Apex Fintech Solutions, [https://apexfintechsolutions.com/blog/the-benefits-of-spec-driven-development-with-claude-code/](https://apexfintechsolutions.com/blog/the-benefits-of-spec-driven-development-with-claude-code/)  
34. ears-spec-engine · Packages \- Pi Coding Agent, [https://pi.dev/packages/ears-spec-engine](https://pi.dev/packages/ears-spec-engine)  
35. Spec-Driven Development Tutorial using GitHub Spec Kit \- Scalable Path, [https://www.scalablepath.com/ai/spec-driven-development-workflow](https://www.scalablepath.com/ai/spec-driven-development-workflow)  
36. From PRD to Production: My spec-kit Workflow for Structured Development \- Stephan Eberle, [https://steviee.medium.com/from-prd-to-production-my-spec-kit-workflow-for-structured-development-d9bf6631d647](https://steviee.medium.com/from-prd-to-production-my-spec-kit-workflow-for-structured-development-d9bf6631d647)  
37. Spec-Driven Development \- Tom Ron, [https://tomron.net/2026/05/12/spec-driven-development/](https://tomron.net/2026/05/12/spec-driven-development/)  
38. Mastering the EARS Syntax: Write Better Requirements \- life michael, [https://lifemichael.com/corporate/mastering-the-ears-syntax-write-better-requirements/](https://lifemichael.com/corporate/mastering-the-ears-syntax-write-better-requirements/)  
39. Spec-Driven Development – Adoption at Enterprise Scale \- InfoQ, [https://www.infoq.com/articles/enterprise-spec-driven-development/](https://www.infoq.com/articles/enterprise-spec-driven-development/)  
40. \[2605.01160\] The Productivity-Reliability Paradox: Specification-Driven Governance for AI-Augmented Software Development \- arXiv, [https://arxiv.org/abs/2605.01160](https://arxiv.org/abs/2605.01160)  
41. Richard W Geven's research works | San Jose State University and other places, [https://www.researchgate.net/scientific-contributions/Richard-W-Geven-2019246609](https://www.researchgate.net/scientific-contributions/Richard-W-Geven-2019246609)  
42. Five Principles for AI-Assisted DDD — Keeping the Human at the Center \- codecentric AG, [https://www.codecentric.de/en/knowledge-hub/blog/five-principles-for-ai-assisted-ddd-keeping-the-human-at-the-center](https://www.codecentric.de/en/knowledge-hub/blog/five-principles-for-ai-assisted-ddd-keeping-the-human-at-the-center)  
43. Structured-Prompt-Driven Development (SPDD) \- Martin Fowler, [https://martinfowler.com/articles/structured-prompt-driven/](https://martinfowler.com/articles/structured-prompt-driven/)  
44. Quick Start Guide | Spec Kit Documentation \- GitHub Pages, [https://github.github.com/spec-kit/quickstart.html](https://github.github.com/spec-kit/quickstart.html)  
45. Spec-driven development | Technology Radar \- Thoughtworks, [https://www.thoughtworks.com/radar/techniques/spec-driven-development](https://www.thoughtworks.com/radar/techniques/spec-driven-development)  
46. Community Extensions | Spec Kit Documentation \- GitHub Pages, [https://github.github.com/spec-kit/community/extensions.html](https://github.github.com/spec-kit/community/extensions.html)  
47. Spec-Driven Development with AI: A Spec Kit \+ Claude Code Case Study \- OrangeLoops, [https://orangeloops.com/2026/05/spec-driven-development-with-ai-a-spec-kit-claude-code-case-study/](https://orangeloops.com/2026/05/spec-driven-development-with-ai-a-spec-kit-claude-code-case-study/)  
48. Spec-Driven Development vs Waterfall: Key Differences \- Augment Code, [https://www.augmentcode.com/guides/spec-driven-development-vs-waterfall](https://www.augmentcode.com/guides/spec-driven-development-vs-waterfall)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABBCAYAAABsOPjkAAAQKElEQVR4Xu2de6huR3XAV7EVpUarkfqokpv6QozVojX1UUhB20pTKUZ8lhIUqkKgPrDW/mGPioiIVXwkfUhTW2xRQ6NobFEhHyq0oNRWLBYfEMUHKlEUW0xbrfvH7NVvfXNnf9853nPOPffe3w+GfHtm9p6116xZs2Zm35MIEREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREZEhPzWlu/WZIiKHyF2ndLs+U0Skcq8p3aNc32FOFxIEZUvvfOOUruozC5f3GScE3ol+zUngp+e8swk6vlOfKSJxzZTe0WeKnHTuPqV/n9Inp/TnU7p+St+cE7/Jo4w61D0XYeL8iS7vOVP6vyld0eUfBQ+O1tZ1Je+ZU/rUnP9bJf/H5Wf6jBMKdvW6aO/99pJP//zBlC4ueT2/MaX/mdLj+oIjApl2BV13mdKHp3Sf+frOU7p2Sv85pUdkpSPkB9F0WUEWZEI2yj42/xeb38UV0Z7Z12XXsx9DZ8JTpvSSaHK9db4m/cWcd2Xsr71nRfNNL+0LDhECX2T6t77gkPm5aO/S92fyk9F09N4p/XBKL4/mW4D+YaHDvd+J1o/UP1sc1F7QMYs1dLzNB4xYWvztgnbwOQeRU+Sswo7PLbE2Wlbkqznl6pyyW6LVPRdh4ux3Go4rYHtktCDlaXG6Y2C36LACthr8nGR43ydHCwrqTtpDpvT1ct2D7t4S7f43dWVHBTazK+hipU4QWSHIO5sBG8ELOoZ/nq/PNGB7T5w+hs4U/MnI/n8nmgxP6PKX4P3Oh4ANsq+2QZ0l+2LX6Ch1sV8Oai9nErD19nMQvhtjPYqcSDBWBleFyb8PAKhzLhp2TvQHcR6HCc73a31mAcd7Jg4H7hin99dJ5Odjeaf2ltgeiD1pSjdH21kgHQfs6O2y+VWcHrABu1q77j0qsIXDbJsxtIrDH0NLARvfF5HPLuF+OOqA7TjZb8D2xRgvoOn7Xp/HzVHZywh83z/2mQcAn/PlPlPkpPL4Kb2tyxsFbH8d66ModhD4Vif/W8GJkPrdJMh74GdjfIxHPtv8bOefKvn5jRBp6ZgKB0HbdYXGLg6r9ZHzQMZ+Ox0ZkYFnjN4hZeZ5yLKNnHhu6gsKH49NB7utfa7RDeWnYn3Uy7Z+31/JA6Z0SbSjupGDP06wnxtifFSTO29L/F203Sz0Rd1eNwnHgbwzbdy/5C/ZFWAD6KbaCDr7bOwOfJALeU51+U+NTX3Tn7ST/btEjp8R2B5l/bjpr7GFXm7q9GMAWZbaq3UZQ6su7zBYCtiQnfzndfnY++j9a8CWY6dnP/5jG9wzWmgs6S/rj+4b+anksAM2xkm2k79HY2ebfqhPWyO7TZvYr70s2XCCruqckuNmSXZ83y59bQOfcyb3i5x1GPRLAcAvR3MWHLWwY4Kx40CeO//OIOYjU/r2/BseOqV/ndK/RDseBHYwmPCYRLnvM3M+/Eq03RjIb8CeGG3AvmxKL57LgG91aOtR0T72ZmVOEMrA//Up/Ve0yRtHkc6AZ/IO6dxwUtdFewbQDs4ggwic1Quj7QS9e85jdXfblB49X/fw7NTPLna1j24IWBJ0w/ugt9+NJlNOAtxL3arPd8WyHOgsvyHalXqHuR/S4SMjsvK7Tgr0PzY1moCSD0TTN7pG50/fLI7LYvNIlWO1m2O7XTGhpN0AdvnGaPJiL/8UzX6Qqw/sE+pii/RzJhYI6BRoI+33S3N9+MJcL+H96nhhFxFZIINH/sv7cO+LoslEv9YJp9czOuO+3g5pm+9TgXHF0dDDotWttoLdowN0gU64Zgwx4TKmee7z57r06fen9MdznV0gH/d/MJosJORi/FY7wz7YxSQQgMun9L5o7wbIeuuU/nC+xhYY2/gF2OY/6J/UzxvmcmRn5/vPpnT7aGOKa2w0+XRs7gDymzxAN9TlmfjIVaz1SR79B+m3fnG+BurV/hxBnaXx8vZY+zTsg8Uiz0M3vBe6oc3UTfoZEr+xK+pjZ/DfsbYT7uHzDj5f4Hu710Trr6uj3YNMS/YC7GahJ8bGqWh6yG8/0TG76PleyJ79wiItn4Hs9C1gb9g5dbiHxDuQj68m/4Hz9b2n9NFo478GktxDm9XeRM4pGPSkERj7KlqABq+Y0j1j/a1WDoYM4Co88y2xHhwMVgYtzoFVNU4xy8hLh5iOggkFcMB5tEZ9Jra9uQznznXKl88drfaqcyMwYpKsAzcn+3QqPAuHgdNLeEec3IiDBGy72ucdfr+UoZt02LTT9xfX/1GukXFJjqMO2CDtJvuwQhlOmR3JEfRp9mc+JwP9BB3Uo1LauTG22xU7ONUeaf/LU7o01u1w/y64//3RJjf6m0QAVm2OvLqDSEBJHhMa8BtZEvSBLAQlBCcZoPJMPjp/wnw9muCrXSfVDplw8z0BXX0s1vZEvWor6GAV4zHUy10DqV1kwJbBJQkdfX5Kz4j1JM27cuyVz6Xfb4v1QglZa/lFsQ5AYZv/SLCderS2is0d9C/OCWif+iw4E36Tlza5inW/PDaajwTkwDYS6hDIJKP+7KFvkWVXwAb5vKobApfUBbol6MoA7jen9L1ofY1tjvzd3vybdlKPBMG/Pecv2Qt9i62kjnjvHNeQwVN9L9qr/YLs9G2SPrYnfWfKnuOoB9l5h15WkXMGBn0fACTbJjIm/k9F29Fih60fSL0z6QcoA5p7SPxLpyvnfHhMtEnxG1P6UKzvywl5JA/sN2AjcOzlZSKuDnXkiOpE2MMqlPJ39AUFVq+s/He1j25qQIBuKIdRwIYD/odY12fX5G4bNY6Xx0XbJRntVCHrKsZ9BNdECzDYoSJ9K9o7VWePLl4855OY9H9pLhvZVdpe3d3J9PDYbucVgrx+N4kVPW3dUPK4rrafz8d2MnAZyZIT0mhyhtEE348zoE7a6bbxDQcJ2JiAs30CoRrk7CLfu5cVyCcoSz19Ik7XDeMGenm5p/cJj4mx/0j2orWJHWGPl5UyoD4JaLe/n0UVNvr4+XoVTYYefOTV0Xzk56K1Wfti1J896KsGpJW+7/vn9XbN76X2uJcA8/rY1PtL5vKR34Ft9sJOHmOT0xZS7bd+PoBqt7CKTb0uBWxAHxK0YZP4UPxIT+pjJKvIOcE2h94P+OSR0QY3OwdMWKOB1DuT0QDlfia6dNiAA+X62vm63nfQgK0OzCoPz+vlBfLeNv8eOaLeoVRw/pTjNJZgp4jAYj/tXxxNNwQs6IbtfaiOk+OYDIoIJF4d6z8fQtB2thjtuCbbnCYrY3Yk6OtMl0R71k2lXkI77KBR/tWS39sVTpwgeRQsQG/nBLv0Z897Ymx7BKerck27SwEbsvTlyUkL2DIlj46mT8boXsnfD7zT0nuTTyLAoT+Xxhj08iJf9Qnb/EdyWbTdJPqC3bK6ewvUJwHy9vfnMzOIXMU4YMNHkp+fBCBX7YtRf/bQ/pLPQ1eHFbC9KJbHJewnYKv2wsKJBVfdHa79NuqXarewiu0BW10Q0oeUsTvNDvKlpSy5KNqu3dI7ipx4tjn0fsAnDKJ0aHBNtMFCPSY16CeSOkCpR2DRl2V79T6cK2UPiBYocgRaj7aA1TSOug/Y6uCv8uQRVX0GA7weHR00YIOroh05cAzVg9OmXdjVPrqpDof3JxiD6jjznfjv3pwHyPi1cn3cMJHUo4weZON7nx7kJqjtuTU2HTXvnN+2QPb7kl0BE0g9SoN3R/umrbdzbHjk1Fcx/teMHI9Vu0BW2kuyv/NItD+SQyZkyaMcxlPlb6IF5P2EDNWuk2qn2GJ/1MX4yWPXfiKtdt+XAff975T+tsuHT8Tm96aVpYAtA6zPzNe0z+97/H+NiDdHO6KHXibkzL7f5T+qHyNQuyXa6UAP9dNucgeVb64SdEBePRLtAzba4hl9QEJ/pX2N+rMnA5FX9QUT74zN70P75/V2nUeiVbfYHIE4dUdHv385/95PwJZ9k4FVjiH8HDaXZXAYAVtvS/gEynmfEfics+kXRc4IJhAmCFJOJhUGNh+U/mpsBhefjs1viPh7OgwUjiKYcFkp80z+0GUeIf3ClL4ypQfFeoLNyZNjqa9Ga4OA7Ppojoh0XbRBRh2OYRjg+fErUIfvkyC/UcA54+iumPNTHhwtbXAP2/2/NpdzjUPMSZY6OCvePZ1bOu5XztcjuI9vdFhZV8fHe/5JrJ3rrvbRTe60AbrB2QI64B9zXDylv4+mTxwpk3LypzH+huO4IPCkH5YY/UFcVsusyJlAq60B/YDu7ztfp+NO27oymm0t2RWgY2z2ZfM1bRAIZJ9wjHL1/Pt18397VtHavU/JYzeOAKPmUeez5Zrdvdo/2DSypPxXR5MFHhqtbh63EdBk378+Nt97NM7STvfma2C81MDk5mjjnbo8cy/W9zOGOEpkDP1VnP63CxkP/cQOyEK7t3X5CeOfcsZHwjHfTdHGC4sxoF+oV+2f3WL0kPIyBrPf+BSBI8f0Ubv8R5KB4l7JS3h/7CmhL+sCgd/4wAT7RIZqt+gXPT1tvr4kWns3RPOR2Hvfn0t8PJpd5/Op/+xoz6zk86puPhlr3eATXxttAUB/wVWxHi/0Q7XbG6MtaGgPG2NRUXe1YGQvLBJ41uVzHZ7BOHx1rH1czgf3m6/Tbqt/RfaqV/rv1mi+j/7D91VY6PCMuiir4HNGf5ZH5IKA4InBAwyqXY4nYXDiMBj8PCMdTNLns1LrHQXXTB79vUA+x4W7QGbkz5XgYcIz2RUg9bInS+2nM0UHdTWcpH6Si6LpnmfV/LMFTvO5fWaBCY+J+seF9yehN963Bivb7AqoS1mvc0B/o4VLwgflPJPnXxGtbwkSe3h/gspd/UFbS+XIR/l+x9QusDXa2s+44B1HdpcwMS7BpHwYHETenr7/R/4Dlo6+l0An2/QyAvmxA9ohLf1jm/3AAo/AicDlTOyCe7Gt0RgAdLdtHPQs2Utv/7z7QfS9xNL4vTS2/502fM62chGRCwIc8Sui/Qs5VsF1N6PnedHqnK9kwHa+wATJLiYwMTMxjmBng90bkeOC4JOTHfwPC4m9jdJN8Dn5KYCIyAULARor2BfE6Uc1IzgmySOT84UnRjueJmDjyOzURum5y160Y1UmRP7MyBJ87F3/zpjIUcPi4eZo/yiL490l8DX4HBGRCx5WuPzjj7f2BVvg28f9BHfnCgSteQxO4sjtfICds9+b0h9F+79oLHGqzxA5Bvj+9NpYPm7Fx/Ddr4iIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIjIEfAjk96Y72+UaGEAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAaCAYAAAA9rOU8AAABn0lEQVR4Xu2VvytGURjHH6GQoigpElksFFHEZvAjBmwWm40slOku/gEZ5Ecmm/W1MLwZWQxMMliYKQYK32/POd7j6ZX03nsH3U996tznuXXP85xzzxHJyCiNcbgD9+Glk2PG6DJs+Ho7YbrgHDyEH3DBPXtf4TOcdO+nwqboZCxj8B3ewFaTS4QO+ACfbALMiE7yDQ6bXCJMi37wwibAlmjuXFLaOxuiH9yzCXAvum+mbCIJamFedDLzQbwcjsBH0T8uFfwSXcNGk0sdv0RHsMLk4oKFNtmgJVyixe+pWMnBKhu0+F/6BfabXFxwEpENFmNXtCvHol36iVnRM4ZLOuBig/AKNsM6eAJXYRlcgX3uvVHY4sZF6RE94DiR0NPwpYAJ0c3Ndnv45/lNH4l2uBe2wW0pFMcCfl2iv8IlvXNjVn/g5JhFnIneZTyPGCOcRFhAbLDdt27c7sa8t3hf5eG6y4WEBXTD6iBXEmy3r5KHIJeIeyES7RDzniU4JFoAJ9MJ16TQsZKpET2VPVyCcNPzQ7y76oMYqXS5jIz/xyetS04B2OGqZwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAZCAYAAABZ5IzrAAABuklEQVR4Xu2WTSgFURTHj3xEvhIlUSSRUopSZCUbCxa+UrKxsbNgoaxeNjZWspBCspAoSYrdW9gppbBQ6illqZSFDf7/zr0z8+6CvDfvzeb96tebzpnXnDP3zJ0RyZEjHArg1j+c1b9ljjnY4sRe4TccCcQK4QlcD8RCp1j0Ii4shkU1O/E90QYyRjs8c4OiBZ2LFmzh0h7AwUAsdDgPMSdWLlrQshMvg0eiTWSVaZiA9U48EvLgLjwWXaLIqYH3cMFNREU3/ID9biIKuERcKg40ly5yOMQJ0YJ+owkewkvRp25GtIEBGBedQT4YpBHuw3G4AXdER+LPhrnfTMAv+Anzk9MevMCtOe6Ab3AUjpk482TV/M7DVvgYyE2KbiFpUwufxN+fuGNfwyrRJpZE70SPyVs4j3bvYiFxP5UenfAdDos/b/a99gIbzLELC+dmS3rhM2yDld4ZKWK3BBbUJ7pcdlYeJPm9twKLxC/cwu3kAq5JCAWRIXgjehG+fO1SLMJT0QJ51ypMnE3cmWPCr4cr2BWIpUQJ3BTtnLDLmJeNgGrRp2gbTonehdKkMyKAH2h80urcRI5s8QMTb0zkUT4aFgAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAaCAYAAAAT6cSuAAACc0lEQVR4Xu2XS6iNURTHlzzyzDt5P5ISoUR5TMSAAQkjJiZioG5RJMqdGBjcyWUkZSBJyUwkA2WijIgRipEkQ3d28f+19u7ss74zOJ17uOfT+dW/7l378e2119pr72PWp0+f8WCydKtNXZHm+bB6sFEakR5Yw4lf0qh0QzomXUh9vkprfFg9uGjVaPyWXktzC9uJFraehqjdCzYWj3M4U3JEGg62nuakdCbYtko/pPXBfk46HWy1o3bp1y4TpDtWs/RrF1Lyp1VT8m9BluyNRjHJfIM/SzuamzqHM0Ux+Vcp+UE6H43mhe6t9E3aENo6Iqckzo03bPLLaBwLC6T31hvO3bbqFdUxM6Wr5o69C22ZAfN04dJ/Lq0yT6sDqf2NtDL9vUKaLV2WNkvfzV85vHzoz6vnsPn4RWlMZrH0RTpY2FZLg9Ina3xvt/Qxd2gFEzMAp6KIItHMcInT/5V0NtmGzIsPH79uvrCd0l1z5/eYL4ZvLJV2mb9lmYu5b5ofh5Jt5s6xKZktSXkeYJNf5A7dgMrFh4ngNPOHNFHHAT5GRLZLU/MAcU16HGzAhuwPNsDxuLFABc2bwVzM2dUri1cKB32WuYPHk50UWpY7FcwwT2Ecj1A0FkqbzBeeYTMeBhuQNTgORI8oHmo0jx0WmaNwSVqe7NyP5a+FtdKUZCPS+4o2yDvPBnGWox0HI6Q85wxId+bt+n080aopAyyM3eVMZeg7vfi/hPSivYRzRkq2+llF+s+RlkhPzQtMbThlfobvWzUl55tXYzia/s6VuRYMSk+suUpmiNoj89fMM2ldc3PvQ4rGilpCuhPBeHX0+a/4A6Bza2aPkzYAAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABXCAYAAAC5txliAAAIoklEQVR4Xu3da4htZRkH8Ccy6EZWSjcDUyyIrIRIyIokhYrKIgW7UBBh2QWFruiXDoFEHyIR+xBkGlGJSRe6ooKT9iE1KiUVisgiDIOSwgSTLu/fdy1mzZqZ48yc2TObc34/eJi93rX23u+eTw/Pe6sCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGDp/anFAy3+N/w9c3LvGS3+M9y7t8X5k3sbeVKtftazZ/cAADgEJ1dPsj41v9Gc0eKv88aDOLHFX0rCBgCw65KwPTRvbG5s8fZ540EkUfvj8BcAgF305+pJ29zdLU6YNx6EhA0AYEFe3+K/w9/RsbPreGyLC1uc1+K5Lb7R4p7J/XnClrlv0+HWq1v8vcW/Wrys+jy5m4dncu9LLd5Uvdr3sxYrLS5oce3wzGOqy9+Ptbioej/yeT8e7gEAHJae1uK2FlfWalKUZC3tU1l4kMRu9LgW17Q4abieJ2xxSa2dH/fMWk3YRg9X/9zxu9OPJGinDtfj3Li8N86ttc9/pDauEAIAHFaSQCXpeVf1YdA71t5+RO6vzNre3OL31ZOpjRK2JGvThO3JtT5hy/XK5DrPTxOwvGelVt/zYIt/tDhniFT87q9eFdyJscoHALDUnlA9aflh9YUGP1p7+xEbJWxJosYEbK8SttxLgjYmbGOk4rcTSTaTdAIALL1x8cGvauPFBhmGTEI2lQrbz1scXVtL2DLMeqgJW/qZKttUhkfHIdLt+mj1KhsAwNL7ZvVEKX+Pmt2L62r99h+ZozZuqruVhC37vh1qwnZprR/CzOcmaYwsSEil8PoWx1evHqbtiha3DM9EFjp8tcVvW1w2tD2lxU+qP3vM0AYAsDQyNHj38HczWZWZ6lZOSfhni08M7UmqkkSNsTK0Z5gyJybk+q7qCwbGZ06pnuCN10mexmRtjHfOrscKXxKrfG5Wnd7X4t1De5LHsTp4evXvT1/HtlQE872XV+9z5DNf2OJA9cUNSfI+PLkPALBUtrJR7uOrV9GyzcdWjM8necqwZV7vRjI0/dzI8Vg31NrqYL7n67U6XJqEMJW6e8YHqq+QzVBt3ntT9aTuOZP7AMAS+0Gtzuv6d/VKTSKv0/as1UdZAkngMhQ6yh5up7e4eLg+u8XtLY5rcefQlq1DsjL2vdW3E8kQbyQZPW14DQAsuVRekpx9YNKWOVGZR5U5XbtRKWL3ZLgziwg+1OK11Strv6g+h+1r1Yd005a92z5efWj0qhafrz4UmsUHeW/m8e10EQMAsMfeVr0aM9/j68zqiVyGzwAA2EdZPXhtrV81mblQ89WOAADssawc/FuLV83aP1m9upbhNQAA9tFZ1ROz7PGV1YiJ8aD0r0ye202ZOD8ubni0eMHwHgCAI9ZK9YRtt2QF4nQV4yIdOIzi05u0bdY+b5vH/JnNPmsemz2XNgBgn2Q4NNW03ZJk7cC8EQCAnUt1bbOKWLb7yJBkdsbPxq3Zt2s8ginbQ2S/r0j7eFRTDhh/tHlvhkQBALZo3H9teg7m1POqb+2Rcygjz497tWUPr1tbPL96Re2ooT3JXxIyAAAOQY43SqI2jWzEupEkYOMu+geqHz7+kupnU2b/tqkTqyd4kY1390qqf+OCiYPFMiaS6XvONZ33dR7L2HcAYEkkMUsSNp5hmT3ZsqP+SvXjjiLJ2UnDc0na8novd9BP1W9MPDOM+sDwOoem3zu5t4wbAE/7nr5O+57fssx9BwCWxBMnr5OETQ9Dz+v5sVVPr71N1rKP3B2T6wzNZhPgK2ttP35dvVK1F7Itylal7y+aXKfvSdCmfU+SvFd9BwDYdalQ5azMUYYXs/BhrP6Nvlvrk8tF2U41LH2fJmfpexK2qSRse9V3AIBd955aO18uc/GS8GSBxNRrZteLtNWELUnYfK5f+n7brC1VRACAw8ZGQ4p7basJ21yGc9P3DOcCABy2Hq5+YP1+2mnClvNc0/cMge6VY1o8dd4IALBIGw0pLtJpLc6Zxec2aHtj9ZW2B5P98NL3+XDubsicvjNmbanoXdXinrXNAACLsx9DiruVsG22unW3/K76dixTJ7e4sMV9s3YAgIXZjyHFjexkSDR9z3DuXvb9y7WY5BAAYFMHG1JMYvKG6kdqfadWzyh9R4ubqp/o8MoWH2xxY/VTHL5V/fOOH57dqp0kbOn7Rqtb4y0t7qq+WvS66r8hsg9e+n5F9b7nN6bvV7e4psX11U9SuKR69W66IvXmFg+2+GmLtw5t+Z5fVv+ezG3b7IxZAIBtmZ4UMI154nZ3rZ6ZmgQmRz29osX7qm9Km+TsxdWTlXzmuO/ZeNLDdmwnYZv3e4yx76cMcWf1PeZSgftM9b4/VL3v2ag3fc9z2dZkpcWxLU6tnnjm9eW1tpr28uq/bTR+T/aBO676/2plch8AYOEeqJ6kJFEbK0dJbs6rPscslagY55KNxgRmO7aTsG1F+jQmXK+rXilM3++v3vf5SQmXTa7jhFp/+kISuSSBU9Pvyf9o/jkAAAuVSfepRl1U/czOOKtWK1mpWGVSfuaSjZWnVLSS6IxDhvsl/R6rfEkwI32/dXgd44KC9H260e6YoI4LDEZpS6VxKt+T3x/zzwEAWLjPVh/iu6VWK2ypqmXifba8uKD6HK8Mh+a5yLDopS0uHq73Sype32txfoujh7b0/YvV+57fMM5PW6m1x1jlvfkNX6jV98Zvqid9U6mwfb/FgVr/OQAAC5UFBq8eXqdylGrakSoVuj9UX7iQBG2URQa3D6/Pru0vtAAAOCSnV5/z9f4W59aRvZXFgepVxpfO2lNN+3b1odWsRAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYpP8Dq4/Wr9pPD4IAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAaCAYAAADSbo4CAAABoElEQVR4Xu2WzSsFURjGH6Hk+6tslFgRUSyk7K1YyM6GLMjSgo3ib8BKShaS8h+46ZalLUsLpWQhpVgoH8/Te6Y794wyZuYu1Pzq173zzsw973nfM2cukJMTj1q6H9NN2m63Zc8QfaOnKA34ST/oLp2j6+6aB9pnt2XPBqKz/KJXtC0Um/8hlhmqxrEX00BKRAOHmaU7XiwzFuiKFxujT3TAi6/RZS9WUSragrhU0UNUsAVxUVteEW3Lb9TTd1qkjeWnkqE1oIWapC1nyKiSQVuUSBJu6YwfTEInvUHyRO7w95ZGUF+3YElce+cCVDHtsOe0he7RS9pEa2jBxcWR+1T8BLYHVdMDF4/QBSupEvBVdVSlgEH6iFL5w2tCv6PBhBLWJqkkNMEivaDTtNldkwq9Cu5ptztWosHgkyi1RQtd+5BQUquwJ0qT63HxVKjcKn+DO9aaUJWGYQkFT9oEfYG91RfpOCyhUVhVUqOKqB0quQbRrPvpNp2CrZXwX4oR+kyXYKh9ve57arTgtG40YB3KN68OF/NphZ1TVXJy/jffYs5NEG820iQAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAaCAYAAADxNd/XAAACcElEQVR4Xu2WTYhOYRTH//I1QshEokgUkUYTC1lKJJKPlaWF5ZTE9k3ZWUlWIzRZkKJkIRbEQmwoHys1ZMsKhTL+vzn36X3unTGmmXfmlu6/fvXOOc+9c57znHOeKzVq1CjXRnPJPDMfzWWzuLSirEXmmmLtS3PRrMkXTLe6zUHTZ4bMZ8WmRtMMc8r8VKw9YvaZ+fmiurRLkdFfZmfFl7Rdkf3X5nfFV6u6zF1zQZHZM2X3sMj+UXNCseZe2V2vVil64KQiuP6ye1hkf665or9vsjZRPrfNfrWzy6kkLTBXFf3yRmOXWS06p8hor/lmXpglmZ+TOaYImuDfm+WZv1atNU/MSrUzzCbYzDxFOW0q1t5SnBB90AkdN1819uT7pw6Ym2aWYhw+VARJORFoHuyg+W62ZbbJitMlgQurjvGKycNLkhiTbADbgKL+kxidnBAn1QmRNE6VGCYkdn1f5YakF9jAebM1syPsTCFGaidEH9FPh6qO8WimuaF4wWa1g2IikWlKKQlfj/lR+PMNcBO/NRsUzwCliB0bIlGPFc+dNg8UnyR8huQD45U5XPwmvhXF7xGiYWgcMpp4mvneKeb+HHOnsi6x1yxT3MotHrR2mNWZPYkyfKRIFP+XvkN5+VBOz836glZhm1KxCU6leicQINMliQk3qCjPT4qLE3H6jGdEOV1XfF/tNksL+5SKgD5o5FEne9Ie80UxIFKJIdYworcoTm5CvTAZ0Q9kMWV0nTmrCBg7otapeWqfjVE2lMZsRf3TJy3FJ3w6DcQdxPumRdT4aDczvUAz5uJvxjAb4HMlH9P4eCa3NWrU6H/THz/Te8HDeXXoAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAaCAYAAADbhS54AAABzUlEQVR4Xu2WvyuFURjHHzEohIhCiSx+ZVCKjAoDAzYLmyLFokwW/4AMiMRCISmLGITNpJhksFBKymbi++15Tu/puKLuva/l/dSn954f995znuc8516RhIR46Ydrf5RzY6MVjsAj+AjHrO1chS/wE87pW+JlCW7CnHAANMAnOBAOZJtG+Arbg/4mexbCQ9jmjcXCqGiqSr0+LmbPXlfAXXvGCtPIhflpHIZXXjt2GKVr0YWx8jbgrbW54H/DpZGLc5TBE9GzR/JFUxtSLlncwLroh/PpqIc7oovJg1uwzxv3eYBDYWe6+Glk5FLRAo9hcThg8O5zkc0YLP9386ergJGcCjs9LmFR2JkuB6LR4lWQa32sTJ6xLrgNl63PcSNasYTRdJFmRE8lmjsjei/2wkF4Dytt3qzN+UYn/BBd1G9yroNfei5RIXRLlMYF+Axr4SRcEZ3HAuF59TfYY8+MUQ3nvTZ3znNaAM/ghejPVpVEi6gTLRBXPOzn52QUpsb9w2C17otGpFk0kv6iHZzPAqmxNtOZ6vc4LbhTpo90wDc4LnoeN+GijfG8Tls/I3gnugEuaMLmZByemxJ7zS9yRePabszHFRQv6oSEhJAvMzBWOm+ggkcAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAZCAYAAADe1WXtAAAAfklEQVR4XmNgGAWjYMCBLBB3AzEHugQlgB+INwOxJroEpaAciqkOzIBYBV0QGfAAsSQZ+BEQJwExJwMWUMEAUUAq/g/Er4A4noFKgBuI+xhwuJIcwALEU4GYEV2CXAAycCEQe6BLUAKkGSDpVARdghLACsRCDFT0+igYBQQAAC92Ft8h9ZYxAAAAAElFTkSuQmCC>