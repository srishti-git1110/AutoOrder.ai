import dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

dotenv.load_dotenv()
class APIConfig(BaseSettings):
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    
config = APIConfig()
