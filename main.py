from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/lifenum/")
def read_lifenum(dob: Optional[str] = None):
    return {
        "ABC": "336",
        "DEF": "156",
        "CFG": "663",
        "CGH": "639",
        "FGI": "639",
        "IHJ": "999",
        "ACK": "369",
        "BCL": "369",
        "KLM": "999",
        "DFN": "167",
        "EFO": "562",
        "NOP": "729",
        "QRS": "336",
        "AEG": "2",
        "having_numbers": "1,3,5,6",
        "missing_numbers": "2,4,7,8,9"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
