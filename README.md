## 🚀 Installation

1. Clone the repository.

bash
git clone https://github.com/Varshitha-D1/JobNovaAI.git
cd JobNovaAI

2. Install the required dependencies.

bash
pip install -r requirements.txt


3. Install **Ollama** from **https://ollama.com**.

4. Download the Gemma 3 model.

bash
ollama pull gemma3:1b


---

## ▶️ Running the Project

1. Start the Ollama server.

bash
ollama serve

2. Run the FastAPI backend.

bash
python -m uvicorn backend.main:app --reload

3. Open `index.html` using **Live Server** in Visual Studio Code.

4. Open the application in your browser and start using **JobNova AI**.
