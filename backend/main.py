import os
import logging
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Configure standard logging for debugging and security auditing
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Fail-safe validation to ensure API key is present before starting the server
if not GEMINI_API_KEY:
    logger.critical("GEMINI_API_KEY is missing in the environment variables.")
    raise ValueError("CRITICAL: GEMINI_API_KEY environment variable not set.")

# Initialize the modern Google GenAI Client
client = genai.Client(api_key=GEMINI_API_KEY)

# Initialize FastAPI application with metadata
app = FastAPI(
    title="Peace AI Backend API",
    description="Core backend engine for Peace AI wellness and productivity assistant.",
    version="1.0.0"
)

# Enable CORS middleware to allow secure communication with the Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# Define strict request payload validation to prevent empty or oversized inputs
class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="User input message for the AI assistant."
    )


# Define structured response payload
class ChatResponse(BaseModel):
    status: str
    reply: str


@app.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint to verify backend service availability."""
    return {
        "status": "online",
        "service": "Peace AI Backend",
        "version": "1.0.0"
    }


@app.post("/api/v1/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_with_peace_ai(request: ChatRequest):
    """Process user messages and return AI-generated responses using the latest GenAI SDK."""
    try:
        # Strip leading/trailing whitespace and validate content
        clean_message = request.message.strip()
        if not clean_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Message cannot contain only whitespace."
            )

        logger.info("Processing incoming chat request with gemini-2.5-flash.")
        
        # Generate content using the modern client and configuration
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=clean_message,
            config=types.GenerateContentConfig(
                max_output_tokens=2048,
            )
        )

        # Ensure the model returned valid text before responding
        if not response or not response.text:
            logger.error("Received empty response from Gemini API.")
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="AI model failed to generate a valid response."
            )

        return ChatResponse(status="success", reply=response.text)

    except HTTPException:
        # Re-raise explicit HTTP exceptions without modification
        raise
    except Exception as e:
        # Log the detailed exception internally without exposing system internals to the client
        logger.error(f"Unexpected error during chat generation: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal server error occurred while processing your request."
        )