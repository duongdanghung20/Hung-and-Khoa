import java.util.*;
import java.io.*;

public class EmployeeTestDrive {
    public static void main(String[] args) {
        System.out.println("Enter the number of employees: ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Employee[] employees = new Employee[n];
        for (int i=0; i<n; i++)
        {
            employees[i] = new Employee();
        }
        for (int i=0; i<n; i++)
        {
            System.out.println("Enter employee "+(i+1)+"'s information: ");
            System.out.println("Employee ID: ");
            employees[i].setID(sc.next());
            System.out.println("Employee full name (with no blank space): ");
            employees[i].setFullName(sc.next());
            System.out.println("Employee department: ");
            employees[i].setDepartment(sc.next());
            System.out.println("Employee's basic salary: ");
            employees[i].setBasicSalary(sc.nextLong());
            System.out.println("Employee's extra salary: ");
            employees[i].setExtraSalary(sc.nextLong());
        }
        try
        {
            PrintWriter out = new PrintWriter(new FileWriter("employee.txt"));
            for (int i=0; i<n; i++)
            {
                out.println(employees[i].getID());
                out.println(employees[i].getFullName());
                out.println(employees[i].getDepartment());
                out.println(employees[i].getBasicSalary());
                out.println(employees[i].getExtraSalary());
            }
            out.close();
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
        try
        {
            Scanner sc2 = new Scanner(new FileInputStream("employee.txt"));
            ArrayList x = new ArrayList();
            while (sc2.hasNextLine()) {
                x.add(sc2.nextLine());
            }
            sc2.close();
            for (int i=0; i<n; i++)
            {
                employees[i].setIncome(Double.parseDouble(String.valueOf(x.get(5*(i+1)-1)))*2.5+Double.parseDouble(String.valueOf(x.get(5*(i+1)-2))));
            }
        }
        catch (IOException e2)
        {
            e2.printStackTrace();
        }
        for (int i=0; i<n; i++)
        {
            System.out.println("Information of employee "+(i+1)+":");
            System.out.print("Employee ID: ");
            System.out.println(employees[i].getID());
            System.out.print("Full name: ");
            System.out.println(employees[i].getFullName());
            System.out.print("Department: ");
            System.out.println(employees[i].getDepartment());
            System.out.print("Income: ");
            System.out.println(employees[i].getIncome());
            System.out.println(" ");
        }
    }
}
