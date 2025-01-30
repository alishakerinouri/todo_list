# 📝 Todo App with Clean Architecture

A Python-based command-line Todo List Application implemented using the principles of Clean Architecture. This project is designed to be modular, testable, and scalable. It utilizes the Click library for the command-line interface and follows a clear separation of concerns with distinct application, infrastructure, and presentation layers.

📂 Project Structure
The project follows the Clean Architecture principles, separating business logic, data handling, and user interface into distinct layers:

<img width="713" alt="Screenshot 2025-01-30 at 13 03 09" src="https://github.com/user-attachments/assets/e60e15cb-36dd-4152-9475-aa1892ac54cd" />

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

<img width="711" alt="Screenshot 2025-01-30 at 13 03 57" src="https://github.com/user-attachments/assets/59b65679-c1e7-4969-b8f0-cff42ca4f0cc" />

2. Set Up a Virtual Environment (Optional but Recommended)

<img width="713" alt="Screenshot 2025-01-30 at 13 04 29" src="https://github.com/user-attachments/assets/8bccc28e-ea65-4aa0-8871-f65eb4d4c99a" />

3. Install Dependencies

<img width="712" alt="Screenshot 2025-01-30 at 13 04 54" src="https://github.com/user-attachments/assets/88054867-d444-4b69-9ed5-18b6bb627283" />


📖 Usage
Navigate to the project directory and run the main.py file using the following commands:


<img width="729" alt="Screenshot 2025-01-30 at 13 06 25" src="https://github.com/user-attachments/assets/59abd2c0-bbb4-464d-b99e-e809fe14c365" />


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
