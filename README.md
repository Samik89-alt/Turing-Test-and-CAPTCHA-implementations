# AI Concepts Implementation

This repository contains small implementations related to **Artificial Intelligence concepts**, including a **Turing Test simulation game** and a **CAPTCHA verification system**.

---

# 1️⃣ Turing Test Game

This program simulates the **Turing Test** proposed by Alan Turing.

In the game, the user interacts with a system that may respond either as:

* **A Human**
* **A Machine (AI)**

The goal of the user is to **guess whether the response came from a human or an AI**.

The AI responses are generated dynamically using an **LLM API**.

## Features

* Random human / AI role assignment
* Score tracking
* Timer for each round
* Interactive terminal gameplay

## Installation

```bash
pip install groq
```

## Running the Program

```bash
python turingTest-imple.py
```

---

# 2️⃣ CAPTCHA Implementation

This project implements a **Text Distortion CAPTCHA system** used to verify whether the user is human.

The system generates a random CAPTCHA image that the user must correctly enter to proceed.

After successful verification, the program redirects the user to **Google**.

## Features

* Random string generation
* Distorted CAPTCHA image generation
* User input validation
* Redirect to Google after successful verification

## Installation

```bash
pip install captcha pillow
```

## Running the Program

```bash
python captcha-imple.py
```

---

# Project Structure

```
AI-Concepts/
│
├── turingTest-imple.py
├── captcha-imple.py
└── README.md
```

---

# Technologies Used

* Python
* Groq API (LLM responses)
* CAPTCHA library
* Pillow (image processing)

---

# Author

Samik (SE24UCSE184)
