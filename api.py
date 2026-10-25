"""
Blackbird OSINT API
FastAPI wrapper for Blackbird username/email search functionality
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional, List
import os
import sys
import logging
from datetime import datetime
import asyncio
from concurrent.futures import ThreadPoolExecutor
import uvicorn

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import config
from modules.whatsmyname.list_operations import checkUpdates
from modules.core.username import verifyUsername
from modules.core.email import verifyEmail
from modules.utils.userAgent import getRandomUserAgent
from modules.export.file_operations import createSaveDirectory
from modules.export.json import saveToJson
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Blackbird OSINT API",
    description="Search for usernames and emails across 600+ platforms",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Thread pool for blocking operations
executor = ThreadPoolExecutor(max_workers=4)

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Pydantic models
class UsernameSearchRequest(BaseModel):
    username: str
    filter: Optional[str] = None
    no_nsfw: bool = False
    timeout: int = 30
    max_concurrent_requests: int = 30
    use_ai: bool = False


class EmailSearchRequest(BaseModel):
    email: EmailStr
    filter: Optional[str] = None
    no_nsfw: bool = False
    timeout: int = 30
    max_concurrent_requests: int = 30
    use_ai: bool = False


class SearchResponse(BaseModel):
    query: str
    query_type: str
    found_accounts: List[dict]
    total_found: int
    search_date: str
    ai_analysis: Optional[dict] = None


class HealthResponse(BaseModel):
    status: str
    version: str
    sites_count: int


def initialize_config():
    """Initialize the config object for API usage"""
    if not os.path.exists("logs/"):
        os.makedirs("logs/")
    
    # Initialize config with defaults
    config.username = None
    config.username_file = None
    config.permute = False
    config.permuteall = False
    config.csv = False
    config.pdf = False
    config.json = False
    config.filter = None
    config.no_nsfw = False
    config.dump = False
    config.proxy = None
    config.verbose = False
    config.ai = False
    config.setup_ai = False
    config.timeout = 30
    config.max_concurrent_requests = 30
    config.email = None
    config.email_file = None
    config.no_update = True  # Skip updates in API mode
    config.about = False
    config.instagram_session_id = os.getenv("INSTAGRAM_SESSION_ID")
    config.api_url = os.getenv("API_URL")
    
    # Use a simple console wrapper that doesn't output to terminal
    from rich.console import Console
    import io
    config.console = Console(file=io.StringIO(), force_terminal=False)
    
    config.dateRaw = datetime.now().strftime("%m_%d_%Y")
    config.datePretty = datetime.now().strftime("%B %d, %Y")
    config.userAgent = getRandomUserAgent(config)
    config.usernameFoundAccounts = None
    config.emailFoundAccounts = None
    config.currentUser = None
    config.currentEmail = None
    config.splash_line = ""


@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    logger.info("Starting Blackbird OSINT API...")
    initialize_config()
    
    # Check for updates on startup (only once)
    try:
        checkUpdates(config)
        logger.info("Sites database updated successfully")
    except Exception as e:
        logger.warning(f"Could not update sites database: {e}")


@app.get("/", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    try:
        # Count available sites
        sites_count = 0
        username_data_path = "data/wmn-metadata.json"
        if os.path.exists(username_data_path):
            import json
            with open(username_data_path, 'r') as f:
                data = json.load(f)
                sites_count = len(data.get('sites', []))
        
        return {
            "status": "healthy",
            "version": "1.0.0",
            "sites_count": sites_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def perform_username_search(username: str, search_config: dict) -> dict:
    """Perform username search in a thread"""
    # Create a new config for this search
    initialize_config()
    
    config.currentUser = username
    config.filter = search_config.get('filter')
    config.no_nsfw = search_config.get('no_nsfw', False)
    config.timeout = search_config.get('timeout', 30)
    config.max_concurrent_requests = search_config.get('max_concurrent_requests', 30)
    config.ai = search_config.get('use_ai', False)
    
    # Perform the search
    verifyUsername(username, config)
    
    result = {
        'found_accounts': config.usernameFoundAccounts or [],
        'ai_analysis': None
    }
    
    # AI analysis if requested
    if config.ai and config.usernameFoundAccounts and len(config.usernameFoundAccounts) > 2:
        try:
            from modules.ai.client import send_prompt
            from modules.ai.key_manager import load_api_key_from_file
            
            apikey = load_api_key_from_file(config)
            if apikey:
                site_names = [account.get("name", "") for account in config.usernameFoundAccounts]
                if site_names:
                    prompt = ", ".join(site_names)
                    ai_data = send_prompt(prompt, config)
                    if ai_data:
                        result['ai_analysis'] = ai_data
        except Exception as e:
            logger.error(f"AI analysis failed: {e}")
    
    return result


def perform_email_search(email: str, search_config: dict) -> dict:
    """Perform email search in a thread"""
    # Create a new config for this search
    initialize_config()
    
    config.currentEmail = email
    config.filter = search_config.get('filter')
    config.no_nsfw = search_config.get('no_nsfw', False)
    config.timeout = search_config.get('timeout', 30)
    config.max_concurrent_requests = search_config.get('max_concurrent_requests', 30)
    config.ai = search_config.get('use_ai', False)
    
    # Perform the search
    verifyEmail(email, config)
    
    result = {
        'found_accounts': config.emailFoundAccounts or [],
        'ai_analysis': None
    }
    
    # AI analysis if requested
    if config.ai and config.emailFoundAccounts and len(config.emailFoundAccounts) > 2:
        try:
            from modules.ai.client import send_prompt
            from modules.ai.key_manager import load_api_key_from_file
            
            apikey = load_api_key_from_file(config)
            if apikey:
                site_names = [account.get("name", "") for account in config.emailFoundAccounts]
                if site_names:
                    prompt = ", ".join(site_names)
                    ai_data = send_prompt(prompt, config)
                    if ai_data:
                        result['ai_analysis'] = ai_data
        except Exception as e:
            logger.error(f"AI analysis failed: {e}")
    
    return result


@app.post("/search/username", response_model=SearchResponse)
async def search_username(request: UsernameSearchRequest):
    """
    Search for a username across 600+ platforms
    
    - **username**: Username to search for
    - **filter**: Filter sites by property (e.g., "cat=social")
    - **no_nsfw**: Exclude NSFW sites from search
    - **timeout**: Request timeout in seconds
    - **max_concurrent_requests**: Maximum concurrent requests
    - **use_ai**: Enable AI-powered profiling (requires API key)
    """
    try:
        logger.info(f"Username search requested: {request.username}")
        
        search_config = {
            'filter': request.filter,
            'no_nsfw': request.no_nsfw,
            'timeout': request.timeout,
            'max_concurrent_requests': request.max_concurrent_requests,
            'use_ai': request.use_ai
        }
        
        # Run blocking search in thread pool
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            executor,
            perform_username_search,
            request.username,
            search_config
        )
        
        return {
            "query": request.username,
            "query_type": "username",
            "found_accounts": result['found_accounts'],
            "total_found": len(result['found_accounts']),
            "search_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ai_analysis": result['ai_analysis']
        }
        
    except Exception as e:
        logger.error(f"Username search error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.post("/search/email", response_model=SearchResponse)
async def search_email(request: EmailSearchRequest):
    """
    Search for an email across multiple platforms
    
    - **email**: Email address to search for
    - **filter**: Filter sites by property (e.g., "cat=social")
    - **no_nsfw**: Exclude NSFW sites from search
    - **timeout**: Request timeout in seconds
    - **max_concurrent_requests**: Maximum concurrent requests
    - **use_ai**: Enable AI-powered profiling (requires API key)
    """
    try:
        logger.info(f"Email search requested: {request.email}")
        
        search_config = {
            'filter': request.filter,
            'no_nsfw': request.no_nsfw,
            'timeout': request.timeout,
            'max_concurrent_requests': request.max_concurrent_requests,
            'use_ai': request.use_ai
        }
        
        # Run blocking search in thread pool
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            executor,
            perform_email_search,
            request.email,
            search_config
        )
        
        return {
            "query": request.email,
            "query_type": "email",
            "found_accounts": result['found_accounts'],
            "total_found": len(result['found_accounts']),
            "search_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ai_analysis": result['ai_analysis']
        }
        
    except Exception as e:
        logger.error(f"Email search error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/search/username/{username}", response_model=SearchResponse)
async def search_username_get(
    username: str,
    no_nsfw: bool = False,
    use_ai: bool = False,
    timeout: int = 30,
    max_concurrent_requests: int = 30,
    filter: Optional[str] = None
):
    """
    Search for a username via GET request (simple URL access)
    
    - **username**: Username to search for (in URL path)
    - **no_nsfw**: Exclude NSFW sites (query parameter)
    - **use_ai**: Enable AI analysis (query parameter)
    - **timeout**: Request timeout in seconds (query parameter)
    - **max_concurrent_requests**: Max concurrent requests (query parameter)
    - **filter**: Filter sites by property (query parameter)
    
    Example: /search/username/johndoe?no_nsfw=true
    """
    try:
        logger.info(f"GET Username search requested: {username}")
        
        search_config = {
            'filter': filter,
            'no_nsfw': no_nsfw,
            'timeout': timeout,
            'max_concurrent_requests': max_concurrent_requests,
            'use_ai': use_ai
        }
        
        # Run blocking search in thread pool
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            executor,
            perform_username_search,
            username,
            search_config
        )
        
        return {
            "query": username,
            "query_type": "username",
            "found_accounts": result['found_accounts'],
            "total_found": len(result['found_accounts']),
            "search_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ai_analysis": result['ai_analysis']
        }
        
    except Exception as e:
        logger.error(f"GET Username search error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/search/email/{email}", response_model=SearchResponse)
async def search_email_get(
    email: str,
    no_nsfw: bool = False,
    use_ai: bool = False,
    timeout: int = 30,
    filter: Optional[str] = None
):
    """
    Search for an email via GET request (simple URL access)
    
    - **email**: Email to search for (in URL path)
    - **no_nsfw**: Exclude NSFW sites (query parameter)
    - **use_ai**: Enable AI analysis (query parameter)
    - **timeout**: Request timeout in seconds (query parameter)
    - **filter**: Filter sites by property (query parameter)
    
    Example: /search/email/test@example.com?no_nsfw=true
    """
    try:
        logger.info(f"GET Email search requested: {email}")
        
        search_config = {
            'filter': filter,
            'no_nsfw': no_nsfw,
            'timeout': timeout,
            'max_concurrent_requests': 30,
            'use_ai': use_ai
        }
        
        # Run blocking search in thread pool
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            executor,
            perform_email_search,
            email,
            search_config
        )
        
        return {
            "query": email,
            "query_type": "email",
            "found_accounts": result['found_accounts'],
            "total_found": len(result['found_accounts']),
            "search_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ai_analysis": result['ai_analysis']
        }
        
    except Exception as e:
        logger.error(f"GET Email search error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        log_level="info"
    )
