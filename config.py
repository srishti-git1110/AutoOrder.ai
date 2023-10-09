import dotenv
from pydantic import BaseSettings, Field

dotenv.load_dotenv()
class APIConfig(BaseSettings):
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    
config = APIConfig()
