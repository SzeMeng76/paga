import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入主应用
from paga import app

# 确保静态文件目录存在
PAGA_DIR = Path("paga")
if not PAGA_DIR.exists():
    PAGA_DIR.mkdir(parents=True, exist_ok=True)

# 导出handler供Vercel使用
handler = app
