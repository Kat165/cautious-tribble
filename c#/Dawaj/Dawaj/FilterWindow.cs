using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Dawaj
{
    public partial class FilterWindow : Form
    {
        ClassManager classManager = new ClassManager(UserManager.loggedIn.Id);
        UserManager userManager = new UserManager();
        ArtifactsFilter artifactsFilter;
        ArtiffactManager artiffactManager = new ArtiffactManager(UserManager.loggedIn.Id);
        public FilterWindow()
        {
            InitializeComponent();
            List<string> list = new List<string>() { "All"};
            List<string> list2 = new List<string>() { "All" };
            list.AddRange(classManager.getClassesToString());
            comboBox1.DataSource = list;
            list2.AddRange(userManager.getUsers().Select(x => x.Name).ToList());
            comboBox2.DataSource = list2;
            textBox1.Text = "0";
            textBox2.Text = artiffactManager.getTop(1)[0].mainAtribute.ToString();
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox2.DropDownStyle = ComboBoxStyle.DropDownList;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (!((textBox1.Text.All(Char.IsDigit) && textBox1.Text != "") && (textBox2.Text.All(Char.IsDigit) && textBox2.Text != "")))
            {
                MessageBox.Show("Not a number");
                return;
            }
            artifactsFilter = new ArtifactsFilter(comboBox1.Text, comboBox2.Text, int.Parse(textBox1.Text), int.Parse(textBox2.Text));
            this.Close();
        }

        public ArtifactsFilter getFilter() { return artifactsFilter; }
    }
}
