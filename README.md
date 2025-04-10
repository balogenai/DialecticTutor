# Dialectic Tutor 🧠

Dialectic Tutor is an interactive AI-powered educational tool designed to help children (ages 8–13) learn through guided conversations. Using the Socratic method, the tutor encourages reflection, asks thoughtful questions, and helps students arrive at answers on their own.

## Features

- **Socratic Method**: Encourages learning through guided questions and reflection.
- **Streamlit Interface**: A user-friendly web app for interactive conversations.
- **Customizable Prompts**: Easily modify the tutor's behavior and tone via prompt templates.
- **Memory Tracking**: Maintains conversation history for context-aware responses.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- [OpenAI API Key](https://platform.openai.com/signup/)
- Required Python libraries (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dialectic-tutor.git
   cd dialectic-tutor
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv_dialectic_tutor
   source venv_dialectic_tutor/bin/activate  # On Windows: venv_dialectic_tutor\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your-openai-api-key
   ```

### Running the App

To launch the Streamlit app, run:
```bash
streamlit run streamlit_app.py
```

The app will open in your default web browser. You can interact with the tutor by typing your questions or topics into the chat input.

### Running in the Terminal

For a terminal-based experience, run:
```bash
python main.py
```

## Project Structure

```
.
├── main.py               # Terminal-based chat interface
├── streamlit_app.py      # Streamlit web app
├── tutor_chain.py        # Chain setup for the AI tutor
├── prompts.py            # Prompt templates for the tutor
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (e.g., OpenAI API key)
├── conversation_log.txt  # Example conversation log
└── venv_dialectic_tutor/ # Virtual environment (optional)
```

## Customization

- **Prompts**: Modify the prompts in `prompts.py` to adjust the tutor's behavior.
- **LLM Settings**: Update the `create_tutor_chain` function in `tutor_chain.py` to change the language model or its parameters.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Built using [LangChain](https://github.com/hwchase17/langchain) and [Streamlit](https://streamlit.io/).
- Inspired by the Socratic method of teaching.

---

Happy learning! 🎓
