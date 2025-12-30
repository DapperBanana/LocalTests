// Since the request is for C# code that performs CRUD operations on a SQLite database,
// here's an example implementation using the System.Data.SQLite library:

using System;
using System.Data.SQLite;

class Program
{
    static string connectionString = "Data Source=example.db;Version=3;";

    static void Main()
    {
        // Create database and table
        CreateDatabaseAndTable();

        // Insert data
        InsertRecord("John Doe", 30);
        InsertRecord("Jane Smith", 25);

        // Read data
        ReadRecords();

        // Update data
        UpdateRecord(1, "John Updated", 31);

        // Read data after update
        ReadRecords();

        // Delete data
        DeleteRecord(2);

        // Read data after delete
        ReadRecords();
    }

    static void CreateDatabaseAndTable()
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();
            string createTableQuery = @"
                CREATE TABLE IF NOT EXISTS Persons (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Age INTEGER NOT NULL
                )";
            using (var command = new SQLiteCommand(createTableQuery, connection))
            {
                command.ExecuteNonQuery();
            }
        }
    }

    static void InsertRecord(string name, int age)
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();
            string insertQuery = "INSERT INTO Persons (Name, Age) VALUES (@Name, @Age)";
            using (var command = new SQLiteCommand(insertQuery, connection))
            {
                command.Parameters.AddWithValue("@Name", name);
                command.Parameters.AddWithValue("@Age", age);
                command.ExecuteNonQuery();
            }
        }
    }

    static void ReadRecords()
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();
            string selectQuery = "SELECT Id, Name, Age FROM Persons";
            using (var command = new SQLiteCommand(selectQuery, connection))
            using (var reader = command.ExecuteReader())
            {
                Console.WriteLine("Current Records:");
                while (reader.Read())
                {
                    Console.WriteLine($"Id: {reader["Id"]}, Name: {reader["Name"]}, Age: {reader["Age"]}");
                }
                Console.WriteLine();
            }
        }
    }

    static void UpdateRecord(int id, string newName, int newAge)
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();
            string updateQuery = "UPDATE Persons SET Name = @Name, Age = @Age WHERE Id = @Id";
            using (var command = new SQLiteCommand(updateQuery, connection))
            {
                command.Parameters.AddWithValue("@Name", newName);
                command.Parameters.AddWithValue("@Age", newAge);
                command.Parameters.AddWithValue("@Id", id);
                command.ExecuteNonQuery();
            }
        }
    }

    static void DeleteRecord(int id)
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();
            string deleteQuery = "DELETE FROM Persons WHERE Id = @Id";
            using (var command = new SQLiteCommand(deleteQuery, connection))
            {
                command.Parameters.AddWithValue("@Id", id);
                command.ExecuteNonQuery();
            }
        }
    }
}