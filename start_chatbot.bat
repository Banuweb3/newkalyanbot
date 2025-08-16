@echo off
echo Starting Kalyan Jewellers FAQ Chatbot...
echo.
echo The chatbot will open in your default browser automatically.
echo To stop the server, close this window or press Ctrl+C
echo.

cd /d "%~dp0"
call venv\Scripts\activate
streamlit run app.py --server.headless true --server.port 8501

pause
