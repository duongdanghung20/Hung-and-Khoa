public class Employee {
    private String ID, fullName, department;
    private long basicSalary, extraSalary;
    double income;

    public double getIncome() {
        return income;
    }

    public long getBasicSalary() {
        return basicSalary;
    }

    public long getExtraSalary() {
        return extraSalary;
    }

    public String getDepartment() {
        return department;
    }

    public String getFullName() {
        return fullName;
    }

    public String getID() {
        return ID;
    }

    public void setBasicSalary(long basicSalary) {
        this.basicSalary = basicSalary;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public void setExtraSalary(long extraSalary) {
        this.extraSalary = extraSalary;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public void setID(String ID) {
        this.ID = ID;
    }

    public void setIncome(double income) {
        this.income = income;
    }
}
