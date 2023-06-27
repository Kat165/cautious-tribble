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
    public partial class ProfileForm : Form
    {
        UserManager userManager = new UserManager();
        RoleManager roleManager = new RoleManager();
        public ProfileForm()
        {
            InitializeComponent();
        }

        private void ProfileForm_Load(object sender, EventArgs e)
        {
            comboBox1.DataSource = roleManager.getUsersList(UserManager.loggedIn.Id);
            comboBox2.DataSource = roleManager.getRolesString();
            comboBox1.SelectedItem = UserManager.loggedIn.Name;
            comboBox2.SelectedItem = userManager.getUserByName(comboBox1.Text).Role.Name;
            if(userManager.getUserByName(UserManager.loggedIn.Name).Role.Name != "Admin")
            {
                button2.Enabled = false;
                comboBox1.Enabled = false;
            }
            comboBox2.Enabled = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(!userManager.checkPassword(comboBox1.Text, textBox1.Text))
            {
                MessageBox.Show("Password incorect");
                return;
            }
            if(textBox2.Text != textBox3.Text)
            {
                MessageBox.Show("Passwords are not equal");
                return;
            }
            MessageBox.Show("Password changed");
            userManager.changePassword(textBox2.Text, userManager.getUserByName(comboBox1.Text).Id);
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            comboBox2.SelectedItem = userManager.getUserByName(comboBox1.Text).Role.Name;
            if (comboBox1.SelectedIndex == 0)
                comboBox2.Enabled = false;
            else
                comboBox2.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            NewRole form = new NewRole();
            form.ShowDialog();
            comboBox2.DataSource = roleManager.getRolesString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            roleManager.changeRole(comboBox1.Text, comboBox2.Text);
            button3.Enabled = false;
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            if(userManager.getUserByName(comboBox1.Text).Role.Name != comboBox2.Text)
            {
                button3.Enabled = true;
            }
            else
                button3.Enabled = false;
        }
    }
}
