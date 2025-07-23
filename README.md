#  MeAgent — Personal AI Agentic Chatbot

A lightweight, no-framework Agentic AI chatbot that acts as a summarizer and representative of **Priyanka Rose Varghese** (inspired from The Complete Agentic AI Engineering Course (2025) by Ed Donner) (Notes here: https://www.notion.so/Week-01-23371137ec068176a32bdf890d259d47?source=copy_link). It uses OpenAI's tool calling to:
- Chat naturally based on your resume and LinkedIn content.
- Record user interest (email, name).
- Record unanswered questions via push notifications.

Built with:
- `openai`
- `pypdf` for PDF parsing
-  `pushover` for notifications
- 🖥 `gradio` for interactive web UI

---

## Features

-  **LLM-powered personalized chatbot** acting on behalf of you (based on summary + resume)
-  **Tool-calling** for structured agent actions:
  - `record_user_details(email, name, notes)`
  - `record_unknown_question(question)`
-  **Push notifications** via Pushover for lead capture or unanswered queries
-  Loads your:
  - `me/summary.txt` – your short summary
  - `me/linkedin.pdf` – your resume/profile PDF



