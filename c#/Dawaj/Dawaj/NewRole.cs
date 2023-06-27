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
    public partial class NewRole : Form
    {
        RoleManager roleManager = new RoleManager();
        ClassManager classManager = new ClassManager(UserManager.loggedIn.Id);
        ArtiffactManager artiffactManager = new ArtiffactManager(UserManager.loggedIn.Id);
        public NewRole()
        {
            InitializeComponent();
        }

        private void NewRole_Load(object sender, EventArgs e)
        {
            checkedListBox1.Items.AddRange(roleManager.getStringRights().ToArray());
            label3.Enabled = false;
            textBox2.Enabled = false;
            checkedListBox2.Items.Add("Default");
            checkedListBox2.Items.AddRange(classManager.getClassesToString().ToArray());
            checkedListBox3.Items.Add("Default");
            checkedListBox3.Items.AddRange(artiffactManager.getArtiffacts(false).Select(x => x.Name).ToArray());
        }

        private void checkedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            for(int i = 0; i <checkedListBox2.Items.Count; i++)
            {
                checkedListBox2.SetItemChecked(i, false);
                if (roleManager.getRightClasses(checkedListBox1.SelectedItem.ToString()).Contains(checkedListBox2.Items[i]))
                    checkedListBox2.SetItemChecked(i, true);
            }
                
            for (int i = 0; i < checkedListBox3.Items.Count; i++)
            {
                checkedListBox3.SetItemChecked(i, false);
                if (roleManager.getRightArtifacts(checkedListBox1.SelectedItem.ToString()).Contains(checkedListBox3.Items[i]))
                    checkedListBox3.SetItemChecked(i, true);
            }
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(button2.Text == "New right")
            {
                button2.Text = "Submit";
                label3.Enabled = true;
                textBox2.Enabled = true;
                checkedListBox2.ClearSelected();
                checkedListBox3.ClearSelected();
            }
            else
            {
                if (checkedListBox1.Items.Contains(textBox2.Text))
                {
                    MessageBox.Show("Right with that name already exists");
                    return;
                }
                button2.Text = "New right";
                List<string> classes = new List<string>();
                foreach(var i in checkedListBox2.CheckedItems)
                    classes.Add(i.ToString());
                List<string> artifacts = new List<string>();
                foreach (var i in checkedListBox3.CheckedItems)
                    artifacts.Add(i.ToString());
                roleManager.newRight(textBox2.Text , classes, artifacts);
                checkedListBox1.Items.Clear();
                checkedListBox1.Items.AddRange(roleManager.getStringRights().ToArray());
                label3.Enabled = false;
                textBox2.Enabled = false;
                checkedListBox2.ClearSelected();
                checkedListBox3.ClearSelected();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (roleManager.getRolesString().Contains(textBox1.Text))
            {
                MessageBox.Show("Role with that name already exists");
                return;
            }
            if (checkedListBox1.SelectedItem == null)
                roleManager.createRole(textBox1.Text, new List<string>());
            else
            {
                List<string> list = new List<string>();
                foreach(var item in checkedListBox1.CheckedItems)
                    list.Add(item.ToString());

                roleManager.createRole(textBox1.Text, list);
            }

            MessageBox.Show("Created");
            this.Close();
        }
    }
}
