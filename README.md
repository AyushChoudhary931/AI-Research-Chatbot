# 🔍 AI Research Agent

A modular multi-agent AI research system built using Streamlit, LangGraph, OpenAI, Tavily Search, SQLite, and LangSmith.

This project performs autonomous web research using multiple AI agents working together in a structured workflow:

* **Researcher Agent** → Collects live web information
* **Analyst Agent** → Extracts key insights and themes
* **Critic Agent** → Reviews findings for bias and missing context
* **Writer Agent** → Generates a final polished research report

The system supports persistent research sessions, observability with LangSmith, and a modern modular Streamlit UI.

---

# ✨ Features

## 🧠 Multi-Agent Research Pipeline

Built with LangGraph state-based workflows.

### Agents

| Agent      | Responsibility                           |
| ---------- | ---------------------------------------- |
| Researcher | Searches the web using Tavily            |
| Analyst    | Extracts facts, statistics, and themes   |
| Critic     | Reviews accuracy, bias, and completeness |
| Writer     | Generates the final report               |

---

## 💾 Persistent Memory

* SQLite-backed research sessions
* Resume previous research threads
* Multi-session sidebar similar to ChatGPT
* Session status tracking

---

## 📊 LangSmith Observability

* Full tracing for all agent executions
* Prompt debugging
* Chain inspection
* Workflow monitoring

---

## 🎨 Modern Streamlit UI

* Classic dark theme
* Modular UI architecture
* Session management sidebar
* Report downloads
* Responsive layout

---

# 🏗️ Architecture

```text
User Query
    ↓
Researcher Agent
    ↓
Analyst Agent
    ↓
Critic Agent
    ↓
Writer Agent
    ↓
Final Research Report
```

The workflow is managed using a LangGraph state graph.

---

# 📁 Project Structure

```text
research-agent/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
│
├── agents/
│   ├── researcher.py
│   ├── analyst.py
│   ├── critic.py
│   └── writer.py
│
├── graph/
│   ├── pipeline.py
│   └── state.py
│
├── tools/
│   └── tavily_search.py
│
├── memory/
│   └── database.py
│
├── monitoring/
│   └── langsmith.py
│
├── config/
│   └── settings.py
│
├── ui/
│   ├── styles.py
│   ├── sidebar.py
│   ├── home.py
│   ├── session_view.py
│   └── footer.py
│
└── research_agent.db
```

---

# ⚙️ Tech Stack

| Technology | Usage                              |
| ---------- | ---------------------------------- |
| Streamlit  | Frontend UI                        |
| LangGraph  | Multi-agent workflow orchestration |
| OpenAI     | LLM inference                      |
| Tavily     | Web search                         |
| SQLite     | Persistent storage                 |
| LangSmith  | Tracing & observability            |
| Python     | Backend logic                      |

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/AyushChoudhary931/research-agent.git
cd research-agent
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=AI-Research-Agent
MODEL_NAME=gpt-4.1-mini
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧪 Example Workflow

## Input

```text
The impact of AI on software engineering jobs
```

## Pipeline

1. Tavily fetches live web sources
2. Analyst extracts insights
3. Critic evaluates quality and bias
4. Writer generates a final report

## Output

* Executive Summary
* Background & Context
* Key Findings
* Multiple Perspectives
* Conclusion

---

# 📥 Report Export

Users can:

* Download reports as Markdown
* Revisit previous sessions
* Resume interrupted research

---

# 🔭 Future Improvements

Potential future additions:

* PDF export
* Real-time streaming responses
* Authentication system
* Vector database memory
* RAG integration
* Multi-model support
* Research citations
* Web scraping support
* Async execution
* Docker deployment

---

# 📸 UI Highlights

## Features

* ChatGPT-style sidebar
* Dark classic theme
* Persistent sessions
* Clean report rendering
* Responsive layout

---

# 🧠 Learning Objectives

This project demonstrates:

* Multi-agent AI systems
* LangGraph orchestration
* LLM pipelines
* AI observability
* Modular Streamlit architecture
* Stateful workflows
* Persistent memory systems

---

# 👨‍💻 Author

## Ayush Choudhary

Machine Learning Engineer & AI Developer

GitHub:

[https://github.com/AyushChoudhary931](https://github.com/AyushChoudhary931)

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful:

* Star the repository
* Fork the project
* Contribute improvements
* Share feedback

---

# 🔥 Final Note

This project is designed as a production-style AI research assistant using modular architecture, agent-based reasoning, persistent storage, and observability tooling.

It is suitable for:

* AI engineering portfolios
* LangGraph learning
* Research automation
* LLM workflow experimentation
* Resume projects
* AI SaaS foundations
