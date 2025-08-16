import subprocess
import webbrowser
import time
import os
import sys

def start_chatbot():
    print("🚀 Starting Kalyan Jewellers FAQ Chatbot...")
    print("💎 Please wait while the server starts...")
    
    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Activate virtual environment and start streamlit
    if os.name == 'nt':  # Windows
        activate_cmd = r"venv\Scripts\activate"
        cmd = f"{activate_cmd} && streamlit run app.py --server.headless true --server.port 8501"
    else:  # Linux/Mac
        activate_cmd = "source venv/bin/activate"
        cmd = f"{activate_cmd} && streamlit run app.py --server.headless true --server.port 8501"
    
    # Start the streamlit server
    process = subprocess.Popen(cmd, shell=True)
    
    # Wait a moment for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(5)
    
    # Open browser
    url = "http://localhost:8501"
    print(f"🌐 Opening browser at {url}")
    webbrowser.open(url)
    
    print("✅ Chatbot is now running!")
    print("📝 To stop the server, close this window or press Ctrl+C")
    print("🔗 Streamlit URL: http://localhost:8501")
    print("🌐 HTML Page URL: file://" + os.path.abspath("chatbot_page.html"))

    # Also open the HTML page
    html_path = os.path.abspath("chatbot_page.html")
    if os.path.exists(html_path):
        print("📄 Opening HTML wrapper page...")
        webbrowser.open("file://" + html_path)
    
    try:
        # Keep the script running
        process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping the chatbot server...")
        process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    start_chatbot()
