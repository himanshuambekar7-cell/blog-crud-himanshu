
 Django Blog CRUD Application



A clean and functional \*\*Django Blog Application\*\* that lets users \*\*Create, Read, Update, and Delete (CRUD)\*\* blog posts.

Built with Django and Bootstrap-based styling — perfect for learning and showcasing Django fundamentals.



\## 🌐 Live Deployment

Link pending — (if you deploy later, you can update here)



🚀 Features



✅ Create new blog posts

✅ View all posts on the homepage

✅ Update or edit existing blogs

✅ Delete unwanted blogs

✅ Responsive and minimal UI design



🛠️ Tech Stack



| Layer        | Technology         |

|--------------|--------------------|

| \*\*Backend\*\*  | Django (Python)    |

| \*\*Frontend\*\* | HTML, CSS (Bootstrap) |

| \*\*Database\*\* | SQLite (default Django DB) |

| \*\*Environment\*\* | Virtualenv / venv |



📂 Project Structure



blog\_project/

│

├── blog/

│ ├── migrations/

│ ├── templates/

│ │ └── blog/

│ │ ├── base.html

│ │ ├── home.html

│ │ ├── post\_list.html

│ │ ├── post\_detail.html

│ │ ├── post\_form.html

│ │ ├── post\_confirm\_delete.html

│ ├── forms.py

│ ├── models.py

│ ├── urls.py

│ └── views.py

│

├── blog\_project/

│ ├── settings.py

│ ├── urls.py

│ └── wsgi.py

│

├── static/

│ └── css/

│ └── style.css

│

├── db.sqlite3

├── manage.py

├── README.md



arduino

Copy code



⚙️ Installation \& Setup



Follow these steps to run the project locally 👇



1️⃣ Clone the Repository

git clone https://github.com/himanshuambekar7-cell/blog-crud-himanshu.git

cd blog-crud-himanshu



mathematica

Copy code



2️⃣ Create \& Activate a Virtual Environment

python -m venv env



Windows

env\\Scripts\\activate



macOS/Linux

source env/bin/activate



mathematica

Copy code



3️⃣ Install Dependencies

pip install django



mathematica

Copy code



4️⃣ Run Migrations

python manage.py makemigrations

python manage.py migrate



pgsql

Copy code



5️⃣ Start the Development Server

python manage.py runserver



pgsql

Copy code



6️⃣ Open in Browser

👉 Visit http://127.0.0.1:8000/ to access your blog.



🎨 UI Overview

\- \*\*Header\*\*: Displays “My Blog” and login/signup buttons

\- \*\*Homepage\*\*: Lists all created blog posts with title and author

\- \*\*Create Page\*\*: Form for adding new posts

\- \*\*Update Page\*\*: Edit existing posts

\- \*\*Delete Option\*\*: Remove posts with confirmation

\- \*\*Login/Signup\*\*: User authentication



👨‍💻 Author

Himanshu Ambekar

📧 himanshuambekar7@gmail.com

🔗 https://github.com/himanshuambekar7-cell



🌟 Support

If you like this project, consider giving it a ⭐ on GitHub!

It helps others discover it and motivates further development.
