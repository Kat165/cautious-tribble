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
    public partial class ClassWindow : Form
    {
        ClassManager classManager;
        DataGridViewRow selectedRow;
        DataGridViewRow selectedRow2;
        RoleManager roleManager = new RoleManager();
        public ClassWindow(int id)
        {
            InitializeComponent();
            classManager = new ClassManager(id);
        }

        private void NewClass_Load(object sender, EventArgs e)
        {
            dataGridView1.DataSource = classManager.getClasses();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(button4.Text == "Edit class")
            {
                if (classManager.addAtribute(textBox3.Text) == false)
                {
                    MessageBox.Show("That attribute already exists");
                }
                textBox3.Clear();

                this.dataGridView2.DataSource = classManager.getNewAtributes().Select(k => new { Value = k }).ToList();
            }
            else
            {
                classManager.addAtributeTo(Int32.Parse(selectedRow.Cells[0].Value.ToString()), textBox3.Text);
                textBox3.Clear();
                dataGridView2.DataSource = classManager.getAtributeDefinitionsById(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(classManager.contains(textBox1.Text))
            {
                MessageBox.Show("Class with that name already exists");
                return;
            }
            classManager.createClass(textBox1.Text, textBox2.Text, classManager.getNewAtributes());
            classManager.clearNewAtributes();
            MessageBox.Show("Created");
            dataGridView1.DataSource = classManager.getClasses();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            selectedRow = dataGridView1.Rows[dataGridView1.CurrentCell.RowIndex];
            dataGridView2.DataSource = classManager.getAtributeDefinitionsById(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if(button4.Text == "Edit class")
            {
                if (selectedRow == null)
                {
                    MessageBox.Show("Chose Class");
                    return;
                }
                if (!roleManager.canEditClass(int.Parse(selectedRow.Cells[0].Value.ToString())))
                {
                    MessageBox.Show("You can't do this");
                    return;
                }
                DialogResult dialogResult = MessageBox.Show("Do you want to delete " + selectedRow.Cells[1].Value + "?", "Alert", MessageBoxButtons.YesNo);
                if (dialogResult == DialogResult.Yes)
                {
                    classManager.deleteClassById(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
                    MessageBox.Show("Deleted");
                    dataGridView1.DataSource = classManager.getClasses();
                    dataGridView2.DataSource = null;
                    selectedRow = null;
                }
            }
            else
            {
                if (selectedRow2 == null)
                {
                    MessageBox.Show("Chose attribute");
                    return;
                }
                DialogResult dialogResult = MessageBox.Show("Do you want to delete " + selectedRow2.Cells[0].Value + "?", "Alert", MessageBoxButtons.YesNo);
                if (dialogResult == DialogResult.Yes)
                {
                    classManager.deleteAttribute(Int32.Parse(selectedRow.Cells[0].Value.ToString()), int.Parse(selectedRow2.Cells[1].Value.ToString()));
                    MessageBox.Show("Deleted");
                    dataGridView2.DataSource = classManager.getAtributeDefinitionsById(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
                    selectedRow2 = null;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if(button4.Text == "Edit class")
            {
                if(selectedRow == null)
                {
                    MessageBox.Show("Class not chosen");
                    return;
                }
                if (!roleManager.canEditClass(int.Parse(selectedRow.Cells[0].Value.ToString())))
                {
                    MessageBox.Show("You can't do this");
                    return;
                }
                button4.Text = "Submit";
                button3.Text = "Delete attribute";
                var classSelected = classManager.getClassById(Int32.Parse(selectedRow.Cells[0].Value.ToString()));
                textBox1.Text = classSelected.Name;
                textBox2.Text = classSelected.mainAtribute;
                button2.Enabled = false;
                dataGridView1.Enabled = false;
                dataGridView2.ReadOnly = false;
            }
            else
            {
                List<string> newAtributesNames = new List<string>();
                foreach (DataGridViewRow row in dataGridView2.Rows)
                {
                    newAtributesNames.Add(row.Cells[0].Value.ToString());
                }
                classManager.rename(int.Parse(selectedRow.Cells[0].Value.ToString()), textBox1.Text, textBox2.Text, newAtributesNames);
                button4.Text = "Edit class";
                button3.Text = "Delete class";
                button2.Enabled = true;
                dataGridView1.DataSource = classManager.getClasses();
                dataGridView2.DataSource = null;
                selectedRow = null;
                selectedRow2 = null;
                textBox1.Text = "";
                textBox2.Text = "";
                dataGridView1.Enabled = true;
                dataGridView2.ReadOnly = true;
            }
        }

        private void dataGridView2_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            if(button4.Text == "Submit")
            {
                selectedRow2 = dataGridView2.Rows[dataGridView2.CurrentCell.RowIndex];
            }
        }
    }
}
