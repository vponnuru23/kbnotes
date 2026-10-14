
## 📄 README.md

```markdown
# 🔐 Firmware Component Security RAG (Vectorless)

This project is a **Streamlit dashboard** for firmware component security research.  
It uses a **vectorless RAG pipeline** with LangChain + Groq to query CVEs and explain risks.  
Instead of a vector database, CVEs are stored in structured JSON and retrieved directly.

---

## 🚀 Features
- Interactive **Streamlit UI** for querying firmware vulnerabilities.
- **Vectorless RAG**: retrieves CVEs directly from structured JSON data (no vector DB).
- **File upload support**: upload your own CVE dataset in JSON format.
- Falls back to a **default dataset** if no file is uploaded.
- Uses **Groq LLM** (`openai/gpt-oss-120b`) for generating security insights.
- Displays both the **LLM answer** and the **retrieved CVEs** for transparency.

---

## 📂 Project Structure
firmware-security-rag/
│
├── app.py                # Main Streamlit app
├── data/
│   └── default_cves.json # Default CVE dataset
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourname/firmware-security-rag.git
   cd firmware-security-rag
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Groq API key**
   - Create a `.env` file in the project root:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```
   - Or export it directly:
     ```bash
     export GROQ_API_KEY="your_api_key_here"
     ```

---

## 🖥️ Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Open in browser at `http://localhost:8501`.

---

## 📌 Example JSON Upload

You can upload a custom CVE dataset in JSON format.  
Example file (`my_cves.json`):

```json
[
  {
    "component": "TPM Firmware",
    "cve": "CVE-2026-1111",
    "description": "Key leakage vulnerability"
  },
  {
    "component": "UEFI Bootloader",
    "cve": "CVE-2026-2222",
    "description": "Secure boot bypass"
  }
]
```

When uploaded, the app will use this dataset instead of the default.

---

## 📊 Default Dataset

If no file is uploaded, the app uses `data/default_cves.json`:

```json
[
  {
    "component": "PCIe Controller",
    "cve": "CVE-2026-1234",
    "description": "Buffer overflow in DMA engine"
  },
  {
    "component": "BIOS Firmware",
    "cve": "CVE-2026-5678",
    "description": "Privilege escalation via SMM handler"
  },
  {
    "component": "Network Adapter Firmware",
    "cve": "CVE-2026-9012",
    "description": "Remote code execution in packet parser"
  }
]
```

---

## 🛡️ Notes
- This app is for **research and educational purposes**.
- Always validate CVE data against official sources (e.g., NVD, vendor advisories).
- For production, consider adding:
  - **Export feature** (download results as JSON/CSV).
  - **Authentication** for secure environments.
  - **Integration with live CVE feeds** (NVD API, vendor advisories).

---

## 📌 Roadmap
- [ ] Add export/download option for results.
- [ ] Integrate live CVE feeds via API.
- [ ] Support multiple datasets (merge uploaded + default).
- [ ] Add visualization (severity charts, timelines).
```