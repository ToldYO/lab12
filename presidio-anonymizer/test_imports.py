print("Testing imports...")
try:
    from flask import Flask, jsonify
    print("✓ Flask imports successful")
except ImportError as e:
    print(f"✗ Flask import failed: {e}")

try:
    from presidio_anonymizer import AnonymizerEngine, DeanonymizeEngine
    print("✓ Presidio imports successful")
except ImportError as e:
    print(f"✗ Presidio import failed: {e}")

try:
    from presidio_anonymizer.entities import InvalidParamError
    from presidio_anonymizer.services.app_entities_convertor import AppEntitiesConvertor
    print("✓ Presidio sub-imports successful")
except ImportError as e:
    print(f"✗ Presidio sub-imports failed: {e}")

try:
    from werkzeug.exceptions import BadRequest, HTTPException
    print("✓ Werkzeug imports successful")
except ImportError as e:
    print(f"✗ Werkzeug import failed: {e}")
