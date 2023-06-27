using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dawaj
{
    public class RoleManager
    {
        ClassManager classManager = new ClassManager(UserManager.loggedIn.Id);
        ArtiffactManager artiffactManager = new ArtiffactManager(UserManager.loggedIn.Id);
        UserManager userManager = new UserManager();
        public RoleManager()
        {

        }

        public List<string> getUsersToEditString(int userId)
        {
            using (var context = new DataModel())
            {
                var rights = context.Users.Include("Role.Rights").Where(x => x.Id == userId).Select(x => x.Role.Rights).FirstOrDefault();
                List<string> list = new List<string>();
                foreach(var right in rights)
                {
                    if(right.UsersAllowedToEdit == null)
                        return list;
                    var temp = right.UsersAllowedToEdit.Split(' ').ToList();
                    foreach(var x in temp)
                    {
                        if (!list.Contains(x))
                        {
                            list.Add(x);
                        }
                    }
                }
                return list;
            }
        }

        public List<string> getClassToEditString(int userId)
        {
            using (var context = new DataModel())
            {
                var rights = context.Users.Include("Role.Rights").Where(x => x.Id == userId).Select(x => x.Role.Rights).FirstOrDefault();
                List<string> list = new List<string>();
                foreach (var right in rights)
                {
                    var temp = right.ClassesAllowedToEdit.Split(' ').ToList();
                    foreach (var x in temp)
                    {
                        if (!list.Contains(x))
                        {
                            list.Add(x);
                        }
                    }
                }
                return list;
            }
        }

        public List<string> getArtifactsToEditString(int userId)
        {
            using (var context = new DataModel())
            {
                var rights = context.Users.Include("Role.Rights").Where(x => x.Id == userId).Select(x => x.Role.Rights).FirstOrDefault();
                List<string> list = new List<string>();
                foreach (var right in rights)
                {
                    var temp = right.ArtifactsAllowedToEdit.Split(' ').ToList();
                    foreach (var x in temp)
                    {
                        if (!list.Contains(x))
                        {
                            list.Add(x);
                        }
                    }
                }
                return list;
            }
        }

        public bool canEditArtifact(int artId)
        {
            if (getArtifactsToEditString(UserManager.loggedIn.Id).Contains("All"))
                return true;
            if (getArtifactsToEditString(UserManager.loggedIn.Id).Contains("Default"))
            {
                if(artiffactManager.getArtiffactById(artId).UserId == UserManager.loggedIn.Id)
                    return true;
                else
                    return false;
            }
            if (getArtifactsToEditString(UserManager.loggedIn.Id).Contains(artiffactManager.getArtiffactById(artId).Name))
            {
                return true;
            }
            return false;
        }

        public bool canEditClass(int artId)
        {
            if (getClassToEditString(UserManager.loggedIn.Id).Contains("All"))
                return true;
            if (getClassToEditString(UserManager.loggedIn.Id).Contains("Default"))
            {
                if (classManager.getClassById(artId).UserId == UserManager.loggedIn.Id)
                    return true;
                else
                    return false;
            }
            if (getClassToEditString(UserManager.loggedIn.Id).Contains(classManager.getClassById(artId).Name))
            {
                return true;
            }
            return false;
        }

        public List<string> getRolesString()
        {
            using (var context = new DataModel())
            {
                return context.Roles.Select(r => r.Name).ToList();
            }
        }

        public List<string> getUsersList(int userId)
        {
            if (getUsersToEditString(userId).Contains("All")){
                return userManager.getUsers().Select(r => r.Name).ToList();
            }
            if (getUsersToEditString(userId).Contains("Default"))
            {
                return userManager.getUsers().Where(x => x.Id == userId).Select(r => r.Name).ToList();
            }
            return getUsersToEditString(userId);
        }

        public List<string> getStringRights()
        {
            using (var context = new DataModel())
            {
                return context.Rights.Select(x => x.Name).ToList();
            }
        }

        public string toOneString(List<string> list)
        {
            string ret = "";
            foreach(var item in list)
            {
                ret += item + " ";
            }
            if (ret == "")
                return ret;
            return ret.Substring(0, ret.Length - 1);
        }

        public void newRight(string name, List<string> classes, List<string> artifacts)
        {
            using (var context = new DataModel())
            {
                Right right = new Right
                {
                    Name = name,
                    ClassesAllowedToEdit = toOneString(classes),
                    ArtifactsAllowedToEdit = toOneString(artifacts),
                    UsersAllowedToEdit = "Default"
                };
                context.Rights.Add(right);
                context.SaveChanges();
            }
        }

        public List<string> getRightClasses(string name)
        {
            using(var context = new DataModel())
            {
                return context.Rights.Where(x => x.Name == name).Select(z => z.ClassesAllowedToEdit).FirstOrDefault().Split(' ').ToList();
            }
        }

        public List<string> getRightArtifacts(string name)
        {
            using (var context = new DataModel())
            {
                return context.Rights.Where(x => x.Name == name).Select(z => z.ArtifactsAllowedToEdit).FirstOrDefault().Split(' ').ToList();
            }
        }

        public void changeRole(string name, string role)
        {
            using(var context = new DataModel())
            {
                var user = context.Users.Where(x => x.Name == name).FirstOrDefault();
                user.Role = context.Roles.Where(x => x.Name == role).FirstOrDefault();
                context.SaveChanges();
            }
        }

        public void createRole(string name, List<string> rights)
        {
            List<Right> rightsList = new List<Right>();
            using(var context = new DataModel())
            {
                foreach (var right in rights)
                {
                    rightsList.Add(context.Rights.Where(x => x.Name == right).FirstOrDefault());
                }

                Role role = new Role
                {
                    Name = name,
                    Rights = rightsList
                };
                context.Roles.Add(role);
                context.SaveChanges();
            }
        }
    }
}
