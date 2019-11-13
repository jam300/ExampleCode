﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;

namespace DataAcces.Repositories
{
    public abstract class MasterRepository:Repository
    {
        protected List<SqlParameter> parameters;

        protected int ExecuteNonQuery( string transactSql)
        {
            using (var connection = GetConnection())
            {
                connection.Open();
                using (var command = new SqlCommand())
                {
                    command.Connection  = connection;
                    command.CommandText = transactSql;
                    command.CommandType = CommandType.Text;

                    foreach(SqlParameter item in parameters)
                    {
                        command.Parameters.Add(item);
                    }
                    int result = command.ExecuteNonQuery();
                    parameters.Clear();
                    return result;

                }
            }

        }

        protected DataTable ExecuteReader(string transactSql)
        {
            using (var connection = GetConnection())
            {
                connection.Open();
                using (var command = new SqlCommand())
                {
                    command.Connection   = connection;
                    command.CommandText  = transactSql;
                    command.CommandType  = CommandType.Text;
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        using (var table = new DataTable())
                        {
                            table.Load(reader);
                            return table;

                        }

                    }               
 

                }
            }
        }



    }
}
