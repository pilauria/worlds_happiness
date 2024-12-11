import os
import sys
import pytest

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def sample_data_path():
    """Fixture to provide path to sample data"""
    return os.path.join(os.path.dirname(__file__), '..', 'data', 'regional_happiness_stats.csv')
