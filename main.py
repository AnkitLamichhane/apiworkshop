from fastapi import FastAPI, Depends
# from .models import Person
from sqlalchemy.orm import Session
import database
import models


app = FastAPI()


@app.get("/student/{id}")
def get_user(id: int, db: Session = Depends(database.get_db)):
    data = db.query(models.student).filter(models.student.id == id).first()
    return {"data": data}

     #127.0.0.1:8000/person

#postmethod is used to add data in database 
@app.post("/person")
def add_person( username:str, password : str,email :str, blog_id:int, db: Session=Depends(database.get_db)):
 data= models.Person(person_username = username, person_password = password, person_email = email, blog_id = blog_id )
 db.add(data)  #database mah lagera data lai add gareko
 db.commit()
 return{"status":201,"message": "Data Added Successfully","data":data}

#getmethod is use to read data 
 @app.get("/person/{id}")
 def get_person_by_id(id: int , db: Session = Depends(database.get_db)):
    data = db.query(models.Person).filter(models.Person.person_id == id).first()
    return {"status":200 , "message": "Data Found", "data": data}



