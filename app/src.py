import os
from pydantic import BaseModel

class SampleModel(BaseModel):
    __root__: str

print(SampleModel(__root__=os.environ['ENV_SAMPLE']))