# Snake Engine — TDD & Decoupled Architecture

A Python-based implementation of the classic Snake game, built with a focus on **Software Engineering best practices**, **Test-Driven Development (TDD)**, and **Separation of Concerns (SoC)**.

---

## 🏗️ Architectural Design
The project is architected with a strict decoupling between game logic and the graphical interface, making the core engine entirely agnostic of the rendering library:

* **Domain Layer (`logic/`)**: Handles the "business rules" of the game, including snake coordinate math, food generation, and collision detection logic.
* **Interface Layer (`UI/`)**: Powered by **Pygame**, this layer is responsible for rendering the game state and capturing user input.
* **Configuration Layer (`game_config.py`)**: Centralizes all constants (board size, speed, colors), allowing for system-wide adjustments without modifying core logic.
* **Entry Point (`main.py`)**: Orchestrates the initialization of the UI and manages the primary execution loop.

---

## 🧪 Quality Assurance (TDD)
Reliability is ensured through an extensive suite of automated tests using **Pytest**. The engine was developed following TDD principles to ensure high code quality and maintainability.

* **Unit Testing**: Validates atomic mechanics such as movement vectors, 180-degree turn restrictions, and tail growth.
* **Integration Testing**: Verifies the interaction between the snake and the game environment, focusing on wall collisions and scoring systems.
* **UI Mocking**: Utilizes `unittest.mock` to simulate real-time keyboard events in `test_ui.py`, allowing for automated validation of the user interface without manual gameplay.

---

## 🚀 Getting Started

### 1. Environment Setup
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Execute the Game
```bash
python main.py
```

### 4. Run Test Suite
```bash
pytest
```
