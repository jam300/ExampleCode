using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DataAcces.Contracts;
using DataAcces.Entities;
using DataAcces.Repositories;
using Domain.ValueObjects;
using System.ComponentModel.DataAnnotations;

namespace Domain.Models
{
    public class EmployeeModel:IDisposable
    {
        private int idPK;
        private string idNumber;
        private string name;
        private string mail;
        private DateTime birthday;
        private int age;

        private IEmployeeRepository employeeRepository;
        public EntityState State { private get; set; }
        private List<EmployeeModel> listEmployees;

        //PROPIEDADES/MODELO DE VISTA / VALIDAR DATOS
        public int IdPK { get => idPK; set => idPK = value; }
        [Required(ErrorMessage ="The field identification number is requerid")]
        [RegularExpression("([0-9])+",ErrorMessage ="Identification number must be only numbers")]
        [StringLength(maximumLength:10,MinimumLength =10, ErrorMessage = "Identification number must be 10 digits")]
        public string IdNumber { get => idNumber; set => idNumber = value; }
        [Required]
        [RegularExpression("^[a-zA-Z]+$", ErrorMessage ="The field name must be only letters")]
        [StringLength(maximumLength:100,MinimumLength =3)]
        public string Name { get => name; set => name = value; }
        [Required]
        [EmailAddress]
        public string Mail { get => mail; set => mail = value; }
        public DateTime Birthday { get => birthday; set => birthday = value; }
        public int Age { get => age; private set => age = value; }

        public EmployeeModel()
        {
            employeeRepository = new EmployeeRepository();
        }

        public string SaveChange()
        {
            string message = null;
            try
            {
                var employeeDataModel = new Employee();

                employeeDataModel.idPK      = idPK;
                employeeDataModel.idNumber  = idNumber;
                employeeDataModel.name      = name;
                employeeDataModel.mail      = mail;
                employeeDataModel.birthday  = birthday;

                switch (State)
                {
                    case EntityState.Added:
                        //Ejecutar reglas comerciales
                        employeeRepository.Add(employeeDataModel);
                        message = "Successfully  record";
                        break;
                    case EntityState.Modified:
                        employeeRepository.Adit(employeeDataModel);
                        message = "successfully edited";
                        break;
                    case EntityState.Deleted:
                        employeeRepository.Remove(idPK);
                        message = "successfully removed";
                        break;

                }
            }
            catch(Exception ex)
            {
                System.Data.SqlClient.SqlException sqlEx = ex as System.Data.SqlClient.SqlException;

                if (sqlEx != null && sqlEx.Number ==2627)
                {
                    message = "Duplicate Record";
                }
                else
                {
                    message = ex.ToString();
                }
            }


            return message;
        }

        public List<EmployeeModel> GetAll()
        {
            var employeeDataModel = employeeRepository.GetAll();
             listEmployees = new List<EmployeeModel>();
            foreach(Employee item in employeeDataModel)
            {
                var birthDate = item.birthday;
                listEmployees.Add(new EmployeeModel
                {
                    idPK = item.idPK,
                    idNumber = item.idNumber,
                    name = item.name,
                    mail = item.mail,
                    birthday = item.birthday,
                    age      = CalculaAge(birthDate),

                });
            }

            return listEmployees;
        }

        public IEnumerable<EmployeeModel>FindById(string filter)
        {
            return listEmployees.FindAll(e => e.IdNumber.Contains(filter) || e.name.ToUpper().Contains(filter.ToUpper()));
        }
        private int CalculaAge(DateTime date)
        {
            DateTime dateNow = DateTime.Now;
            return dateNow.Year - date.Year;
        }

        void IDisposable.Dispose()
        {
            
        }
    }
}
