# Marketing Market Intelligence MCP

**Competitive intelligence organized around what buyers actually compare, not just company names.**

Imagine you run marketing for a small SaaS business. A competitor announces an AI-assisted scheduling feature. Is that a threat to your scheduling product, a new message your sales team needs, or just noise? A spreadsheet of competitor names won't answer that. You need to understand the *specific feature*, the customer it's for, how it's positioned, and whether your business can credibly respond.

That's the problem this project is exploring.

[Explore the interactive demonstration](https://abharadwaj-cell.github.io/marketing-market-intelligence-mcp/) · [See the buyer-friendly walkthrough](docs/START_HERE.md) · [View the Python engine](src/intelligence.py)

> **Project status:** A working, read-only Python classification prototype with a real stdio MCP interface and synthetic data. Not a continuously running competitive crawler, a hosted AI model, or a production recommendation engine. The Pages link works only after GitHub Pages is enabled.

## Who this is for

**Founder or solo marketer:** Check where a competitor overlaps with your offering without needing to become an analyst first.

**Marketing director / product marketing lead:** Turn competitor changes into a focused discussion about positioning, evidence, customer segments, and go-to-market priorities.

**Marketing analyst / developer:** Inspect the classification rules, connect an MCP client, replace sample inputs with approved data, and build an auditable intelligence workflow.

## What it does today

The starter reads sample competitor observations and compares them with a demo company's **configured capability list**. It shows:

| Lens | Why it matters |
| --- | --- |
| Product category | Competition in scheduling is not automatically competition in payments. |
| Shared capabilities | Where the observation overlaps with the demo offering. |
| Unmatched competitor capabilities | Where a feature isn't in the *configured list*. **This does not prove the company lacks that feature.** |
| Augmentations | Extra functionality, such as AI assistance, automation, or OCR, described separately from base features. |
| Shared ICPs | Whether the observed target audience overlaps with the demo's configured customer segments. |
| Narrative | The customer value the competitor is emphasizing. |
| Source and observation date | What would need checking before anyone acts on the observation. |

**Example, using fictional records:** A scheduling vendor highlights AI triage for multi-site clinics. The system flags overlap in online scheduling and separately lists AI triage as an augmentation. A marketing leader can then ask: *Do we have verified proof for a more useful customer outcome? Is the buyer segment relevant? Is a page update justified?*

That is a **research starting point**, not proof that any product has or lacks a feature.

## Try it without writing code

1. Open the [demo dashboard](https://abharadwaj-cell.github.io/marketing-market-intelligence-mcp/) after Pages is enabled.
2. Filter by product category or fictional competitor.
3. Read the shared capabilities, unmatched features, target segments, and message.
4. Write down the next question that should be verified with product or market evidence. Don't turn demo observations into public claims.

**Decision you should leave with:** *Which specific product capability and buyer segment deserves deeper investigation, and what evidence would justify acting?*

## Run the actual code

Python 3.11+ is sufficient for the classifier; no paid API is needed.

```bash
python -m unittest discover -s tests -v
python src/intelligence.py
```

To launch the **read-only MCP tool server** with a compatible MCP client:

```bash
python -m pip install 'mcp>=1.0,<2'
python src/mcp_server.py
```

MCP tools: `compare_competitor_capabilities` and `list_competitor_signals`. An MCP server exposes tools; it **does not run an AI model or independently search the web**.

Start by examining `fixtures/tenant.json` (fictional company capabilities and ICPs) and `fixtures/signals.json` (fictional competitor observations). Run the classifier again to see how the comparisons change. These examples are intentionally public-safe.

## Where the commercial value could come from

This prototype does **not measure generated revenue**. In a properly integrated system, its findings could support better comparison pages, sales enablement, product positioning, segment-specific content, and qualified opportunity creation. Those effects would need campaign and CRM measurement, not just a competitor-overlap score.

Next build steps: real source validation, historical change detection, product-level identity mapping, expert review, action ownership, and connection to the [Marketing Revenue Lab](https://github.com/ABharadwaj-cell/marketing-revenue-lab).

## Safety and limitations

- Source URLs and competitor names in fixtures are illustrative, **not validated market evidence**.
- Overlap uses simple normalized string matching, so synonyms and nuanced feature relationships can be missed.
- No direct competitor crawling, semantic model inference, API polling, credentials, automatic outreach, publishing, or actual business data is present.
- Do not add confidential documents or customer information to this public repository.
- Any future automated publication must use verified product claims, appropriate permissions, and approval gates.

## Related work

[Marketing Practice Radar](https://github.com/ABharadwaj-cell/marketing-practice-radar) examines emerging marketing methods and experiment hypotheses. [Marketing Revenue Lab](https://github.com/ABharadwaj-cell/marketing-revenue-lab) explains sourced and influenced pipeline. Together, these are building blocks for a broader, independently governed marketing operating system.
