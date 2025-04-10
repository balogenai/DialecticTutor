from tutor_chain import create_tutor_chain

def run_chat():
    print("👋 Welcome to Dialectic Tutor! (Type 'exit' to quit)\n")
    topic = input("🎓 What topic do you want to learn about today? ")

    chain = create_tutor_chain()

    while True:
        student_input = input("\nYou: ")
        if student_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye! Keep questioning everything! 💡")
            break

        response = chain.run(topic=topic, student_input=student_input)
        print(f"\nTutor: {response}")

if __name__ == "__main__":
    run_chat()
