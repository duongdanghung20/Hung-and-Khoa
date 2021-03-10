import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) {
        int i = 1;
        long l = 10;
        try {
            PrintWriter out = new PrintWriter(new FileWriter("test.txt"));
            out.println("Hello " + i + " " + l);
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            Scanner sc = new Scanner(new FileInputStream("test.txt"));
            String s = sc.next();
            int j = sc.nextInt();
            while (sc.hasNextLong()) {
                long aLong = sc.nextLong();
                System.out.println(aLong);
            }
            System.out.println(s);
            System.out.println(j);
            sc.close();
        } catch(IOException e) {
            e.printStackTrace();
        }
    }
}