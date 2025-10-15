import pandas as pd
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database_name"
)

# Load data
query = "SELECT * FROM students_mental_health;"
df = pd.read_sql(query, conn)

# Visualize
sns.countplot(data=df, x='Gender')
plt.title('Number of Students by Gender')
plt.show()
