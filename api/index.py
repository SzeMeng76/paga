from fastapi import FastAPI
from starlette.responses import HTMLResponse

# 创建应用
app = FastAPI()

# 简单的根路由
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>测试页面</title>
        </head>
        <body>
            <h1>测试页面</h1>
            <p>这是一个简单的测试页面，用于验证FastAPI应用能否在Vercel上运行。</p>
        </body>
    </html>
    """

# 健康检查接口
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 导出handler
handler = app
