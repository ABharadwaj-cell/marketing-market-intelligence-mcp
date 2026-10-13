# Marketing Capability Intelligence MCP

Working read-only MCP prototype. Classifies competitor signals by **product line, exact feature, augmentation, ICP, narrative, evidence URL and observation date**. No scraping or proprietary data is included.

## Run tests (no dependencies)
`python -m unittest discover -s tests -v`

## Run JSON analysis
`python src/intelligence.py`

## Run MCP server
`python -m pip install 'mcp>=1.0,<2'`
`python src/mcp_server.py`

MCP tools: `compare_competitor_capabilities`, `list_competitor_signals`. Attach the stdio server to a compatible local client. An MCP server is *not* an AI model; a model-enabled client supplies reasoning.

## Live portfolio page
GitHub Pages from `/docs` after deployment. Dashboard data is synthetic. Production ingestion, authentication, pagination, paid connectors and dynamic snapshots are future work.
