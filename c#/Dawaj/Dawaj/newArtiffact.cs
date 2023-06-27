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
    public partial class newArtiffact : Form
    {
        public ArtiffactManager newArtiffactManager;
        ClassManager classManager = new ClassManager(UserManager.loggedIn.Id);
        RoleManager roleManager = new RoleManager();    
        int atributeIndex = -2;
        string name;
        int mainAtribute;
        List<string> atributesValue = new List<string>();
        bool edit;
        Artiffact toEdit;
        public newArtiffact(int LoggedId)
        {
            InitializeComponent();
            newArtiffactManager = new ArtiffactManager(LoggedId);
            edit = false;
        }

        public newArtiffact(int LoggedId, Artiffact artiffact)
        {
            InitializeComponent();
            newArtiffactManager = new ArtiffactManager(LoggedId);
            edit = true;
            toEdit = artiffact;
        }

        private void newArtiffact_Load(object sender, EventArgs e)
        {
            if (!edit)
            {
                comboBox1.DataSource = newArtiffactManager.getClassesToString();
                comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;   
            }
            else
            {
                comboBox1.DataSource = new List<string>() { toEdit.Class };
                comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
                comboBox1.Enabled = false;
                textBox1.Text = toEdit.Name;
            }
              
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (atributeIndex == -2)
                return;
            label2.Text = newArtiffactManager.getAtributeByIndex(atributeIndex, comboBox1.Text);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (!edit)
                createNewForm();
            else
                editForm();
        }

        public void createNewForm()
        {
            if (atributeIndex == -2)
            {
                if(!roleManager.canEditClass(classManager.getClasses().Where(x => x.Name == comboBox1.Text).FirstOrDefault().Id))
                {
                    MessageBox.Show("You can't do this");
                    return;
                }
                comboBox1.Enabled = false;
                name = textBox1.Text;
            }
            if (atributeIndex == -1)
                if (textBox1.Text.All(Char.IsDigit) && textBox1.Text != "")
                    mainAtribute = Convert.ToInt32(textBox1.Text);
                else
                {
                    MessageBox.Show("Not a number");
                    return;
                }
            if (atributeIndex > -1)
            {
                atributesValue.Add(textBox1.Text);
            }

            atributeIndex++;
            if (atributeIndex >= newArtiffactManager.getAtributesCountByName(comboBox1.Text))
            {
                newArtiffactManager.createArtiffact(comboBox1.Text, name, mainAtribute, atributesValue);
                MessageBox.Show("Artiffact created");
                this.Close();
            }
            else
            {
                label2.Text = newArtiffactManager.getAtributeByIndex(atributeIndex, comboBox1.Text);
            }
            textBox1.Clear();
        }

        public void editForm()
        {
            if (atributeIndex == -2)
            {
                comboBox1.Enabled = false;
                name = textBox1.Text;
                textBox1.Text = toEdit.mainAtribute.ToString();
            }
            if (atributeIndex == -1)
            {
                if (textBox1.Text.All(Char.IsDigit) && textBox1.Text != "")
                    mainAtribute = Convert.ToInt32(textBox1.Text);
                else
                {
                    MessageBox.Show("Not a number");
                    return;
                }
                textBox1.Text = toEdit.Atributes[atributeIndex + 1].Value;
            }
                
            if (atributeIndex > -1)
            {
                atributesValue.Add(textBox1.Text);
                if(atributeIndex + 1 < toEdit.Atributes.Count)
                    textBox1.Text = toEdit.Atributes[atributeIndex + 1].Value;
            }

            atributeIndex++;
            if (atributeIndex >= newArtiffactManager.getAtributesCountByName(comboBox1.Text))
            {
                newArtiffactManager.edit(toEdit.Id, name, mainAtribute, atributesValue);
                MessageBox.Show("Artiffact edited");
                this.Close();
            }
            else
            {
                label2.Text = newArtiffactManager.getAtributeByIndex(atributeIndex, comboBox1.Text);
            }
        }
    }
}
