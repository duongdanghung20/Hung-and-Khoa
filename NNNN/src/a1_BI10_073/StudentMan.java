package a1_BI10_073;
import utils.*;
import java.util.*;

/**
 * @overview A test application for students.
 *
 * @author Duong Dang Hung
 */

public class StudentMan {
    public static void main(String[] args) {
        // create objects
        try {
            Student s;
            s = new UndergradStudent((int) 1.0E5 + 2, "Duong Dang Hung", "0886865966", "USTH");
            // use objects
            System.out.println(s.toString());
            System.out.println("-Id: " + s.getId());
            System.out.println("-Name: " + s.getName());
            System.out.println("-Phone number: " + s.getPhoneNumber());
            System.out.println("-Address: " + s.getAddress());
        } catch (NotPossibleException e) {
            e.printStackTrace();
        }

        try {
            PostgradStudent s;
            s = new PostgradStudent((int) 1.0E8 + 2, "Bui Bich Ngoc", "0222222222", "Banking Academy", 4);
            System.out.println("\n" + s.toString());
            System.out.println("-Id: " + s.getId());
            System.out.println("-Name: " + s.getName());
            System.out.println("-GPA: " + s.getGpa());
            System.out.println("-Phone number: " + s.getPhoneNumber());
            System.out.println("-Address: " + s.getAddress());
        } catch (NotPossibleException e) {
            e.printStackTrace();
        }

        Student s1 = new Student((int) 1.0E5 + 2, "Duong Dang Hung", "0886865966", "USTH");
        Student s2 = new Student((int) 1.0E8 + 2, "Bui Bich Ngoc", "0222222222", "Banking Academy");
        if( s1.compareTo(s2) > 0 ) {
            System.out.println("\nHung before Ngoc");
        }
        else if ( s1.compareTo(s2) < 0) {
            System.out.println("\nHung after Ngoc");
        }
        else {
            System.out.println("\nHung equals Ngoc");
        }

    }
}


