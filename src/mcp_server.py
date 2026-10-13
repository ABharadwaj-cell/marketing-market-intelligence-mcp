"""Read-only MCP server. Optional package: pip install 'mcp>=1.0,<2'."""
import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from intelligence import analyze_all
ROOT=Path(__file__).resolve().parents[1]
mcp=FastMCP('Marketing Capability Intelligence')
@mcp.tool()
def compare_competitor_capabilities() -> str:
    """Analyze fixture competitors by exact capabilities, augmentations and ICP; read-only demo."""
    signals=json.loads((ROOT/'fixtures/signals.json').read_text())
    tenant=json.loads((ROOT/'fixtures/tenant.json').read_text())
    return json.dumps({'synthetic_data':True,'results':analyze_all(signals,tenant)},indent=2)
@mcp.tool()
def list_competitor_signals() -> str:
    """Return timestamped public-demo signal records with source references."""
    return (ROOT/'fixtures/signals.json').read_text()
if __name__=='__main__':mcp.run()
