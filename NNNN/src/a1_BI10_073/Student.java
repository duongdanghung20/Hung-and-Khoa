package a1_BI10_073;
import utils.*;

import java.util.Objects;

/**
 * @overview Student is a person who go to school
 * @attributes
 *  id          Integer     int
 *  name        String
 *  phoneNumber String
 *  address     String
 * @object
 *  A typical Student is s = <i,n,p,a>, where id(i), name(n), phoneNumber(p), address(a).
 * @abstract_properties
 *    mutable(id) = false /\ optional(id) = false /\ min(id) = 1 /\ max(id) = 10^9 /\
 *    mutable(name) = true /\ optional(name) = false /\ length(name) = 50 /\
 *    mutable(phoneNumber) = true /\ optional(phoneNumber) = false /\ length(phoneNumber) = 10 /\
 *    mutable(address) = true /\ optional(address) = false /\ length(address) = 100
 * @author Duong Dang Hung
 */

public class Student implements Comparable<Student> {

    @DomainConstraint(type = "Integer", mutable = false, optional = false, min = 1, max = 1.0E9)
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
     *            if i,n,p,a are valid
     *              initialise this as Student:<i,n,p,a>
     *            else
     *              throws NotPossibleException
     *
     */
    public Student(@AttrRef("id") int i, @AttrRef("name") String n,
                   @AttrRef("phoneNumber") String p, @AttrRef("address") String a)
            throws NotPossibleException {
        if(!validateID(i)) {
            throw new NotPossibleException("Student.init: invalid id: " + i);
        }
        if(!validateName(n)) {
            throw new NotPossibleException("Student.init: invalid name: " + n);
        }
        if(!validatePhoneNumber(p)) {
            throw new NotPossibleException("Student.init: invalid phone number: " + p);
        }
        if(!validateAddress(a)) {
            throw new NotPossibleException("Student.init: invalid address: " + a);
        }
        // all are valid
        this.id = i;
        this.name = n;
        this.phoneNumber = p;
        this.address = a;
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
    public void setName(String name) {
        if (validateName(name)) {
            this.name = name;
        }
        else {
            throw new NotPossibleException("Student.setName: invalid name: "+ name);
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
    public void setPhoneNumber(String phoneNumber) {
        if(validatePhoneNumber(phoneNumber))
            this.phoneNumber = phoneNumber;
        else
            throw new NotPossibleException("Student.setPhoneNumber: invalid phoneNumber: "+ phoneNumber);
    }

    /**
     * @effects
     *  if address is valid
     *      set this.address = address
     *  else
     *      throws NotPossibleException
     */
    @DOpt(type = OptType.Mutator) @AttrRef("address")
    public void setAddress(String address) {
        if(validateAddress(address))
            this.address = address;
        else
            throw new NotPossibleException("Student.setAddress: invalid address: "+ address);
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
        if (i<1 || i>1.0E9) {
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
        if (n == null || n.length() > 50) {
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
        if (p == null || p.length() > 10) {
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
        if (a == null || a.length() > 100) {
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
        return(validateName(n) && validatePhoneNumber(p) &&
                validateID(i) && validateAddress(a));
    }

    /**
     * @effects
     *  if this is valid
     *      return true
     *  else
     *      return false
     */
    @DOpt(type = OptType.Helper)
    public boolean repOK() { return validate(this.id, this.name, this.phoneNumber, this.address); }

    @Override
    public String toString() {
        if (this.getClass().getSimpleName() == "UndergradStudent") {
            return "UndergradStudent(" + name + ")";
        }
        else if (this.getClass().getSimpleName() == "PostgradStudent") {
            return "PostgradStudent(" + name + ")";
        }
        else {
            return "Student" + name + ")";
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

}
