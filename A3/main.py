from pathlib import Path

model_path = Path("C:\Users\47480\Documents\DTU\41934 Advanced BIM/A3/CES_BLD_24_11_ARC.ifc")
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

model = ifcopenshell.open(model_path)
