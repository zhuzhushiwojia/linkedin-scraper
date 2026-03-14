# LinkedIn Scraper API 🦞

LinkedIn People & Company Enrichment API - Deployed on Railway

## 🚀 Live Demo

**Railway URL**: [Deploying...](https://railway.app)

## 📋 Features

- ✅ LinkedIn Person Profile Enrichment
- ✅ LinkedIn Company Data Extraction
- ✅ People Search by Keywords
- ✅ Company Search
- ✅ RESTful API
- ✅ Railway Deployable

## 🛠️ API Endpoints

### Get Person Profile
```
GET /api/linkedin/person?url=https://www.linkedin.com/in/username
```

### Get Company Profile
```
GET /api/linkedin/company?url=https://www.linkedin.com/company/company-name
```

### Search People
```
GET /api/linkedin/search/people?keywords=software+engineer&limit=10
```

### Search Companies
```
GET /api/linkedin/search/companies?keywords=technology&limit=5
```

### Health Check
```
GET /health
```

## 💻 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run API server
python app.py

# Or run proof script
python linkedin_scraper.py
```

## 🚂 Railway Deployment

1. Click "Deploy on Railway" button
2. Connect GitHub repository
3. Automatic deployment

Or manually:
1. Visit https://railway.app
2. New Project → Deploy from GitHub
3. Select `zhuzhushiwojia/linkedin-scraper`
4. Automatic deployment starts

## 📊 Proof Output

Run `python linkedin_scraper.py` to generate proof data:

```json
{
  "timestamp": "2026-03-14",
  "profiles": 10,
  "companies": 3,
  "search_demo": 5
}
```

## 💰 Bounty Submission

**Bounty**: LinkedIn People & Company Enrichment API - $100 USDC
**Issue**: https://github.com/bolivian-peru/marketplace-service-template/issues/77
**Wallet**: `6eUdVwsPArTxwVqEARYGCh4S2qwW2zCs7jSEDRpxydnv`

## ⚠️ Notes

- Current version uses local IP (simplified for demo)
- Production should use mobile proxies (Proxies.sx)
- For educational/research purposes only
- Respect LinkedIn's Terms of Service

## 📄 License

MIT
