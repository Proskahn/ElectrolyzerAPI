# ElectrolyzerAPI

**ElectrolyzerAPI** is a digital twin backend for modeling, simulating, and evaluating electrolyzer systems. It provides a structured way to compile component selections (e.g., membranes) and evaluate operational conditions (e.g., optimal temperature). Designed for scalability and scientific extensibility — ideal for research and industrial applications.

---

## 🚀 Features

- 🔧 **Compile tools**: Select key components like membranes (e.g., Nafion 115/117)
- 📊 **Evaluate tools**: Compute optimal operating temperatures based on inputs
- 💡 Built with **FastAPI** + **Jinja2** for high-performance APIs and easy templating
- 💻 Responsive Web Interface using **Tailwind CSS**
- ⚙️ Structured with scalability in mind for scientific computing

---



## 🛠️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ElectrolyzerAPI.git
cd ElectrolyzerAPI
```

### 2. Install Dependencies

```bash
poetry install
```

> Make sure [Poetry](https://python-poetry.org/) is installed (`pip install poetry`)

### 3. Run the API Server

```bash
poetry run uvicorn electrolyzer.main:app
```


---

## ✅ Usage

- Click **Compile** to select membranes (currently supports: Nafion 115, 117, 212).
- Click **Evaluate** to input current density and compute recommended temperature.
- Backend logic is structured in `api/` for future scientific model expansions.

---

## 🧪 Running Tests

```bash
poetry run pytest
```

*(Test files live in `tests/`)*

---

## 📌 TODO

- [ ] Connect frontend to real backend computation
- [ ] Expand compile options (electrodes, catalysts, etc.)
- [ ] Add authentication (if needed for deployment)
- [ ] Containerize with Docker
- [ ] Deploy to cloud (e.g., GCP, AWS, Railway)

---

## 📄 License

MIT License

---

## 👨‍🔬 Author

**zkang** – PhD Candidate at University Leiden
