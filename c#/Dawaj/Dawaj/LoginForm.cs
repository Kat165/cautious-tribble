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
    public partial class LoginForm : Form
    {
        public UserManager userManager;
        public RoleManager roleManager = new RoleManager();
        public LoginForm()
        {
            InitializeComponent();
            userManager = new UserManager();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (userManager.checkPassword(textBox1.Text, textBox2.Text))
            {
                MainMenu form = new MainMenu(UserManager.loggedIn.Id);
                this.Hide();
                form.ShowDialog();
                this.Show();
            }
            else
            {
                MessageBox.Show("Name or password incorect");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            CreateAccount createAccount = new CreateAccount();
            createAccount.ShowDialog();
        }
    }
}
