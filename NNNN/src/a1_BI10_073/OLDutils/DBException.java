package a1_BI10_073.utils;

/**
 * @overview An exception that is thrown when an error occured with database connection 
 *           or processing
 * 
 * @author dmle
 * 
 */
public class DBException extends RuntimeException {
  public DBException(String msg) {
    super(msg);
  }
}
