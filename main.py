import time
from dreamberd import interprete

now = time.time()
# Sourcery will be angry
with open("test.java", "r", encoding="utf-8") as file:
    content: str = file.read()

result: None = interprete(content)
print(f"Took {(time.time() - now):.2f}s")
