# Complete Deployment Steps for SarcasmDetect-AI

## 🎯 **Deployment Plan Overview**
- **Frontend**: Vercel (React app)
- **Backend**: Railway (FastAPI server)
- **Total Time**: 15-20 minutes
- **Cost**: FREE on both platforms

---

## 🔧 **Step 1: Deploy Backend to Railway (10 minutes)**

### 1.1 Login to Railway
```powershell
railway login
```
*This will open a browser window - sign up/login with GitHub*

### 1.2 Initialize Railway Project
```powershell
cd backend
railway init
```
*Choose: "Create new project" and give it a name like "sarcasmdetect-backend"*

### 1.3 Set Environment Variables
```powershell
# Add your Gemini API key
railway variables set GEMINI_API_KEY=your_actual_gemini_api_key_here

# Add your OCR.space API key  
railway variables set OCR_SPACE_API_KEY=your_actual_ocr_space_api_key_here

# Enable OCR feature
railway variables set ENABLE_OCR=true

# Disable ASR (Audio Speech Recognition) for now
railway variables set ENABLE_ASR=false
```

### 1.4 Deploy Backend
```powershell
railway up
```
*Railway will automatically detect Python, install requirements.txt, and deploy*

### 1.5 Get Backend URL
```powershell
railway status
```
*Copy the generated URL (looks like: https://your-app-name.up.railway.app)*

---

## 🌐 **Step 2: Deploy Frontend to Vercel (5-10 minutes)**

### 2.1 Update Frontend with Backend URL
*Replace `BACKEND_URL_PLACEHOLDER` in the config file:*

```powershell
cd ../frontend/src
# Edit config.js and replace 'BACKEND_URL_PLACEHOLDER' with your Railway URL
```

### 2.2 Login to Vercel
```powershell
vercel login
```
*This will open a browser - sign up/login with GitHub*

### 2.3 Deploy Frontend
```powershell
cd .. # Go to frontend root
vercel --prod
```
*Follow the prompts:*
- Link to existing project? **N**
- Project name: **sarcasmdetect-ai** (or your choice)
- Directory: **./frontend** or just press Enter
- Override settings? **N**

### 2.4 Get Frontend URL
*Vercel will show your live URL: https://your-app-name.vercel.app*

---

## 🎯 **Ready-to-Copy Commands**

### Backend Deployment (Railway):
```powershell
# Navigate to backend
cd backend

# Login to Railway
railway login

# Initialize project
railway init

# Set environment variables (replace with your actual keys)
railway variables set GEMINI_API_KEY=your_actual_gemini_api_key_here
railway variables set OCR_SPACE_API_KEY=your_actual_ocr_space_api_key_here
railway variables set ENABLE_OCR=true
railway variables set ENABLE_ASR=false

# Deploy
railway up

# Get the URL
railway status
```

### Frontend Deployment (Vercel):
```powershell
# Navigate to frontend
cd ../frontend

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

---

## 📋 **What You Need Before Starting**

### Required API Keys:
1. **Gemini API Key**: 
   - Get from: https://aistudio.google.com/app/apikey
   - Free tier: 15 requests/minute

2. **OCR.space API Key**:
   - Get from: https://ocr.space/ocrapi
   - Free tier: 25,000 requests/month

### Accounts to Create:
1. **Railway Account**: https://railway.app (login with GitHub)
2. **Vercel Account**: https://vercel.com (login with GitHub)

---

## ⏱️ **Timeline**
- **Prep (API keys)**: 5 minutes
- **Backend deployment**: 8-10 minutes  
- **Frontend deployment**: 5 minutes
- **Testing**: 2-3 minutes
- **Total**: 20-25 minutes

---

## 🎉 **Final Result**
You'll have:
- ✅ **Live backend API**: https://your-backend.up.railway.app
- ✅ **Live frontend**: https://your-frontend.vercel.app  
- ✅ **Professional demo URL** for presentations
- ✅ **Free hosting** with excellent uptime

Ready to start? I'll help you with any issues along the way! 🚀