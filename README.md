# 📝 Todo App with Clean Architecture

A Python-based command-line Todo List Application implemented using the principles of Clean Architecture. This project is designed to be modular, testable, and scalable. It utilizes the Click library for the command-line interface and follows a clear separation of concerns with distinct application, infrastructure, and presentation layers.

📂 Project Structure
The project follows the Clean Architecture principles, separating business logic, data handling, and user interface into distinct layers:

<img width="711" alt="Screenshot 2025-01-30 at 13 20 42" src="https://github.com/user-attachments/assets/853e0860-d6b2-4658-95cc-fd1981b29f58" />

🚀 Features
Add Tasks: Add new tasks to the todo list.
List Tasks: View all current tasks in the todo list.
Delete Tasks: Remove a task by specifying its index.
Persistent Storage: Tasks are saved in a text file (tasks.txt) within the memory/ folder.

🛠️ Technologies Used
Python: Programming language.
Click: Library for building beautiful command-line interfaces.
Clean Architecture: Ensures modularity, scalability, and testability.

💻 Installation
1. Clone the Repository

<img width="715" alt="Screenshot 2025-01-30 at 13 21 31" src="https://github.com/user-attachments/assets/47783617-72af-4ea6-86c9-7d32f1f45030" />

2. Set Up a Virtual Environment (Optional but Recommended)

<img width="711" alt="Screenshot 2025-01-30 at 13 22 24" src="https://github.com/user-attachments/assets/98645268-5e8f-4970-94c6-2624979ed0e1" />

3. Install Dependencies

<img width="712" alt="Screenshot 2025-01-30 at 13 23 32" src="https://github.com/user-attachments/assets/16d51683-f281-476e-8bc4-51812285f45b" />

📖 Usage
Navigate to the project directory and run the main.py file using the following commands:

<img width="726" alt="Screenshot 2025-01-30 at 13 25 10" src="https://github.com/user-attachments/assets/c077e40b-8088-45eb-be03-4242f21339b7" />

🌟 Key Concepts of Clean Architecture
Separation of Concerns:

The Application Layer (todo_service.py) handles business rules.
The Infrastructure Layer (file_repository.py) handles data persistence.
The Presentation Layer (cli.py) handles user interaction.
Scalability: The application can easily switch storage solutions (e.g., a database) by updating the Infrastructure Layer without affecting the rest of the application.
Testability: Each layer is independent and can be tested separately.


🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

📧 Contact
For questions or suggestions, feel free to reach out:

GitHub: alishakerinouri

Email: alishakerinouri@gmail.com
