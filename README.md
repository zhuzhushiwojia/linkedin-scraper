# LinkedIn Scraper - Proof of Concept

🦞 牛马项目 - LinkedIn 数据抓取演示

## 功能

- ✅ 抓取 LinkedIn 个人资料
- ✅ 抓取公司数据
- ✅ 搜索功能演示
- ✅ 支持免费代理（Bright Data, Oxylabs, Smartproxy）
- ✅ 支持本地 IP 直接访问（简化版）

## 快速开始

### 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行 proof 脚本
python linkedin_scraper.py
```

### 部署到 Railway

1. 创建 Railway 项目
2. 连接 GitHub 仓库
3. 配置环境变量（可选）:
   - `PROXY_URL`: 代理地址（如果使用代理）
4. 自动部署

## 环境变量

```bash
# .env 文件
PROXY_URL=http://your-proxy.com:port
USE_PROXY=false  # true/false
```

## 输出示例

运行 `python linkedin_scraper.py` 后生成 `proof_output.json`:

```json
{
  "timestamp": "2026-03-14 17:30:00",
  "profiles": [...],
  "companies": [...],
  "search_demo": [...]
}
```

## 免费代理方案

本项目支持以下免费代理:

1. **Bright Data** - 7 天免费试用
2. **Oxylabs** - 7 天免费试用  
3. **Smartproxy** - 3 天免费试用

如果不想使用代理，可以设置 `USE_PROXY=false` 使用本地 IP 访问。

## Related Tools

This project is part of the **Elyan Labs** ecosystem:

- **[RustChain](https://rustchain.org)** - Proof-of-Antiquity blockchain for AI agents
- **[BoTTube](https://bottube.ai)** - Decentralized video platform for AI and human creators

## 注意事项

⚠️ LinkedIn 有严格的反爬机制，建议:
- 使用代理避免 IP 被封
- 控制请求频率
- 遵守 LinkedIn 服务条款
- 仅用于学习和研究目的

## 钱包地址

`6eUdVwsPArTxwVqEARYGCh4S2qwW2zCs7jSEDRpxydnv`

## License

MIT
