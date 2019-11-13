using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Domain.Models;
using Domain.ValueObjects;

namespace Presentation.Forms
{
    public partial class FormEmployee : Form
    {
        private EmployeeModel employee = new EmployeeModel();

        public FormEmployee()
        {
            InitializeComponent();
        }

        private void FormEmployee_Load(object sender, EventArgs e)
        {

            ListEmployees();
            panel1.Enabled = false;

        }

        private void ListEmployees()
        {
            try
            {
                dgvDatos.DataSource = employee.GetAll();
            }
            catch (Exception ex)
            {

                MessageBox.Show(ex.ToString());
            }
        }

        private void txtSearch_TextChanged(object sender, EventArgs e)
        {
            dgvDatos.DataSource = employee.FindById(txtSearch.Text);
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            employee.IdNumber = txtIdentificationNumber.Text;
            employee.Name = txtName.Text;
            employee.Mail = txtEmail.Text;
            employee.Birthday = dTBirthday.Value;

            bool valid = new Helps.DataValidation(employee).Validate();

            if (valid)
            {
                string result = employee.SaveChange();
                MessageBox.Show(result);
                ListEmployees();
                Restart();
            }

        }

        private void Restart()
        {
            panel1.Enabled = false;
            txtIdentificationNumber.Clear();
            txtEmail.Clear();
            txtName.Clear();

        }

        private void btnNew_Click(object sender, EventArgs e)
        {
            panel1.Enabled = true;
            employee.State = EntityState.Added;
        }

        private void btnEdit_Click(object sender, EventArgs e)
        {
            if (dgvDatos.SelectedRows.Count>0)
            {
                panel1.Enabled = true;
                employee.State = EntityState.Modified;
                employee.IdPK = Convert.ToInt32( dgvDatos.CurrentRow.Cells[0].Value);
                txtIdentificationNumber.Text = dgvDatos.CurrentRow.Cells[1].Value.ToString();
                txtName.Text = dgvDatos.CurrentRow.Cells[2].Value.ToString();
                txtEmail.Text = dgvDatos.CurrentRow.Cells[3].Value.ToString();
                dTBirthday.Value = Convert.ToDateTime(dgvDatos.CurrentRow.Cells[4].Value);
            }
            else
            {
                MessageBox.Show("Select row");
            }
        }

        private void btnRemove_Click(object sender, EventArgs e)
        {
            if (dgvDatos.SelectedRows.Count > 0)
            {
               
                employee.State = EntityState.Deleted;
                employee.IdPK = Convert.ToInt32(dgvDatos.CurrentRow.Cells[0].Value);
                string result = employee.SaveChange();
                MessageBox.Show(result);
                ListEmployees();

            }
            else
            {
                MessageBox.Show("Select row");
            }
        }
    }
}
