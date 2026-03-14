# Railway Deployment Guide

## 🚀 Quick Deploy (Recommended)

### Option 1: Manual Deploy via Railway Dashboard

1. Visit https://railway.app
2. Click "Login" → Login with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose repository: `zhuzhushiwojia/linkedin-scraper`
6. Railway will auto-detect Python/Flask and deploy
7. Wait 2-3 minutes for deployment
8. Click "Generate Domain" to get public URL
9. Copy the URL and share

### Option 2: Railway CLI

```bash
# Install Railway CLI (if not installed)
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

### Option 3: GitHub Actions (Auto-deploy)

1. Go to https://railway.app
2. Create new project
3. Click "Settings" → "Variables"
4. Add `RAILWAY_TOKEN` (get from Railway dashboard)
5. Push to main branch triggers auto-deploy

---

## 📋 Environment Variables (Optional)

```bash
# Proxy configuration (for production)
PROXY_URL=http://your-proxies-sx-url:port
USE_PROXY=false  # Set to true when using proxies

# Port (Railway auto-sets this)
PORT=8080
```

---

## ✅ Deployment Checklist

- [x] Procfile created
- [x] railway.json configured
- [x] nixpacks.toml ready
- [x] requirements.txt with Flask + gunicorn
- [x] app.py with REST API
- [x] GitHub Actions workflow
- [ ] Railway deployment (manual step required)
- [ ] Get live URL
- [ ] Test endpoints

---

## 🧪 Test After Deployment

```bash
# Health check
curl https://your-railway-url.railway.app/health

# Search people
curl "https://your-railway-url.railway.app/api/linkedin/search/people?keywords=software+engineer&limit=10"

# Search companies
curl "https://your-railway-url.railway.app/api/linkedin/search/companies?keywords=technology&limit=5"
```

---

## 📞 Support

If deployment fails:
1. Check Railway project logs
2. Verify requirements.txt
3. Ensure PORT environment variable is used
4. Contact: zhuzhushiwojia on GitHub
