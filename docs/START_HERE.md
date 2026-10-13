# Start here: competitive intelligence without the spreadsheet headache

This project helps you *ask better competitive questions*. It doesn't pretend to know everything about a market. Start with the interactive demo, then use the Python project if you want to inspect how its decisions are made.

## If you're a founder running marketing alone

**Time needed:** Five minutes. No code.

Open the [demo dashboard](https://abharadwaj-cell.github.io/marketing-market-intelligence-mcp/). Choose **Patient access**, then select **ExampleFlow**. It is a fictional competitor.

The card tells you that online scheduling overlaps with the fictional company's configured features. A waitlist is not found in that configuration, and AI triage is listed as an augmentation.

**What should you actually do?** Don't publish a comparison page yet. Check your own product documentation, ask who the relevant buyer is, and find independent evidence of what the competing functionality really does. If the difference matters to buyers, create a specific positioning or sales-enablement task.

A useful first decision sounds like this:

> Investigate scheduling for multi-site clinics this week. Confirm whether our current offer solves the same underlying problem and collect one verified customer example before we update our messaging.

## If you lead a marketing function

Use the same classification to separate noise from commercially relevant changes.

| Question | Why it matters | Who to involve |
| --- | --- | --- |
| Is the same feature being compared? | Avoid category-level claims that aren't product-accurate | Product marketing / Product |
| Does the ICP overlap? | Prevent irrelevant competitor panic | Sales / Market research |
| Is the augmentation new? | Distinguish a feature enhancement from an entirely new offering | Product |
| What outcome is promised? | Compare buyer value, not slogans | Marketing leadership |
| Is the evidence credible? | Keep public claims defensible | Product / Legal when required |
| What commercial outcome are we targeting? | Avoid research without action | RevOps / Sales |

A sensible next step might be a focused landing-page review, new competitor objection handling, or no action at all.

## If you work in analytics or engineering

The classifier lives in [src/intelligence.py](../src/intelligence.py), with tests in [tests/test_intelligence.py](../tests/test_intelligence.py). The demo inputs are [fixtures/signals.json](../fixtures/signals.json) and [fixtures/tenant.json](../fixtures/tenant.json).

Run `python src/intelligence.py` to see structured comparisons. Run `python -m unittest discover -s tests -v` before making changes. The optional MCP server in `src/mcp_server.py` exposes read-only tools to compatible clients after installing `mcp`.

The current comparison uses exact feature names normalized to lowercase; **it cannot resolve synonyms or verify facts by itself**. Keep source verification independent from classification.

## What success would eventually look like

In a live environment, a useful finding should become a measurable decision: identify a relevant competitive gap, create an approved change, evaluate engagement or qualified opportunities, and record whether it helped pipeline.

Right now, this is a **working foundation and demonstration**, not evidence of those business outcomes. Honest limitations are part of making a trustworthy tool.
