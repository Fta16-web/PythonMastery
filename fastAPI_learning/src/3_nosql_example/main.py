from fastapi import FastAPI, HTTPException
from database import db  # Your MongoDB database connection object
from scalar_fastapi import get_scalar_api_reference  # For optional API reference UI

# Used to convert string IDs (from requests) into MongoDB's _id ObjectId type
from bson import ObjectId

# Pydantic imports:
# - BaseModel for defining data schemas (validation)
# - EmailStr for email validation
# - field_validator to add custom validation logic on model fields
from pydantic import BaseModel, EmailStr, field_validator

# The users collection from your MongoDB database
from database import user_collection

# Initialize FastAPI app
app = FastAPI()


# Define a Tweet schema for embedded tweets in users
class Tweet(BaseModel):
    content: str  # The tweet's textual content
    hashtags: list[str]  # List of hashtags (strings)


# Define the User schema for user data validation and serialization
class User(BaseModel):
    name: str
    email: EmailStr  # Validated email field using Pydantic's EmailStr
    age: int
    tweets: list[Tweet] | None = None  # Optional list of tweets; None if no tweets

    # Custom validator for 'age' field ensuring age between 18 and 100
    @field_validator("age")
    def validate_age(cls, value):
        if value < 18 or value > 100:
            raise ValueError("Age must be between 18 and 100")
        return value


# Extend User schema to add an 'id' field for responses (string representation of MongoDB's _id)
class UserResponse(User):
    id: str


# -------------------------------
# API Endpoints
# -------------------------------


# GET /users - Fetch all users from MongoDB
@app.get("/users")
def read_users() -> list[UserResponse]:
    users = []
    # Loop over all documents returned from the MongoDB collection 'users'
    for user in user_collection.find():
        # MongoDB stores IDs in '_id' as ObjectId, convert to string for JSON serialization
        user["id"] = str(user["_id"])
        # Remove '_id' to avoid duplicate/confusing fields in the response
        user.pop("_id")
        # Create a Pydantic UserResponse model instance from MongoDB document
        users.append(UserResponse(**user))
    return users


# POST /user - Create a new user in the database
@app.post("/user")
def create_user(user: User) -> UserResponse:
    # Insert the user data into MongoDB, exclude any None fields
    result = user_collection.insert_one(user.model_dump(exclude_none=True))
    # Prepare the response including the inserted document ID as 'id'
    user_response = UserResponse(id=str(result.inserted_id), **user.model_dump())
    return user_response


# DELETE /user/{user_id} - Delete a user by their MongoDB ObjectId
@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    # Validate that the provided user_id is a valid ObjectId string
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")

    # Attempt to delete the user document with the specified ObjectId
    result = user_collection.delete_one({"_id": ObjectId(user_id)})

    # If no documents were deleted, user was not found
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    # Return a success message
    return {"message": f"User {user_id} deleted successfully"}


# Root endpoint to check MongoDB server status (basic health check)
@app.get("/")
def read_root():
    server_status = db.command("serverStatus")  # MongoDB server status command
    return {"ok": server_status["ok"]}  # Return 1 if server is healthy


# Optional endpoint to return an API reference page (not included in Swagger docs)
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
