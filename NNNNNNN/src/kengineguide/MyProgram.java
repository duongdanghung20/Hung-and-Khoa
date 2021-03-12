package kengineguide;

import java.io.File;

import kengine.Doc;
import kengine.Engine;
import kengine.Query;

/**
 * @overview 
 *  A program that demonstrates how to use {@link Engine}.
 *  
 * @author dmle
 *
 */
public class MyProgram {
  public static void main(String[] args) {
    // initialise an engine
    System.out.println("Initialising a KEngine...");
    Engine eng = new Engine();

    // initialise the document collection 
    /*
     String sep = File.separator;
     String dirUrlPrefix = "file:" + sep + sep;
     String docDirPath = "C:\\kengine\\docscol";
     String docDirUrl = dirUrlPrefix + docDirPath;
     e.g. "file:\\C:\kengine\docscol"
     */
    String sep = File.separator;
    String dirUrlPrefix = "file://";
    String docDirName = "docscol";
    String docDirPath = MyProgram.class.getResource(docDirName).getPath();
    String docDirUrl = dirUrlPrefix + docDirPath;

    // add docs from the data directory
    System.out.println("\nAdding docs from URL: " + docDirUrl);
    try {
      eng.addDocs(docDirUrl);
    } catch (Exception e) {
      System.err.println("Error: " + e.getMessage());
    }

    // find some doc: 
    //findDocs(eng);
    
    // query: use both queryFirst and queryMore 
    try {
      String key = "sinh";
      System.out.println("\nQuerying using keyword: " + key);
      Query q = eng.queryFirst(key);
      printMatches(q);
      
      key = "viên";
      System.out.println("Refine query with keyword: " + key);
      q = eng.queryMore(key);
      printMatches(q);

      key = "Nội";
      System.out.println("Refine query with keyword: " + key);
      q = eng.queryMore(key);
      printMatches(q);
      
    } catch (Exception e) {
      System.err.println("Error: " + e.getMessage());
    } 
  }

  /**
   * @effects 
   *  find some test docs in <tt>eng</tt> and print their titles
   */
  private static void findDocs(Engine eng) {
    String[] titles = {
        // invalid titles
        "Trường Đại học Hà nội",
        // valid titles
        "Hanoi University - Tin tức sinh viên",
        "Hanoi University - Tin tức &amp; Sự kiện",
        "Hanoi University - Tin tức &amp; Sự kiện (2) " // note the extra space at the end
    };

    Doc d;
    for (String title : titles) {
      System.out.println("? title = " + title);
      try {
        d = eng.findDoc(title);
        System.out.print("...found\n");
      } catch (Exception e) {
        System.out.print("...not found\n");
        //e.printStackTrace();
      }
    }    
  }

  /**
   * @effects 
   *  if q.matches is empty
   *    print "no matches"
   *  else
   *    print each match in q.matches (one per line)
   */
  private static void printMatches(Query q) {
    // print matches
    if (q.size() == 0) {
      System.out.println("No matches");
    } else {
      System.out.println("Matches");
      for (int di = 0; di < q.size(); di++) {
        Doc d = q.fetch(di);
        System.out.println((di + 1) + ": " + d.title());
      }    
    }
  }
}
