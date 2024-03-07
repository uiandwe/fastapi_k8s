from fastapi import FastAPI

# FastAPI 인스턴스 생성
app = FastAPI()

# GET 요청 핸들러


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
## 2. FastAPI 튜토리얼 코드 작성
