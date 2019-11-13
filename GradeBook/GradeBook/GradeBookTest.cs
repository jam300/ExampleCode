using System;

public class GradeBookTest
{
    public static void Main (string[] args)
    {
        /// create GradeBook object myGradeBook and
        /// pass course name to constructor
        GradeBook myGradeBook = new GradeBook("CS101 Introduction to C# Programming");

        myGradeBook.DisplayMessage(); //display welcome message
        myGradeBook.InputGrades(); // read grades from user
        myGradeBook.DisplayGradeReport(); // display report based on grades
        
        Console.ReadKey(true);

    }
}
