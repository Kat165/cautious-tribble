using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dawaj
{
    public class ClassManager
    {
        int LoggedId;
        List<string> newAtributes = new List<string>();
        ArtiffactManager ArtiffactManager = new ArtiffactManager(UserManager.loggedIn.Id);
        public ClassManager(int id)
        {
            LoggedId = id;
        }
        public List<Class> getClasses()
        {
            List<Class> data;
            using (var context = new DataModel())
            {
                data = context.Classes.Include("Atributes").ToList();
            }
            return data;
        }

        public List<string> getClassesToString()
        {
            List<string> ret = new List<string>();
            foreach (var c in getClasses())
            {
                ret.Add(c.Name.ToString());
            }
            return ret;
        }

        public bool contains(string name)
        {
            if (getClassesToString().Contains(name))
            {
                return true;
            }
            return false;
        }

        public void createClass(string name, string mainAtribute, List<string> atributesDef)
        {
            using(var context = new DataModel())
            {
                List<AtributeDefinition> list = new List<AtributeDefinition>();
                for (int i = 0; i < atributesDef.Count; i++)
                {
                    var atr = new AtributeDefinition
                    {
                        Name = atributesDef[i]
                    };
                    list.Add(atr);
                }
                var variable = new Class()
                {
                    Name = name,
                    UserId = LoggedId,
                    mainAtribute = mainAtribute,
                    Atributes = list
                };
                context.Classes.Add(variable);
                context.SaveChanges();
            }
        }

        public Class getClassById(int id)
        {
            List<Class> list = new List<Class>();
            list = getClasses();
            foreach (var item in list)
            {
                if (item.Id == id)
                {
                    return item;
                }
            }
            return null;
        }

        public List<AtributeDefinition> getAtributeDefinitionsById(int id)
        {
            Class variable = getClassById(id);
            return variable.Atributes.ToList();
        }

        public List<string> getNewAtributes() { return newAtributes; }
        public void clearNewAtributes() { newAtributes.Clear(); }

        public bool addAtribute(string atribute)
        {
            if (newAtributes.Contains(atribute))
            {
                return false;
            }
            newAtributes.Add(atribute);
            return true;
        }

        public void rename(int id, string newName, string newMainAtributeName, List<string> newAtributesNames)
        {
            using(var context = new DataModel())
            {
                string oldName = context.Classes.Include("Atributes").Where(x => x.Id == id).FirstOrDefault().Name;
                context.Classes.Include("Atributes").Where(x => x.Id == id).FirstOrDefault().Name = newName;
                context.Classes.Include("Atributes").Where(x => x.Id == id).FirstOrDefault().mainAtribute = newMainAtributeName;
                for (int i = 0;  i < context.Classes.Include("Atributes").Where(x => x.Id == id).FirstOrDefault().Atributes.Count; i++)
                {
                    context.Classes.Include("Atributes").Where(x => x.Id == id).FirstOrDefault().Atributes[i].Name = newAtributesNames[i];
                }
                foreach(var item in context.Artifacts.Include("Atributes").Where(x => x.Class == oldName).ToList())
                {
                    item.Class = newName;
                    for(int i = 0; i < context.Classes.Include("Atributes").Where(x => x.Id == id).FirstOrDefault().Atributes.Count; i++)
                    {
                        item.Atributes[i].Name = newAtributesNames[i];
                    }
                }
                context.SaveChanges();
            }
        }

        public void deleteClassById(int id)
        {
            using (var context = new DataModel())
            {
                List<Class> data = context.Classes.Include("Atributes").ToList();
                foreach (var item in data)
                {
                    if (item.Id == id)
                    {
                        foreach (var art in context.Artifacts.Include("Atributes").ToList())
                        {
                            if (art.Class == getClassById(id).Name)
                            {
                                ArtiffactManager.deleteArtiffactById(art.Id);
                            }
                        }
                        context.Classes.Remove(item);
                        break;
                    }
                }
                context.SaveChanges();
            };
        }

        public void deleteAttribute(int classId, int attributeId)
        {
            using (var context = new DataModel())
            {
                var variable = context.Classes.Include("Atributes").Where(x => x.Id == classId).FirstOrDefault().Atributes.Where(x => x.Id == attributeId).FirstOrDefault();
                context.Classes.Include("Atributes").Where(x => x.Id == classId).FirstOrDefault().Atributes.Remove(variable);
                string c = getClassById(classId).Name;
                foreach (var item in context.Artifacts.Include("Atributes").Where(x => x.Class == c).ToList())
                {
                    string a = context.AtributesDefinitions.Where(y => y.Id == attributeId).Select(z => z.Name).FirstOrDefault().ToString();
                    var toDelete = item.Atributes.Where(x => x.Name == a).FirstOrDefault();
                    item.Atributes.Remove(toDelete);
                }
                context.SaveChanges();
            }
        }

        public void addAtributeTo(int id, string atributeName)
        {
            using(var context = new DataModel())
            {
                var variable = context.Classes.Include("Atributes").Where(x => x.Id == id).FirstOrDefault();
                variable.Atributes.Add(new AtributeDefinition { Name = atributeName });
                string className = getClassById(id).Name;
                foreach (var item in context.Artifacts.Include("Atributes").Where(x => x.Class == className))
                {
                    item.Atributes.Add(new Atribute { Name = atributeName, Value = null });
                }

                context.SaveChanges();
            }
        }
    }
}
