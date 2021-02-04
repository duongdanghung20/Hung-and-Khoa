package a1_BI10_073;
import utils.*;
import java.util.*;
import java.math.*;

/**
 * @overview PostgradStudent is a person who go to school after completed Bachelor program
 * @attributes
 *  gpa Float float
 * @object A typical PostgradStudent is <i,n,p,a,g> where id(i), name(n), phoneNumber(p), address(a), gpa(g)
 * @abstract_properties
 *    P_Student /\
 *    min(id) = 10^8+1 /\ max(id) = 10^9 /\
 *    mutable(gpa) = true /\ optional(gpa) = false /\ min(gpa) = 0 /\ max(gpa) = 4
 * @author Duong Dang Hung
 */
public class PostgradStudent extends Student {
    private static final int MIN_ID = 100000001;
    private static final int MAX_ID = 1000000000;
    @DomainConstraint(type = "Float", mutable = true, optional = false, min = 0.0, max = 4.0)
    private float gpa;

    /**
     * @effects
     *            if i,n,p,a,g are valid
     *              initialise this as PostgradStudent:<i,n,p,a,g>
     *            else
     *              print error message
     *
     */
    public PostgradStudent(@AttrRef("id") int id,@AttrRef("name") String name, @AttrRef("phoneNumber") String phoneNumber, @AttrRef("address") String address, @AttrRef("gpa") float gpa) {
        super(id,name,phoneNumber,address);
        if(!validateGpa(gpa)) {
            System.err.println("PostgradStudent.init: invalid gpa");
        }
        else {
            this.gpa = gpa;
        }
    }

    /**
     *
     * @effects
     *  return this.gpa
     */
    @DOpt(type = OptType.Observer) @AttrRef("gpa")
    public float getGpa() {
        return this.gpa;
    }


    /**
     * @effects
     *  if gpa is valid
     *    set this.gpa = gpa
     *  else
     *    print error message
     */
    @DOpt(type = OptType.Mutator) @AttrRef("gpa")
    public void setGpa(float gpa) {
        if (validateGpa(gpa)) {
            this.gpa = gpa;
        } else {
            System.err.println("PostgradStudent.setGpa: gpa is not valid " + gpa);
        }
    }

    /**
     *
     * @effects
     *  if this satisfies rep invariant
     *      return true
     *  else
     *      return false
     */
    @Override
    public boolean repOK() {
        if (super.repOK()) {
            return validateGpa(gpa);
        }
        else {
            return false;
        }
    }

    @Override
    public String toString() {
        return "PostgradStudent(" + getName() + ")";
    }

    /**
     * @effects
     *  if gpa is valid
     *    return true
     *  else
     *    return false
     */
    private boolean validateGpa(float gpa) {
        if (gpa < 0.0 || gpa > 4.0 || (Object) gpa == null) {
            return false;
        }
        return true;
    }

    /**
     * @effects
     *            if i is valid
     *              return true
     *            else
     *              return false
     */
    @Override
    @DomainConstraint(type = "Integer", min = MIN_ID, max = MAX_ID, optional = false)
    protected boolean validateID(int i) {
        if(!super.validateID(i))
            return false;
        if(i < MIN_ID || i > MAX_ID)
            return false;

        return true;
    }
}
