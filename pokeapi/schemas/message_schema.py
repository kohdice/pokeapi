from pydantic import BaseModel


class RootMessageSchema(BaseModel):
    """Response schema class for root."""

    message: str
