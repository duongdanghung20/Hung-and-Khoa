package a1_BI10_073;
import utils.*;


/**
 * @overview UndergradStudent (Undergraduate Student) is a person who go to school and
             take part in the Bachelor program
 * @abstract_properties
 *    P_Student /\
 *    min(id) = 10^5 /\ max(id) = 10^8
 * @author Duong Dang Hung
 */
public class UndergradStudent extends Student {
    private static final int MIN_ID = 100000;
    private static final int MAX_ID = 100000000;
    /**
     * @effects
     *            if id, name, phoneNumber, address are valid
     *              initialise this as UndergradStudent:<id, name, phoneNumber, address>
     *            else
     *              print error message
     *
     */
    public UndergradStudent(@AttrRef("id") int id, @AttrRef("name") String name, @AttrRef("phoneNumber") String phoneNumber, @AttrRef("address") String address) throws NotPossibleException {
        super(id, name, phoneNumber, address);
    }

    /**
     * @effects return a string present UndergradStudent
     */
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
    @DomainConstraint(type = "Integer", min = MIN_ID, max = MAX_ID, optional = false)
    protected boolean validateID(int i) {
        if(!super.validateID(i))
            return false;
        if(i < MIN_ID || i > MAX_ID)
            return false;

        return true;
    }

    @Override
    public boolean repOK() {
        return super.repOK();
    }
}
