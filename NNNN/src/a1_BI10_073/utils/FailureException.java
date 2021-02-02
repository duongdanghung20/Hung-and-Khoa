package a1_BI10_073.utils;

/**
 * @overview An exception that is thrown when an unexpected system failures
 *           occur.
 * 
 * @author dmle
 * 
 */
public class FailureException extends RuntimeException {
  public FailureException(String msg) {
    super(msg);
  }
}
