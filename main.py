from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Walkman(BaseModel):
    id: int
    name: str
    describtion: str
    year: int 

walkmans_db = [
Walkman(id=1, name="Sony TPS-L2", describtion="The TPS-L2 was the first commercially available personal stereo cassette player",year=1979),
Walkman(id=2, name="Sony WM-2", describtion="This milestone walkman was the second walkman after the legendary TPS-L2 and set the form factor for the DD line",year=1982),
Walkman(id=3, name="Sony WM-DD", describtion="The first model of the 'disc drive' series, the WM-DD, was introduced in 1982, and had a solid reputation for performance",year=1982),
Walkman(id=4, name="Sony WM-7", describtion="The first ever Walkman to have auto reverse and (basic) inline remote control unit. It is one of the most complex of all the Walkman models",year=1982),
Walkman(id=5, name="Sony WM-F5", describtion="The first Walkman developed for use during outdoor activities. Marked the first appearance of the distinctive yellow seen in later sports models",year=1983),
Walkman(id=6, name="Sony WM-20", describtion="Product developed based on creating a Walkman roughly the size of a cassette case",year=1983),
]

@app.get("/Walkmans/")
def get_walkmans():
    return walkmans_db

@app.get("/Walkmans/{walkman_id}")
def get_walkman(walkman_id: int):
    for walkman in walkmans_db:
        if walkman.id == walkman_id:
            return walkman
    raise HTTPException(status_code=404, detail="Walkman not found")

@app.post("/Walkmans/")
def create_walkman(walkman: Walkman):
    for existing_walkman in walkmans_db:
        if existing_walkman.id == walkman.id:
            raise HTTPException(status_code=400, detail="Walkman with this ID already exists")
    walkmans_db.append(walkman)
    return walkman

@app.delete("/Walkmans/{walkman_id}")
def delete_walkman(walkman_id: int):
    for index, walkman in enumerate(walkmans_db):
        if walkman.id == walkman_id:
            del walkmans_db[index]
            return {"message": "Walkman was successfully deleted"}

    raise HTTPException(status_code=404, detail="Walkman not found")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)