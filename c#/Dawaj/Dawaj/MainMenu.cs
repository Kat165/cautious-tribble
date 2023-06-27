using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.Entity.Migrations;

namespace Dawaj
{
    public partial class MainMenu : Form
    {
        ArtiffactManager artiffactsM;
        DataGridViewRow selectedRow;
        ArtifactsFilter artifactsFilter;
        RoleManager roleManager = new RoleManager();
        public MainMenu(int loggedId)
        {
            InitializeComponent();
            artiffactsM = new ArtiffactManager(loggedId);
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            dataGridView1.DataSource = artiffactsM.getArtiffacts(true);
            textBox1.Text = "5";
            dataGridView3.DataSource = artiffactsM.getTop(int.Parse(textBox1.Text));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            newArtiffact form = new newArtiffact(UserManager.loggedIn.Id);
            form.ShowDialog();
            dataGridView1.DataSource = artiffactsM.getArtiffacts(true);
            dataGridView2.DataSource = null;
            dataGridView3.DataSource = artiffactsM.getTop(int.Parse(textBox1.Text));
            selectedRow = null;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (selectedRow == null)
            {
                MessageBox.Show("Chose Artifact");
                return;
            }
            if (!roleManager.canEditArtifact(int.Parse(selectedRow.Cells[0].Value.ToString())))
            {
                MessageBox.Show("You can't do this");
                return;
            }
            DialogResult dialogResult = MessageBox.Show("Do you want to delete " + selectedRow.Cells[1].Value + " " + selectedRow.Cells[2].Value + "?", "Alert", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.Yes)
            {
                artiffactsM.deleteArtiffactById(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
                MessageBox.Show("Deleted");
                dataGridView1.DataSource = artiffactsM.getArtiffacts(true);
                dataGridView2.DataSource = null;
                dataGridView3.DataSource = artiffactsM.getTop(int.Parse(textBox1.Text));
                selectedRow = null;
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            selectedRow = dataGridView1.Rows[dataGridView1.CurrentCell.RowIndex];
            dataGridView2.DataSource = artiffactsM.getAtributes(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
        }

        private void dataGridView3_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            selectedRow = dataGridView3.Rows[dataGridView3.CurrentCell.RowIndex];
            dataGridView2.DataSource = artiffactsM.getAtributes(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ClassWindow form = new ClassWindow(UserManager.loggedIn.Id);
            form.ShowDialog();
            dataGridView1.DataSource = artiffactsM.getArtiffacts(true);
            selectedRow = null;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (!textBox1.Text.All(Char.IsDigit))
            {
                MessageBox.Show(textBox1.Text + " is not a number");
                return;
            }
            if (label2.Text == "Ranking")
            {
                dataGridView3.DataSource = artiffactsM.getArtiffacts(false).OrderByDescending(x => x.Id).Take(int.Parse(textBox1.Text)).ToList();
                label2.Text = "The latest Artifacts";
                button4.Text = "Ranking";
            }
            else
            {
                dataGridView3.DataSource = artiffactsM.getTop(int.Parse(textBox1.Text));
                label2.Text = "Ranking";
                button4.Text = "The latest Artifacts";
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (!textBox1.Text.All(Char.IsDigit) || textBox1.Text == "")
            {
                return;
            }
            if (label2.Text == "The latest Artifacts")
            {
                dataGridView3.DataSource = artiffactsM.getArtiffacts(false).OrderByDescending(x => x.Id).Take(int.Parse(textBox1.Text)).ToList();
            }
            else
            {
                dataGridView3.DataSource = artiffactsM.getTop(int.Parse(textBox1.Text));
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            using (var filterWindow = new FilterWindow())
            {
                var result = filterWindow.ShowDialog();
                artifactsFilter = filterWindow.getFilter();
            }
            if(artifactsFilter != null)
                dataGridView1.DataSource = artiffactsM.getArtiffacts(artifactsFilter);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            ProfileForm form = new ProfileForm();
            form.ShowDialog();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (selectedRow == null)
            {
                MessageBox.Show("Chose Artifact");
                return;
            }
            if (!roleManager.canEditArtifact(int.Parse(selectedRow.Cells[0].Value.ToString())))
            {
                MessageBox.Show("You can't do this");
                return;
            }
            newArtiffact form = new newArtiffact(UserManager.loggedIn.Id, artiffactsM.getArtiffactById(int.Parse(selectedRow.Cells[0].Value.ToString())));
            form.ShowDialog();
            dataGridView1.DataSource = artiffactsM.getArtiffacts(true);
            dataGridView2.DataSource = null;
            dataGridView3.DataSource = artiffactsM.getTop(int.Parse(textBox1.Text));
            selectedRow = null;
        }
    }
}
