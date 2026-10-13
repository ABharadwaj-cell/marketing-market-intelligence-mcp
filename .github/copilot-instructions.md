# Working instructions for this repository

## Why this project exists
Classify competitors at the specific product, workflow, feature, augmentation, ICP and narrative level. Do not equate a missing entry in a configured list with the real absence of a product feature.

## Who you are building for
- **Solo founders and nontechnical executives:** Lead with the decision they can make and the question they should ask next. Do not require familiarity with Python, MCP or marketing attribution to understand the demo.
- **CMOs and marketing directors:** Explain evidence, trade-offs, operating implications and commercial relevance.
- **Practitioners and developers:** Keep implementation details and limitations inspectable, with runnable tests and explicit source definitions.

## Business outcome to protect
Help a founder decide which competitive difference merits evidence gathering, positioning, product discussion or sales enablement. Qualified demand and pipeline are downstream hypotheses, not current measurements.

## How to write
Write the way a thoughtful marketing operator explains their work to another human. Use direct sentences, concrete examples, accurate terminology and active voice. Avoid inflated claims, buzzword stacks, fake case studies, jargon without explanation, keyword stuffing and generic AI-sounding praise. Keep the tone credible and approachable. Avoid em dashes. Use descriptive page titles, a clear opening answer, logical headings and natural terminology so searchers and readers can understand the project.

## When changing the product
1. Start with the user problem and the real business decision.
2. Check what the current code and data actually support. Don't describe a roadmap item as implemented.
3. Prefer a plain-English first-use path followed by an advanced technical path.
4. Keep a visible separation among synthetic demo data, verified source evidence, opinion, forecast and measured results.
5. Update the README, start-here guide and demo UI when functionality or interpretation changes.
6. Add or update tests, execute them where possible, and report whether they actually passed.
7. Never silently rewrite historical evidence, create invented results, expose credentials or upload private company/customer data.

## Implementation map
src/intelligence.py, src/mcp_server.py, fixtures/tenant.json, fixtures/signals.json, tests/test_intelligence.py, docs/index.html

## Project-specific guardrails
Preserve source attribution; validate URLs and required fields; don't imply the synthetic fixtures describe real competitors; keep MCP tools read-only; test capability overlap and taxonomy behavior.

## Definition of done
A first-time visitor can answer: What problem does this solve? Who is it for? What can I try right now? What can the output help me decide? What is still missing? An experienced reviewer can then find the code, understand the data rules, run the tests and identify the limits without guesswork.

This file guides contributors and coding assistants. It is not a substitute for deterministic security policies, human authorization or actual test results.
