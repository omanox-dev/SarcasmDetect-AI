# Railway Backend Deployment Configuration

# Railway will automatically detect this is a Python project
# and use the requirements.txt file

# Environment Variables needed for Railway:
# GEMINI_API_KEY=your_actual_gemini_key
# OCR_SPACE_API_KEY=your_actual_ocr_key  
# ENABLE_OCR=true
# ENABLE_ASR=false

# Railway will run this command automatically:
# uvicorn app:app --host 0.0.0.0 --port $PORT

echo "Backend will be deployed to Railway"
echo "Frontend will connect to Railway backend URL"