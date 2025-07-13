import os
import json
import argparse
from datetime import datetime


# Argument parser
parser = argparse.ArgumentParser(description="🐟 Marine Species Predictor")
parser.add_argument("--image", type=str, required=True, help="Path to test image")
parser.add_argument("--export", action="store_true", help="Export prediction to JSON")
args = parser.parse_args()

# Check if image exists
if not os.path.exists(args.image):
    print("❌ Error: Image path not found!")
    exit()

# Run prediction
result = predict_species(args.image)

# Export if flag is set
if args.export:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join("exports", f"prediction_{timestamp}.json")
    os.makedirs("exports", exist_ok=True)
    
    with open(out_path, "w") as f:
        json.dump(result, f, indent=4)
    
    print(f"\n✅ Exported prediction to: {out_path}")
