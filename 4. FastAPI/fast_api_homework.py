from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


#http://127.0.0.1:8000/suma?a=1&a=2&a=3
@app.get("/suma")
def Suma(a: List[int] = Query(None)):
    return {"suma": sum(a)}

#http://127.0.0.1:8000/resta?a=1&a=2&a=3
@app.get("/resta")
def Resta(a: List[int] = Query(None)):
    result = a[0]
    for i in range(1, len(a)):
        result = result-a[i]
    return {"resta": result}

#http://127.0.0.1:8000/multiplicacion?a=1&a=2&a=3
@app.get("/multiplicacion")
def Multiplicacion(a: List[int] = Query(None)):
    result = a[0]
    for i in range(1, len(a)):
        result = result*a[i]
    return {"multiplicación": result}

#http://127.0.0.1:8000/division?a=1&a=2&a=3
@app.get("/division")
def Division(a: List[int] = Query(None)):
    result = a[0]
    for i in range(1, len(a)):
        result = result/a[i]
    return {"división": result}


#http://127.0.0.1:8000/operacion/1?a=1&a=2&a=3
@app.get("/operacion/{numero}")
def Operacion(numero: int, a: List[int] = Query(None)):
    result = a[0]
    if numero == 1: #Suma
        result = sum(a)
    elif numero == 2: #Resta
        for i in range(1, len(a)):
            result = result - a[i]
    elif numero == 3: #Multiplicacion
        for i in range(1, len(a)):
            result = result * a[i]
    elif numero == 4: #Division
        for i in range(1, len(a)):
            result = result / a[i]

    return {"resultado": result}