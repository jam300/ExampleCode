using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DataAcces.Contracts;
using DataAcces.Entities;
using System.Data;
using System.Data.SqlClient;

namespace DataAcces.Repositories
{
    public class EmployeeRepository : MasterRepository, IEmployeeRepository
    {
        //campos
        private string selectAll;
        private string insert;
        private string update;
        private string delete;
        //Propiedades

        //Constructores

        public EmployeeRepository()
        {
            selectAll = "select *from Employee";
            insert = "insert into Employee values (@idNumber, @name, @mail, @birthday)";
            update = "update Employee set IdNumber=@idNumber, Name=@name, Mail=@mail, Birthday=@birthday where idPK=@idPK";
            delete = "delete from Employee where idPK=@idPK";
        }


        //Metodos
        public int Add(Employee entity)
        {
            parameters = new List<SqlParameter>();
            parameters.Add(new SqlParameter("@idNumber", entity.idNumber));
            parameters.Add(new SqlParameter("@name", entity.name));
            parameters.Add(new SqlParameter("@mail", entity.mail));
            parameters.Add(new SqlParameter("@birthday", entity.birthday));

            return ExecuteNonQuery(insert);

        }

        public int Adit(Employee entity)
        {
            parameters = new List<SqlParameter>();
            parameters.Add(new SqlParameter("@idPK", entity.idPK));
            parameters.Add(new SqlParameter("@idNumber", entity.idNumber));
            parameters.Add(new SqlParameter("@name", entity.name));
            parameters.Add(new SqlParameter("@mail", entity.mail));
            parameters.Add(new SqlParameter("@birthday", entity.birthday));

            return ExecuteNonQuery(update);
        }

        public IEnumerable<Employee> GetAll()
        {
            var tableResult = ExecuteReader(selectAll);
            var listEmployees = new List<Employee>();
            
            foreach(DataRow item in tableResult.Rows)
            {
                listEmployees.Add(new Employee
                {
                    idPK     = Convert.ToInt32(item[0]),
                    idNumber = item[1].ToString(),
                    name     = item[2].ToString(),
                    mail     = item[3].ToString(),
                    birthday = Convert.ToDateTime(item[4])
                });

            }
            return listEmployees;

        }

        public int Remove(int idPK)
        {
            parameters = new List<SqlParameter>
            {
                new SqlParameter("@idPK", idPK)
            };

            return ExecuteNonQuery(delete);
        }
    }
}
