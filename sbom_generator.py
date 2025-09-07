#!/usr/bin/env python3
import json
import os
from datetime import datetime

def parse_requirements(req_file="requirements.txt"):
    """Parse requirements.txt into a list of dependencies"""
    deps = []
    if os.path.exists(req_file):
        with open(req_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "==" in line:
                        name, version = line.split("==")
                    else:
                        name, version = line, "latest"
                    deps.append({"name": name.strip(), "version": version.strip()})
    return deps

def generate_sbom(output_file="sbom_output.json"):
    """Generate a CycloneDX-style SBOM"""
    dependencies = parse_requirements()

    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.4",
        "version": 1,
        "metadata": {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "tools": [
                {"vendor": "CustomScript", "name": "sbom_generator", "version": "1.0"}
            ]
        },
        "components": []
    }

    for dep in dependencies:
        sbom["components"].append({
            "type": "library",
            "name": dep["name"],
            "version": dep["version"],
            "purl": f"pkg:pypi/{dep['name']}@{dep['version']}"
        })

    with open(output_file, "w") as f:
        json.dump(sbom, f, indent=4)

    print(f"SBOM generated successfully → {output_file}")

if __name__ == "__main__":
    generate_sbom()
