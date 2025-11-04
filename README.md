# 🐍 Guess Number - FastAPI + Docker

A small demo project using **FastAPI** and **Docker** to run a minimal API.

---

## 🚀 How to run the project

### 1️⃣ Build the image

```bash
make build
```

### 2️⃣ Start the container

```bash
make up
```

The app will be available at [http://localhost:8000](http://localhost:8000)

---

## 🔁 Development with hot reload

The container runs with:

```dockerfile
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "80"]
```

This enables **automatic server reload** when you modify the code (you’ll still need to manually refresh your browser).

---

## 🧩 Endpoints

| Method | Path | Description              |
| :----- | :--- | :----------------------- |
| GET    | `/`  | Returns a basic greeting |

Interactive API docs are available at
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧹 Clean up containers

```bash
make clean
```

---

## 📁 Project structure

```
guess_number/
├── main.py
├── Dockerfile
├── requirements.txt
├── Makefile
└── .gitignore
```
