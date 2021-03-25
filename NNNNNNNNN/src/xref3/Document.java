package xref3;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import utils.AttrRef;
import utils.DomainConstraint;
import utils.NotPossibleException;

/**
 * @overview 
 *  Represents a document
 *  
 * @attributes ...
 * 
 * @object ...
 * 
 * @abstract_properties ...
 * 
 *   
 * @author Duc Minh Le (ducmle)
 *
 * @version 
 */
public class Document {
  
  // TODO: add @DomainConstraint
//  private List<Line> lines;
  
  @DomainConstraint(mutable=false, optional=false)
  private String doc;
  
  @DomainConstraint(mutable=false)
  private Map<Word,List<Line>> wordLocations;
  
  /**
   * @effects 
   *   if doc is not a text document
   *     throws NotPossibleException
   *   else
   *    initialise this with words in doc
   */
  public Document(@AttrRef("doc") String doc) throws NotPossibleException {
    this.doc = doc;
  }
  
  /**
   * @effects 
   *  if this.wordLocations have not been extracted
   *    create a Map of words in this containing more than one letter and 
   *    the lines where they appear (e.g. compiler: 3, 17, 25...)
   *    record result in this.wordLocations
   *  
   *  return this.wordLocations
   */
  public Map<Word,List<Line>> wordLocations() {
    if (wordLocations == null) {
      // extract from doc
      doc = doc.trim();
      final String linesep = System.getProperty("line.separator");
      
      if (!doc.isEmpty()) {
        // 1st split: split document to lines
        String[] lines = doc.split(linesep);
        String line; Line lineObj;
        Iterator<Word> words;
        for (int lineno = 0; lineno < lines.length; lineno++) {
          line = lines[lineno].trim();
          if (line.isEmpty()) // empty line
            continue;

          // 2nd split: split line to words
          int llineno = lineno+1; // line numbers start from 1
          lineObj = createLine(line, llineno);
          
          words = lineObj.words();
          
          while (words.hasNext()) {
            Word w = words.next();
            if (wordLocations == null)
              wordLocations = new LinkedHashMap<>();

            //check if wlines existed => immediately add the word in. else create the line.
            List<Line> wlines = wordLocations.get(w);
            if (wlines == null) {
              wlines = new ArrayList<>();
              wordLocations.put(w, wlines);
            }

            //1 line can have duplicated words. check if this word is duplicated.
            if (!wlines.contains(lineObj))  // unique
              wlines.add(lineObj); 
          }
        }
      }
    }
    
    return wordLocations;
  }
  
  /**
   * @effects 
   *  if lineStr is a valid line
   *    create a {@link Line} whose number is <tt>llineno</tt> and 
   *    containing all the non-single-char words in lineStr
   */
  private Line createLine(String lineStr, int llineno) throws NotPossibleException {
    if (lineStr == null || lineStr.length() < 2) {
      throw new NotPossibleException("Line.init: invalid line string: '" + lineStr + "'");
    }

    Line line = new Line(llineno);
    final String wordsep = "\\s";

    String[] words = lineStr.split(wordsep);
    
    for (String w : words) {
      if (w.length() > 1) { // not a single-char word 
        line.addWord(canon(w));
      }
    }
    
    return line;
  }

  /**
   * @effects returns the canonicalised form of w
   */
  private String canon(String w) {
    String[] specials = {",", ".", ":", ";", "!", "?", "[", "]", "(", ")" };
    w = w.trim();
    
    for (String s : specials) {
      if (w.startsWith(s))
        w = w.substring(1);
      if (w.endsWith(s))
        w = w.substring(0,w.length()-1);
    }
    
    return w;
  }
}
