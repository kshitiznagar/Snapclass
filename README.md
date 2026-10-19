# 🎓 SnapClass

**Making attendance faster using AI.**

SnapClass is a Streamlit web app that automates classroom attendance using **face recognition** and **voice recognition**. Teachers create subjects and share a **QR code / join link**; students scan it to enroll instantly, and attendance is verified with biometrics instead of roll calls.

---

## ✨ Features

### 👨‍🏫 Teacher
- Secure login (passwords hashed with `bcrypt`)
- Create and manage subjects/classes
- Generate a **QR code** and join link for each class
- Take attendance and review attendance records

### 👨‍🎓 Student
- Secure login and registration
- Join a class by scanning a QR code or opening a join link
- **Auto-enroll**: opening a link with `?join-code=XXXX` signs the student into the student flow and shows an enrollment dialog
- Register face and voice for biometric verification
- View enrolled classes and attendance

### 🤖 AI / Biometrics
| Capability | Libraries |
|---|---|
| Face recognition (embeddings + classifier) | `face_recognition_models`, `dlib-bin`, `scikit-learn` |
| Voice recognition (speaker embeddings) | `resemblyzer`, `librosa` |
| QR code generation | `segno` |
| Image preprocessing | `Pillow`, `numpy` |

---

## 🛠️ Tech Stack

- **Frontend / App framework:** [Streamlit](https://streamlit.io/)
- **Language:** Python 3.10+ (the app uses `match` statements)
- **Database / backend:** [Supabase](https://supabase.com/)
- **Auth security:** `bcrypt`
- **Data handling:** `numpy`, `pandas`

---

## 📁 Project Structure

```
Snapclass/
├── app.py                  # Entry point: page config, session state, routing
├── requirements.txt        # Python dependencies
├── .gitignore
└── src/
    ├── screens/
    │   ├── home_screen.py      # Landing page / login-type selection
    │   ├── student_screen.py   # Student dashboard & flows
    │   └── teacher_screen.py   # Teacher dashboard & flows
    └── components/
        └── dialog_auto_enroll.py   # Enrollment dialog for join-code links
```

> Add any other folders under `src/` (e.g. database, pipelines, utils) here.

### How routing works (`app.py`)

`app.py` stores `login_type` in `st.session_state` and renders:

| `login_type` | Screen |
|---|---|
| `None` | `home_screen()` |
| `'teacher'` | `teacher_screen()` |
| `'student'` | `student_screen()` |

If the URL contains `?join-code=<code>`, the app switches to the student flow and, once the student is logged in, opens `auto_enroll_dialog(join_code)`.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or newer
- A [Supabase](https://supabase.com/) project
- A webcam and microphone (for face and voice features)
- `git` (one dependency is installed straight from GitHub)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kshitiznagar/Snapclass.git
cd Snapclass

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Add your Supabase credentials. Use whichever method your code reads from — Streamlit secrets shown here:

`.streamlit/secrets.toml`
```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-anon-or-service-key"
```

> ⚠️ Never commit secrets. Make sure `.streamlit/secrets.toml` / `.env` are listed in `.gitignore`.

### Run the app

```bash
streamlit run app.py
```

Then open `http://localhost:8501`.

---

## 📦 Dependencies

From `requirements.txt`:

| Package | Purpose |
|---|---|
| `streamlit` | Web UI |
| `numpy`, `pandas` | Data handling |
| `scikit-learn` | Face classifier |
| `face_recognition_models` (from GitHub) | Pretrained face embedding models |
| `dlib-bin` | Prebuilt dlib (avoids compiling dlib) |
| `setuptools==80.9.0` | Required to install the GitHub-hosted models package |
| `supabase` | Database client |
| `bcrypt` | Password hashing |
| `segno` | QR code generation |
| `pillow` | Image processing |
| `librosa` | Audio processing |
| `resemblyzer` | Voice embeddings |

---

## 🔄 Usage Flow

1. **Teacher** logs in → creates a subject → shares the generated QR code / join link.
2. **Student** scans the QR code → lands on the app with `?join-code=...` → logs in → confirms enrollment.
3. **Attendance** is taken and verified using face and/or voice recognition.
4. **Teacher** reviews attendance records.

---

## 🧩 Troubleshooting

- **`dlib` fails to install:** this project uses `dlib-bin` to avoid compiling. Make sure you installed from `requirements.txt` and did not install plain `dlib`.
- **`face_recognition_models` install error:** ensure `git` is installed and `setuptools==80.9.0` is present.
- **Camera / microphone not working:** allow browser permissions for the site.

---

## 🗺️ Roadmap

- [ ] Attendance export (CSV / Excel)
- [ ] Analytics dashboard
- [ ] Deployment guide (Streamlit Community Cloud)

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push and open a Pull Request

---

## 📄 License

Add a license (e.g. MIT) and update this section.

---

## 👤 Author

**Kshitiz Nagar** — [@kshitiznagar](https://github.com/kshitiznagar)
