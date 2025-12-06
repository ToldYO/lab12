# Direct test without running full server
from app import create_app

app = create_app()

print("=== Registered Routes ===")
for rule in app.url_map.iter_rules():
    print(f"  {rule.rule}")

print("\n=== Checking for genz-preview ===")
found = False
for rule in app.url_map.iter_rules():
    if 'genz-preview' in rule.rule:
        print(f"  ✓ FOUND: {rule.rule}")
        found = True
        break

if not found:
    print("  ✗ NOT FOUND: /genz-preview")
    
    # Let's check what's actually in the Server class
    print("\n=== Debug: Checking Server class ===")
    import inspect
    from app import Server
    
    server = Server()
    methods = [name for name in dir(server.app) if not name.startswith('_')]
    print(f"App methods: {methods}")
