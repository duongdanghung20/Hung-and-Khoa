package xref3;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

/**
 * @overview 
 *
 * @author Duc Minh Le (ducmle)
 *
 * @version 
 */
public class Test {
  public static void main(String[] args) {
    Map<Word,List<Line>> map = new HashMap<>();
    
    String word = "compiler";
    Word w1 = new Word(word),
         w2 = new Word(word);
    
    Line l1 = new Line(1);
    Line l2 = new Line(1);
    Line l3 = new Line(2);
    
    map.put(w1, new LinkedList<>());
    List lines = map.get(w2);
    
    System.out.println("key: " + w2 + ((lines != null) ? ": found" : ": not found"));
    
    lines.add(l1);
    if (!lines.contains(l2)) lines.add(l2);
    if (!lines.contains(l3)) lines.add(l3);
    System.out.println(map);
    
    
    int h1 = w1.hashCode();
    int h2 = w2.hashCode();
    System.out.println("w1: " + w1);
    System.out.println("w2: " + w1);
    System.out.println("w1.hashCode() == w2.hashCode(): " + (h1 == h2));
    System.out.println("w1.equals(w2): " + w1.equals(w2));
  }
}
