import torch
from typing import Dict, Any

def save_model(model, path: str, metadata: Dict[str, Any] = None):
    """Save model with optional metadata"""
    state = {
        'state_dict': model.state_dict(),
        'metadata': metadata or {}
    }
    torch.save(state, path)

def load_model(model, path: str):
    """Load model with its metadata"""
    state = torch.load(path)
    model.load_state_dict(state['state_dict'])
    return state.get('metadata', {})