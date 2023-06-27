using System;
using System.Data.Entity;
using System.Linq;
using System.Collections.Generic;

namespace Dawaj
{
    public class DataModel : DbContext
    {
        // Your context has been configured to use a 'DataModel' connection string from your application's 
        // configuration file (App.config or Web.config). By default, this connection string targets the 
        // 'Dawaj.DataModel' database on your LocalDb instance. 
        // 
        // If you wish to target a different database and/or database provider, modify the 'DataModel' 
        // connection string in the application configuration file.
        public DataModel()
            : base("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=E:\\data.mdf;Integrated Security=True;Connect Timeout=30")
        {
        }

        // Add a DbSet for each entity type that you want to include in your model. For more information 
        // on configuring and using a Code First model, see http://go.microsoft.com/fwlink/?LinkId=390109.

        public virtual DbSet<User> Users { get; set; }
        public virtual DbSet<Artiffact> Artifacts { get; set; }
        public virtual DbSet<Atribute> Atributes { get; set; }
        public virtual DbSet<AtributeDefinition> AtributesDefinitions { get; set; }
        public virtual DbSet<Class> Classes { get; set; }
        public virtual DbSet<Right> Rights { get; set; }
        public virtual DbSet<Role> Roles { get; set; }
    }

    public class Right
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string ClassesAllowedToEdit { get; set; }
        public string ArtifactsAllowedToEdit { get; set; }
        public string UsersAllowedToEdit { get; set; }
    }

    public class Role
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public List<Right> Rights { get; set; } //= new List<Right>();
    }

    public class User
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Password { get; set; }
        public Role Role { get; set; }
    }

    public class Atribute
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Value { get; set; }
    }

    public class Artiffact
    {
        public int Id { get; set; }
        public string Class { get; set; }
        public string Name { get; set; }
        public int UserId { get; set; }
        public int mainAtribute { get; set; }
        public List<Atribute> Atributes { get; set; } //= new List<Atribute>();
    }

    public class AtributeDefinition
    {
        public string Name { get; set; }
        public int Id { get; set; }
    }

    public class Class
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int UserId { get; set; }
        public string mainAtribute { get; set; }
        public List<AtributeDefinition> Atributes { get; set; } //= new List<AtributeDefinition>();
    }
}