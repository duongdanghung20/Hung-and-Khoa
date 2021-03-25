package xref3;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

import utils.AttrRef;
import utils.DOpt;
import utils.DomainConstraint;
import utils.NotPossibleException;
import utils.OptType;

/**
 * @overview 
 *  Represents a line in a document.
 *  
 * @attributes ...
 * 
 * @object ...
 * 
 * @abstract_properties ...
 * 
 * @author Duc Minh Le (ducmle)
 *
 * @version 
 */
public class Line {

  private static final int MIN_LINENO = 1;
  
  @DomainConstraint(mutable=false, optional=false,min=MIN_LINENO)
  private int lineNo;
  
  @DomainConstraint(mutable=true, optional=false)
  private List<Word> words;
  
  
  /**
   * @effects 
   */
  public Line(@AttrRef("lineNo") int lineNo) throws NotPossibleException {
    if (lineNo < MIN_LINENO) {
      throw new NotPossibleException("Line.init: invalid line number: " + lineNo);
    }
    
    this.lineNo = lineNo;
    this.words = new LinkedList<>();
  }

//  @DOpt(type=OptType.MutatorAdd)
//  public void addWord(Word w) {
//    words.add(w);
//  }

  @DOpt(type=OptType.MutatorAdd)
  public void addWord(String w) {
    words.add(new Word(w));
  }
  
  @DOpt(type=OptType.MutatorRemove)
  public void removeWord(Word w) {
    words.remove(w);
  }
  
  @DOpt(type=OptType.ObserverContains)
  public void contains(Word w) {
    words.contains(w);
  }
  
  @DOpt(type=OptType.ObserverSize)
  public int size() {
    return words.size();
  }
  
  /**
   * 
   * @effects 
   *  if this is empty 
   *    return null
   *  else
   *    return an Iterator of words contained in this
   */
  @DOpt(type=OptType.ObserverIterator)
  public Iterator<Word> words() {
    if (size() == 0) {
      return null;
    } else {
      return words.iterator();
    }
  }

  /**
   * @effects return lineNo
   */
  @DOpt(type=OptType.Observer) @AttrRef("lineNo")
  public int getLineNo() {
    return lineNo;
  }

  /* (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  /**
   * @effects 
   * 
   * @version 
   */
  @Override
  public String toString() {
    return lineNo+"";
  }

  /* (non-Javadoc)
   * @see java.lang.Object#equals(java.lang.Object)
   */
  /**
   * @effects 
   * 
   * @version 
   */
  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Line other = (Line) obj;
    if (lineNo != other.lineNo)
      return false;
    return true;
  }
  
  
}
