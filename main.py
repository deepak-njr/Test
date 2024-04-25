from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define the first endpoint to say "Hello, World!"
@app.get("/hello")
async def get_hello():
    return {"message": "Hello, World!"}

# Define the second endpoint to say "Goodbye!"
@app.get("/goodbye")
async def get_goodbye():
    return {"message": "Goodbye!"}
