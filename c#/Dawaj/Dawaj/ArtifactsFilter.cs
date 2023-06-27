using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dawaj
{
    public class ArtifactsFilter
    {
        public string className;
        public int userId = -1;
        public int maxMainAtribute = -1;
        public int minMainAtribute = -1;
        UserManager userManager = new UserManager();

        public ArtifactsFilter(string c, string userName, int minMA, int maxMA)
        {
            if(c != "All")
                className = c;
            if (userName != "All")
                userId = userManager.getUserByName(userName).Id;
            maxMainAtribute = maxMA;
            minMainAtribute = minMA;
        }

        public string toString()
        {
            return className.ToString() + " " + userId.ToString() + " " + maxMainAtribute.ToString() + " " + minMainAtribute.ToString();
        }
    }
}
