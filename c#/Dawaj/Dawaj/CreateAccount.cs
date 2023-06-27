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
    public partial class CreateAccount : Form
    {
        UserManager userManager = new UserManager();
        public CreateAccount()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (userManager.doesUserNameExists(textBox1.Text) && textBox2.Text == textBox3.Text)
            {
                userManager.createUser(textBox1.Text, textBox2.Text);
                MessageBox.Show("Created");
                this.Close();
                return;
            }
            MessageBox.Show("Username exists or paswords are not equal");
        }
    }
}
