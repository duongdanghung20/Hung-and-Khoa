package a2_BI10_073.studentman;
import a2_BI10_073.studentman.Document;
import utils.*;

import java.util.Comparator;
import java.util.Objects;

/**
 * @overview Student is a person who go to school
 * @attributes
 *  id  Integer int
 *  name    String
 *  phoneNumber String
 *  address String
 * @object
 *  A typical Student is s = <i,n,p,a>, where id(i), name(n), phoneNumber(p), address(a).
 * @abstract_properties
 *    mutable(id) = false /\ optional(id) = false /\ min(id) = 1 /\ max(id) = 10^9 /\
 *    mutable(name) = true /\ optional(name) = false /\ length(name) = 50 /\
 *    mutable(phoneNumber) = true /\ optional(phoneNumber) = false /\ length(phoneNumber) = 10 /\
 *    mutable(address) = true /\ optional(address) = false /\ length(address) = 100
 * @author Duong Dang Hung
 */

public class Student implements Comparable<Student>, Document {
    private static final int MIN_ID = 1;
    private static final int MAX_ID = 1000000000;
    @DomainConstraint(type = "Integer", mutable = false, optional = false, min = MIN_ID, max = MAX_ID)
    private int id;
    @DomainConstraint(type = "String", mutable = true, optional = false, length = 50)
    private String name;
    @DomainConstraint(type = "String", mutable = true, optional = false, length = 10)
    private String phoneNumber;
    @DomainConstraint(type = "String", mutable = true, optional = false, length = 100)
    private String address;

    // constructor methods
    /**
     * @effects
     *            if id, name, phoneNumber, address are valid
     *              initialise this as Student:<id,name,phoneNumber,address>
     *            else
     *              throws NotPossibleException
     *
     */
    public Student(@AttrRef("id") int id, @AttrRef("name") String name, @AttrRef("phoneNumber") String phoneNumber, @AttrRef("address") String address)
            throws NotPossibleException {
        if (!validateID(id)) {
            throw new NotPossibleException("Student.init: invalid id: " + id);
        }
        if (!validateName(name)) {
            throw new NotPossibleException("Student.init: invalid name: " + name);
        }
        if (!validatePhoneNumber(phoneNumber)) {
            throw new NotPossibleException("Student.init: invalid phoneNumber: " + phoneNumber);
        }
        if (!validateAddress(address)) {
            throw new NotPossibleException("Student.init: invalid address: " + address);
        }
        this.id = id;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.address = address;
    }

    // methods
    /**
     * @effects
     *  if name is valid
     *      set this.name = name
     *  else
     *      throws NotPossibleException
     */
    @DOpt(type = OptType.Mutator) @AttrRef("name")
    public boolean setName(String name) {
        if (validateName(name)) {
            this.name = name;
            return true;
        }
        else {
            return false;
        }
    }

    /**
     * @effects
     *  if phoneNumber is valid
     *      set this.phoneNumber = phoneNumber
     *  else
     *      throws NotPossibleException
     */
    @DOpt(type = OptType.Mutator) @AttrRef("phoneNumber")
    public boolean setPhoneNumber(String phoneNumber) {
        if(validatePhoneNumber(phoneNumber)) {
            this.phoneNumber = phoneNumber;
            return true;
        }
        else
            return false;
    }

    /**
     * @effects
     *  if address is valid
     *      set this.address = address
     *  else
     *      throws NotPossibleException
     */
    @DOpt(type = OptType.Mutator) @AttrRef("address")
    public boolean setAddress(String address) {
        if(validateAddress(address)) {
            this.address = address;
            return true;
        }
        else
            return false;
    }

    /**
     *
     * @effects
     *  return this.id
     */
    @DOpt(type = OptType.Observer) @AttrRef("id")
    public int getId() {
        return id;
    }

    /**
     *
     * @effects
     *  return this.name
     */
    @DOpt(type = OptType.Observer) @AttrRef("name")
    public String getName() {
        return name;
    }

    /**
     *
     * @effects
     *  return this.address
     */
    @DOpt(type = OptType.Observer) @AttrRef("address")
    public String getAddress() {
        return address;
    }

    /**
     *
     * @effects
     *  return this.phoneNumber
     */
    @DOpt(type = OptType.Observer) @AttrRef("phoneNumber")
    public String getPhoneNumber() {
        return phoneNumber;
    }


    // validation methods
    /**
     * @effects
     *  if i is valid
     *      return true
     *  else
     *      return false
     */
    protected boolean validateID(int i) {
        if (i<MIN_ID || i>MAX_ID) {
            return false;
        }
        return true;
    }

    /**
     * @effects
     *  if n is valid
     *      return true
     *  else
     *      return false
     */
    private boolean validateName(String n) {
        if (n == null || n.length() > 50 || n.isBlank() || n.isEmpty()) {
            return false;
        }
        return true;
    }

    /**
     * @effects
     *  if p is valid
     *      return true
     *  else
     *      return false
     */
    private boolean validatePhoneNumber(String p) {
        if (p == null || p.length() > 10 || p.isBlank() || p.isEmpty()) {
            return false;
        }
        return true;
    }

    /**
     * @effects
     *  if a is valid
     *      return true
     *  else
     *      return false
     */
    private boolean validateAddress(String a) {
        if (a == null || a.length() > 100 || a.isBlank() || a.isEmpty()) {
            return false;
        }
        return true;
    }

    /**
     * @effects
     *  if <i,n,p,a> is a valid tuple
     *      return true
     *  else
     *      return false
     */
    private boolean validate(int i, String n, String p, String a) {
        return(validateName(n) && validatePhoneNumber(p) && validateID(i) && validateAddress(a));
    }

    /**
     * @effects
     *  if this satisfies rep invariant
     *      return true
     *  else
     *      return false
     */
    public boolean repOK() { return validate(id, name, phoneNumber, address); }

    @Override
    public String toString() {
        if (this.getClass().getSimpleName() == "UndergradStudent") {
            return "UndergradStudent(" + name + ")";
        }
        else if (this.getClass().getSimpleName() == "PostgradStudent") {
            return "PostgradStudent(" + name + ")";
        }
        else {
            return "Student(" + name + ")";
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return id == student.id &&
                Objects.equals(name, student.name) &&
                Objects.equals(phoneNumber, student.phoneNumber) &&
                Objects.equals(address, student.address);
    }

    /**
     *
     * @effects
     *  return result of comparing this.name and student.name
     */
    @Override
    public int compareTo(Student student) {
        int compare = (this.getName()).compareTo(student.getName());
        return compare;
    }

    // ASC (natural) ordering
    public static int compareByNameAsc(Student v1, Student v2) {
        return v1.getName().compareTo(v2.getName());
    }

    // DESC (reversed natural) ordering
    public static int compareByNameDesc(Student v1, Student v2) {
        return v2.getName().compareTo(v1.getName());
    }


    /**
     *
     * @effects
     *  return a String containing the text of a simple HTML document generated from the state of the current object
     */
    @Override
    public String toHtmlDoc() {
        if (this.getClass().getSimpleName() == "UndergradStudent") {
            return "<html>\n<head><title>UndergradStudent:" + this.id + "-" + this.name + "</title></head>\n<body>\n" + this.id + " " + this.name + " " + this.phoneNumber + " " + this.address + "\n</body></html>";
        }
        else if (this.getClass().getSimpleName() == "PostgradStudent") {
            return "<html>\n<head><title>PostgradStudent:" + this.id + "-" + this.name + "</title></head>\n<body>\n" + this.id + " " + this.name + " " + this.phoneNumber + " " + this.address + "\n</body></html>";
        }
        else {
            return "<html>\n<head><title>Student:" + this.id + "-" + this.name + "</title></head>\n<body>\n" + this.id + " " + this.name + " " + this.phoneNumber + " " + this.address + "\n</body></html>";
        }
    }
}
