"""Esta base de datos recopila indicadores clave de salud, datos de brotes de enfermedades, tasas de va
DOI: https://github.com/juanmoisesd/impacto-sanitario-en-venezuela-20242025-indicadores-clave-factores-y-datos-de-en | GitHub: https://github.com/juanmoisesd/impacto-sanitario-en-venezuela-20242025-indicadores-clave-factores-y-datos-de-en"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/impacto-sanitario-en-venezuela-20242025-indicadores-clave-factores-y-datos-de-en".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). Esta base de datos recopila indicadores clave de salud, datos de brotes de enfer. Zenodo. https://github.com/juanmoisesd/impacto-sanitario-en-venezuela-20242025-indicadores-clave-factores-y-datos-de-en'
def info(): print(f"Dataset: Esta base de datos recopila indicadores clave de salud, datos de brotes de enfer\nDOI: https://github.com/juanmoisesd/impacto-sanitario-en-venezuela-20242025-indicadores-clave-factores-y-datos-de-en\nGitHub: https://github.com/juanmoisesd/impacto-sanitario-en-venezuela-20242025-indicadores-clave-factores-y-datos-de-en")