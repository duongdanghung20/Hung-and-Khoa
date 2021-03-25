package xref3;

import utils.AttrRef;
import utils.DOpt;
import utils.DomainConstraint;
import utils.NotPossibleException;
import utils.OptType;

/**
 * @overview 
 *  Represents a word
 * 
 * @attribute
 *  label String
 *  
 * @object 
 *  A typical word is <l> where label(l)
 *  
 * @abstract_properties
 *  mutable(label)=false /\ optional=false /\ length(255) /\
 *    label.length > 1
 *  
 * @author Duc Minh Le (ducmle)
 */
public class Word {
  
  private final int MAX_LEN = 255;
  
  @DomainConstraint(optional=false, mutable=false, length=MAX_LEN)
  private String label;
  
  /**
   * @effects
   *  if content is valid
   *    initialise this with content
   *  else
   *    throw NotPossiblException
   */
  public Word(@AttrRef("label") String content) throws NotPossibleException {
    if (!validateContent(content)) {
      throw new NotPossibleException("Word.init: invalid word: " + content);
    }
    
    this.label = content;
  }

  /**
   * @effects 
   *  if label is valid
   *    return true
   *  else
   *    return false
   * @version 
   */
  private boolean validateContent(String label) {
    if (label != null && label.length() > 1 && 
        label.length() <= MAX_LEN
        ) {
      return true;
    } else {
      return false;
    }
  }

  /**
   * @effects return label
   */
  @DOpt(type=OptType.Observer) @AttrRef("label")
  public String getLabel() {
    return label;
  }

  /**
   * @effects 
   * 
   * @version 
   */
  @Override
  public String toString() {
    return label;
  }

  /**
   * @effects 
   * 
   * @version 
   */
  @Override
  public int hashCode() {
//    final int prime = 31;
//    int result = 1;
//    result = prime * result + ((label == null) ? 0 : label.hashCode());
//    return result;
    return label.hashCode();
  }

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
    
    Word other = (Word) obj;
    if (label == null) {
      if (other.label != null)
        return false;
    } else if (!label.equals(other.label))
      return false;
    return true;
  }
}
