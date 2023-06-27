using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Security.Cryptography;

namespace Dawaj
{
    public class UserManager
    {
        public static User loggedIn = new User { Id = 1, Name = "Admin" };
        public UserManager()
        {

        }

        public void createUser(string n, string p)
        {
            using(var context = new DataModel())
            {
                var user = new User()
                {
                    Name = n,
                    Password = passwordEncode(p),
                    Role = context.Roles.Include("Rights").Where(x => x.Id == 11).FirstOrDefault()
            };
                context.Users.Add(user);
                context.SaveChanges();
            }
        }

        public string passwordEncode(string pswd)
        {
            using (var sha256 = SHA256.Create())
            { 
                var hashedBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(pswd));
                var hash = BitConverter.ToString(hashedBytes).Replace("-", "").ToLower();
                return hash;
            }
        }

        public bool checkPassword(string name, string password)
        {
            password = passwordEncode(password);
            using (var context = new DataModel())
            {
                var users = context.Users.ToList();
                foreach (var user in users)
                {
                    if (user.Password == password && user.Name == name)
                    {
                        loggedIn = user;
                        return true;
                    }
                }
                return false;
            }
        }

        public List<User> getUsers()
        {
            using(var context = new DataModel())
            {
                return context.Users.Include("Role").ToList();
            }
        }

        public bool doesUserNameExists(string name)
        {
            using(var context = new DataModel())
            {
                List<User> list = context.Users.Where(x => x.Name == name).ToList();
                if(list.Count == 0)
                    return true;
            }
            return false;
        }

        public void changePassword(string newPassword, int userId)
        {
            using (var context = new DataModel())
            {
                User user = context.Users.Where(x => x.Id == userId).First();
                user.Password = passwordEncode(newPassword);
                context.SaveChanges();
            }
        }

        public User getUserById(int id)
        {
            return getUsers().FirstOrDefault(x => x.Id == id);
        }

        public User getUserByName(string name)
        {
            return getUsers().FirstOrDefault(x => x.Name == name);
        }
    }
}
