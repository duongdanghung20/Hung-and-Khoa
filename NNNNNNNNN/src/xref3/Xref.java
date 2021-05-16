package xref3;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import utils.NotPossibleException;
import utils.fileio.FileHandler;

/**
 * @overview Represents a program that index a document to determine the lines in which each word appears.
 *
 * @author Duc Minh Le (ducmle)
 *
 * @version 
 */
public class Xref {

  /**
   * @effects starts an Xref running
   */
  public static void main(String[] args) {
    Xref prog = new Xref();
    
    String path = "/C:/Users/Administrator/Desktop/Git/Hung-and-Khoa/NNNNNNNNN/xref3/compiler.txt";
    String doc = FileHandler.getFile(path);
    Map<Word,List<Integer>> wm = prog.indexDocument(doc);

    if (wm != null) {
      for (Entry<Word, List<Integer>> e : wm.entrySet() ) {
        System.out.printf("%s: %s%n", 
            e.getKey(), 
            e.getValue());
      }
    } else {
      System.out.println("Empty index");
    }
  }
  
 /**
  * @effects 
  *   if doc is not a text document
  *     throws NotPossibleException
  *   else
  *     for each word containing more than one letter,
  *     record the lines in which it appears (e.g. compiler: 3, 17, 25).
  *     Return the result.
  * @pseudocode (validation of the design)
  *   initialise d = Document(doc)
  *   Map<Word,List<Line>> wm = d.wordLocations()
  *   convert wm to Map<Word,List<Integer>>
  *   return the result
  */
  Map<Word, List<Integer>> indexDocument(String doc) throws NotPossibleException {
    Document d = new Document(doc);
    Map<Word,List<Line>> m = d.wordLocations();
    Map<Word,List<Integer>> wm = new LinkedHashMap<>();
    
    for (Entry<Word, List<Line>> e : m.entrySet()) {
      Word w = e.getKey();
      List<Line> lines = e.getValue();
      List<Integer> lineNos = new ArrayList<>();
      for (Line l : lines) lineNos.add(l.getLineNo());
      wm.put(w, lineNos);
    }
    
    return wm;
  }
}
