from pydantic import BaseModel, ConfigDict
from typing import Dict, Any, List, Optional
from datetime import datetime

class UnitSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    base_stat: Dict[str, Any]
    growth_stat: Optional[Dict[str, Any]] = None
    updated_at: datetime = None