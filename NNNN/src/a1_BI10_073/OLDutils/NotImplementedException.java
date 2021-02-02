package a1_BI10_073.utils;

/**
 * @overview <code>NotImplementedException<code> is a run-time exception that is thrown 
 *           by a method that does not provide an implementation of its 
 *           specification
 *            
 * @author dmle
 *
 */
public class NotImplementedException extends RuntimeException {
  public NotImplementedException() {  
  }
  
  public NotImplementedException(String s) {
    super(s);
  }
}
