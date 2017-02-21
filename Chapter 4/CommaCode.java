class CommaCode {
  public static void main(String[] args) {
      String[] spam = {"apples","bananas", "tofu", "cats"};
      System.out.println(convertsToString(spam));
    }
  public static String convertsToString(String[] list){
    String newString = "";
    for (int i=0; i<list.length-1; i++) {
        newString += list[i] + ", ";
    }
    newString += "and " + list[list.length-1];
    return newString;
    }
}