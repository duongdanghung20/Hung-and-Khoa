package a1_BI10_073.utils;

/**
 * Represent exceptions that are thrown when a collection does not have any elements.  
 * 
 * @author dmle
 *
 */
public class EmptyException extends RuntimeException {
  public EmptyException(String msg) {
    super(msg);
  }
}
