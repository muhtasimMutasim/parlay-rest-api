
"""

This is the entry point for the REST api.

How to run FastAPI file:

    uvicorn main:app --host {insert ip address} --port {desired port number} --reload
    
    uvicorn main:app --host 0.0.0.0 --port 5057 --reload
    
"""

from app.main import app

app = app


