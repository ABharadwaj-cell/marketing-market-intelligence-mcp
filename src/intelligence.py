import json
from pathlib import Path
from urllib.parse import urlparse

def analyze_signal(signal, tenant):
    required=('id','competitor','source_url','observed_at','product_line','capabilities','augmentations','icps','narrative')
    missing=[k for k in required if k not in signal]
    if missing: raise ValueError('Missing fields: '+', '.join(missing))
    u=urlparse(signal['source_url'])
    if u.scheme not in ('http','https') or not u.netloc: raise ValueError('Valid source URL required')
    offered=set(x.casefold() for x in tenant['approved_capabilities'])
    found=set(x.casefold() for x in signal['capabilities'])
    overlap=sorted(found & offered)
    gaps=sorted(found - offered)
    icps=sorted(set(x.casefold() for x in signal['icps']) & set(x.casefold() for x in tenant['icps']))
    return {'id':signal['id'],'competitor':signal['competitor'],'category':signal['product_line'],'overlap':overlap,'unmatched_capabilities':gaps,'augmentations':signal['augmentations'],'icp_overlap':icps,'narrative':signal['narrative'],'source_url':signal['source_url'],'observed_at':signal['observed_at'],'suggested_followup':'Validate positioning and proof' if overlap else 'Determine whether adjacent threat merits research','status':'analysis_only'}

def analyze_all(signals, tenant): return [analyze_signal(s,tenant) for s in signals]

if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]
    print(json.dumps(analyze_all(json.loads((root/'fixtures/signals.json').read_text()),json.loads((root/'fixtures/tenant.json').read_text())),indent=2))
