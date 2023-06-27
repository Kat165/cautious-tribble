using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dawaj
{
    public class ArtiffactManager
    {
        int LoggedId;
        public ArtiffactManager(int Id)
        {
            LoggedId = Id;
        }

        public List<Artiffact> getArtiffacts(bool orderedByClass)
        {
            using (var context = new DataModel())
            {
                if (orderedByClass)
                {
                    var data = context.Artifacts.Include("Atributes").OrderBy(x => x.Class).ToList();
                    return data;
                }
                else
                {
                    var data = context.Artifacts.Include("Atributes").ToList();
                    return data;
                }  
            }
        }
        public List<Artiffact> getArtiffacts(ArtifactsFilter filter)
        {
            using (var context = new DataModel())
            {
                var data = getArtiffacts(true);
                if (filter.className != null)
                    data = data.Where(x => x.Class == filter.className).ToList();
                if (filter.userId != -1)
                    data = data.Where(x => x.UserId == filter.userId).ToList();
                if (filter.minMainAtribute != -1)
                    data = data.Where(x => x.mainAtribute >= filter.minMainAtribute).ToList();
                if (filter.maxMainAtribute != -1)
                    data = data.Where(x => x.mainAtribute <= filter.maxMainAtribute).ToList();
                return data;
            }
        }

        public List<Class> getClasses()
        {
            List<Class> variable;
            using (var context = new DataModel())
            {
                variable = context.Classes.Include("Atributes").ToList();
            }
            return variable;
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

        public Class getClassByName(string name)
        {
            return getClasses().Find(c => c.Name == name);
        }

        public string getAtributeByIndex(int i, string comboBoxText)
        {
            if (i == -1)
            {
                return getClassByName(comboBoxText).mainAtribute;
            }
            return getClassByName(comboBoxText).Atributes[i].Name;
        }

        public int getAtributesCountByName(string name)
        {
            return getClassByName(name).Atributes.Count;
        }

        public List<string> getAtributesNamesByClassName(string name)
        {
            List<string> list = new List<string>();
            foreach(var c in getClassByName(name).Atributes)
            {
                list.Add(c.Name.ToString());
            }
            return list;
        }

        public void createArtiffact(string c, string name, int mainAtribute, List<string> atributes)
        {
            List<string> lista = getAtributesNamesByClassName(c);
            if(getArtiffacts(new ArtifactsFilter(c, "All", -1, -1)).OrderByDescending(x => x.mainAtribute).ToList().Count != 0)
            {
                int maxValueOfMainAtribute = getArtiffacts(new ArtifactsFilter(c, "All", -1, -1)).OrderByDescending(x => x.mainAtribute).ToList()[0].mainAtribute;
                if(maxValueOfMainAtribute < mainAtribute)
                    mainAtribute = maxValueOfMainAtribute;
            }
            

            using (var context = new DataModel())
            {
                List<Atribute> list = new List<Atribute>();
                for (int i = 0; i < atributes.Count; i++)
                {
                    var atr = new Atribute
                    {
                        Value = atributes[i],
                        Name = lista[i]
                    };
                    list.Add(atr);
                }

                var variable = new Artiffact
                {
                    Name = name,
                    Class = c,
                    mainAtribute = mainAtribute,
                    Atributes = list,
                    UserId = LoggedId
                };
                context.Artifacts.Add(variable);
                context.SaveChanges();
            }
        }

        public Artiffact getArtiffactById(int id)
        {
            List<Artiffact> list = new List<Artiffact>();
            list = getArtiffacts(true);
            foreach(var item in list)
            {
                if (item.Id == id)
                {
                    return item;
                }
            }
            return null;
        }

        public void deleteArtiffactById(int id)
        {
            using (var context = new DataModel())
            {
                List<Artiffact> data = context.Artifacts.Include("Atributes").ToList();
                foreach (var item in data)
                {
                    if (item.Id == id)
                    {
                        context.Artifacts.Remove(item);
                        break;
                    }
                }
                context.SaveChanges();
            };
        }

        public List<Atribute> getAtributes(int id)
        {
            return getArtiffactById(id).Atributes.ToList();
        }
        public List<Artiffact> getTop(int count)
        {
            var ret = getArtiffacts(true).OrderByDescending(x => x.mainAtribute).Take(count).ToList();
            return ret;
        }

        public void edit(int oldId, string name, int mainAtribute, List<string> atributeValues)
        {
            using (var context = new DataModel())
            {
                var artifact = context.Artifacts.Include("Atributes").Where(x => x.Id == oldId).FirstOrDefault();
                artifact.Name = name;
                artifact.mainAtribute = mainAtribute;
                for (int i = 0; i < artifact.Atributes.Count; i++)
                {
                    artifact.Atributes[i].Value = atributeValues[i];
                }
                context.SaveChanges();
            }
        }
    }
}
