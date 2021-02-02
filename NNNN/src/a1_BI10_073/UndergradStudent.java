package a1_BI10_073;
import a1_BI10_073.utils.*;


/**
 * @overview UndergradStudent (Undergraduate Student) is a person who go to school and
             take part in the Bachelor program
 * @abstract_properties
 *    P_Student /\
 *    min(id) = 10^5 /\ max(id) = 10^8
 * @author Duong Dang Hung
 */
public class UndergradStudent extends Student {

    /**
     * @effects
     *            if i,n,p,a are valid
     *              initialise this as UndergradStudent:<i,n,p,a>
     *            else
     *              print error message
     *
     */
    public UndergradStudent(@AttrRef("id") int i,@AttrRef("name") String n,
                            @AttrRef("phoneNumber") String p,@AttrRef("address") String a){
        super(i,n,p,a);
    }

    @Override
    public String toString() {
        return "UndergradStudent(" + getName() + ")";
    }

    /**
     * @effects
     *            if i is valid
     *              return true
     *            else
     *              return false
     */
    @Override
    @DomainConstraint(type = "Integer", min = 1.0E5, max = 1.0E8, optional = false)
    protected boolean validateID(int i) {
        if(!super.validateID(i))
            return false;
        if(i < 1.0E5 || i > 1.0E8)
            return false;

        return true;
    }

    @Override
    public boolean repOK() {
        return super.repOK();
    }
}
