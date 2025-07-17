from fastapi import FastAPI

app = FastAPI()

#di comment ba2a 3aizeen n3mlha pull

@app.get("/")
def root():
    return {"Message": " This is the root endpoint"}


@app.get("/minus/{a}/{b}")
def minus(a, b):
    try:
        a_num = float(a)
        b_num = float(b)
        result = a_num - b_num
        if a_num.is_integer():
            a_num = int(a_num)
        if b_num.is_integer():
            b_num = int(b_num)
        if result.is_integer():
            result = int(result)
        return {f"a = {a}, b = {b}, a - b = {result}"}
    except ValueError:
        return {"Error": " Both values must be of numerical value"}
